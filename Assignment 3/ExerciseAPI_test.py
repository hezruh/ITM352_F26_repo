import importlib.util
import tempfile
import time
import unittest
from pathlib import Path


APP_FILE = Path(__file__).resolve().parent / "templates" / "Assignment3Program.py"
SPEC = importlib.util.spec_from_file_location("assignment3_program", APP_FILE)
quiz_app = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(quiz_app)


class Assignment3QuizTests(unittest.TestCase):
    def setUp(self):
        self.temp_directory = tempfile.TemporaryDirectory()
        quiz_app.SCORE_FILE = Path(self.temp_directory.name) / "quiz_scores.json"
        quiz_app.SCORE_FILE.write_text("[]", encoding="utf-8")
        quiz_app.app.config["TESTING"] = True
        self.client = quiz_app.app.test_client()

    def tearDown(self):
        self.temp_directory.cleanup()

    def identify_user(self, name="Test User"):
        with self.client.session_transaction() as session:
            session["user_name"] = name

    def test_welcome_requires_user_name(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Enter your name before starting.", response.data)

    def test_name_is_saved_and_returning_user_is_welcomed(self):
        response = self.client.post("/", data={"name": "  Alex  "})
        self.assertEqual(response.status_code, 302)

        with self.client.session_transaction() as session:
            self.assertEqual(session["user_name"], "Alex")

        response = self.client.get("/")
        self.assertIn(b"Welcome back, Alex!", response.data)

    def test_questions_api_returns_json(self):
        response = self.client.get("/api/questions")

        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.get_json(), dict)
        self.assertGreater(len(response.get_json()), 0)

    def test_score_api_can_store_and_retrieve_scores(self):
        response = self.client.post("/api/scores", json={
            "name": "Alex",
            "generation": "Millennial",
            "scores": [2, 1, 1, 1],
            "total_questions": 5,
        })
        self.assertEqual(response.status_code, 201)

        response = self.client.get("/api/scores")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.get_json()), 1)
        self.assertEqual(response.get_json()[0]["name"], "Alex")

    def test_score_api_rejects_invalid_scores(self):
        response = self.client.post("/api/scores", json={
            "name": "Alex",
            "generation": "Unknown",
            "scores": [True, 1, 1, 1],
        })

        self.assertEqual(response.status_code, 400)

    def test_quiz_shuffles_answers_and_records_feedback(self):
        self.identify_user()
        response = self.client.get("/quiz")
        self.assertEqual(response.status_code, 200)

        with self.client.session_transaction() as session:
            question = session["quiz_questions"][0]
            answer = session["visible_options"][0]
            self.assertCountEqual(session["visible_options"], question["answers"])

        response = self.client.post("/quiz", data={"answer": answer})
        self.assertEqual(response.status_code, 302)

        with self.client.session_transaction() as session:
            self.assertIn("answer_feedback", session)
            self.assertEqual(len(session["answer_history"]), 1)

        response = self.client.get("/quiz")
        self.assertIn(b"Answer Feedback", response.data)
        self.assertIn(b"Next Question", response.data)

    def test_hint_removes_exactly_two_generation_options(self):
        self.identify_user()
        self.client.get("/quiz")

        response = self.client.post("/quiz", data={"action": "fifty_fifty"})
        self.assertEqual(response.status_code, 302)

        response = self.client.get("/quiz")
        self.assertIn(b"Select two generations", response.data)

        response = self.client.post("/quiz", data={
            "action": "remove_generations",
            "removed_generations": ["0", "3"],
        })
        self.assertEqual(response.status_code, 302)

        with self.client.session_transaction() as session:
            self.assertFalse(session["fifty_fifty_available"])
            self.assertEqual(len(session["visible_options"]), 2)

    def test_invalid_hint_selection_displays_validation_message(self):
        self.identify_user()
        self.client.get("/quiz")
        self.client.post("/quiz", data={"action": "fifty_fifty"})

        response = self.client.post("/quiz", data={
            "action": "remove_generations",
            "removed_generations": ["0"],
        })

        self.assertIn(b"Please select exactly two generations.", response.data)

    def test_timer_starts_at_fifteen_seconds(self):
        self.identify_user()
        response = self.client.get("/quiz")

        self.assertEqual(quiz_app.QUESTION_TIME_LIMIT_SECONDS, 15)
        self.assertIn(b'id="quiz-timer"', response.data)
        self.assertTrue(
            b'data-seconds-left="14"' in response.data
            or b'data-seconds-left="15"' in response.data
        )

    def test_server_redirects_expired_timer_to_results(self):
        self.identify_user()
        self.client.get("/quiz")

        with self.client.session_transaction() as session:
            session["question_deadline"] = time.time() - 1

        response = self.client.get("/quiz")
        self.assertEqual(response.status_code, 302)
        self.assertTrue(response.location.endswith("/result"))

    def test_progress_bar_updates_after_answer(self):
        self.identify_user()
        self.client.get("/quiz")

        with self.client.session_transaction() as session:
            answer = session["visible_options"][0]

        self.client.post("/quiz", data={"answer": answer})
        response = self.client.get("/quiz")

        self.assertIn(b"Quiz Progress: 1 of 5", response.data)
        self.assertIn(b"width: 20%;", response.data)

    def test_result_uses_generation_color_classes(self):
        self.identify_user()
        with self.client.session_transaction() as session:
            session["scores"] = [1, 1, 1, 2]
            session["quiz_questions"] = [{}, {}, {}, {}, {}]
            session["answer_history"] = []

        response = self.client.get("/result")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"result-blue", response.data)
        self.assertIn(b"result-green", response.data)
        self.assertIn(b"result-yellow", response.data)
        self.assertIn(b"result-red", response.data)

    def test_review_answers_page_and_back_button(self):
        self.identify_user()
        with self.client.session_transaction() as session:
            session["scores"] = [1, 1, 1, 2]
            session["quiz_questions"] = [{}, {}, {}, {}, {}]
            session["answer_history"] = [{
                "question_number": 1,
                "question": "Test question",
                "selected_answer": "Test answer",
                "generation": "Millennial",
                "color": "blue",
                "comment": "Test comment",
            }]

        response = self.client.get("/review")
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Review Your Answers", response.data)
        self.assertIn(b"Test question", response.data)
        self.assertIn(b"Back to Results", response.data)


if __name__ == "__main__":
    unittest.main()
