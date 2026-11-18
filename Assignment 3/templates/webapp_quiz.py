# application to manage the quiz webapp
# name: Hezra Calventas
# Date: November 13, 2026

import json
import random
from pathlib import Path
from datetime import datetime, timezone

from flask import Flask, jsonify, redirect, render_template, request, session, url_for

BASE_DIR = Path(__file__).resolve().parents[2]
QUESTION_FILE = BASE_DIR / "Assignment 3" / "questions.json"
SCORE_FILE = BASE_DIR / "Assignment 3" / "quiz_scores.json"
COMMENTS_FILE = BASE_DIR / "Assignment 3" / "generation_comments.json"
NUM_QUESTIONS_PER_QUIZ = 5
GENERATIONS = ["Millennial", "Zoomer", "Gen Alpha", "Baby Boomer"]

def load_question_bank():
    """Load quiz questions and answer choices from the JSON data file."""
    with QUESTION_FILE.open(encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise ValueError("Question data must be a JSON object")
    return data

def load_generation_comments():
    """Load snarky feedback comments for each generation from JSON."""
    with COMMENTS_FILE.open(encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise ValueError("Generation comment data must be a JSON object")
    if any(
        not isinstance(data.get(generation), list)
        or not data[generation]
        or not all(isinstance(comment, str) for comment in data[generation])
        for generation in GENERATIONS
    ):
        raise ValueError("Every generation must have a non-empty string comment list")
    return data

def load_scores():
    """Retrieve saved quiz results from the JSON score file."""
    if not SCORE_FILE.exists():
        return []
    with SCORE_FILE.open(encoding="utf-8") as file:
        data = json.load(file)
    return data if isinstance(data, list) else []

def save_score(scores, generation, total_questions=None):
    """Append one completed quiz result to the JSON score history."""
    score_history = load_scores()
    score_history.append({
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "generation": generation,
        "scores": dict(zip(GENERATIONS, scores)),
        "total_questions": total_questions if total_questions is not None else sum(scores),
    })
    with SCORE_FILE.open("w", encoding="utf-8") as file:
        json.dump(score_history, file, indent=2)
    return score_history

QUESTION_BANK = load_question_bank()
GENERATION_COMMENTS = load_generation_comments()

app = Flask(
    __name__,
    template_folder=str(Path(__file__).resolve().parent),
    static_folder=str(Path(__file__).resolve().parents[1] / "static"),
)
app.secret_key = "quiz-app-development-key"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/questions', methods=['GET'])
def get_questions():
    """Serve the question bank and answer choices from server-side JSON storage."""
    try:
        response = jsonify(load_question_bank())
        response.headers["Cache-Control"] = "no-store"
        return response
    except (OSError, json.JSONDecodeError, ValueError) as error:
        return jsonify({"error": "Questions could not be loaded.", "details": str(error)}), 500

@app.route('/api/scores', methods=['GET', 'POST'])
def score_api():
    """Retrieve or store quiz score records as JSON through RESTful requests."""
    if request.method == 'GET':
        try:
            response = jsonify(load_scores())
            response.headers["Cache-Control"] = "no-store"
            return response
        except (OSError, json.JSONDecodeError) as error:
            return jsonify({"error": "Scores could not be loaded.", "details": str(error)}), 500

    if not request.is_json:
        return jsonify({"error": "Request body must use application/json."}), 415

    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"error": "Request body must be a JSON object."}), 400

    score_values = data.get("scores")
    generation = data.get("generation")
    total_questions = data.get("total_questions")

    if (
        not isinstance(score_values, list)
        or len(score_values) != len(GENERATIONS)
        or not all(
            isinstance(value, int)
            and not isinstance(value, bool)
            and value >= 0
            for value in score_values
        )
        or generation not in GENERATIONS
        or (
            total_questions is not None
            and (
                not isinstance(total_questions, int)
                or isinstance(total_questions, bool)
                or total_questions < 0
            )
        )
    ):
        return jsonify({"error": "Provide valid generation scores."}), 400

    try:
        score_history = save_score(score_values, generation, total_questions)
    except (OSError, json.JSONDecodeError) as error:
        return jsonify({"error": "Score could not be saved.", "details": str(error)}), 500
    return jsonify(score_history[-1]), 201

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    if "quiz_questions" not in session:
        question_items = random.sample(
            list(QUESTION_BANK.items()),
            k=min(NUM_QUESTIONS_PER_QUIZ, len(QUESTION_BANK)),
        )
        session["quiz_questions"] = [
            {"question": question, "answers": answers}
            for question, answers in question_items
        ]
        session["question_number"] = 0
        session["scores"] = [0] * len(GENERATIONS)
        session["fifty_fifty_available"] = True
        session["fifty_fifty_selecting"] = False
        session["visible_options"] = random.sample(
            session["quiz_questions"][0]["answers"],
            k=len(session["quiz_questions"][0]["answers"]),
        )

    fifty_fifty_error = None
    if request.method == 'POST':
        if request.form.get("action") == "continue":
            session.pop("answer_feedback", None)
            current_number = session["question_number"]
            if current_number == len(session["quiz_questions"]):
                return redirect(url_for("result"))

            next_answers = session["quiz_questions"][current_number]["answers"]
            session["visible_options"] = random.sample(
                next_answers,
                k=len(next_answers),
            )
            return redirect(url_for("quiz"))

        if request.form.get("action") == "fifty_fifty":
            if session["fifty_fifty_available"]:
                session["fifty_fifty_selecting"] = True
            return redirect(url_for("quiz"))

        if request.form.get("action") == "remove_generations":
            selected_generations = request.form.getlist("removed_generations")
            try:
                selected_indices = {int(index) for index in selected_generations}
            except ValueError:
                selected_indices = set()

            if (
                len(selected_indices) != 2
                or not selected_indices.issubset(range(len(GENERATIONS)))
            ):
                fifty_fifty_error = "Please select exactly two generations."
            else:
                current_number = session["question_number"]
                current_question = session["quiz_questions"][current_number]
                remaining_options = [
                    answer
                    for index, answer in enumerate(current_question["answers"])
                    if index not in selected_indices
                ]
                session["visible_options"] = random.sample(
                    remaining_options,
                    k=len(remaining_options),
                )
                session["fifty_fifty_available"] = False
                session["fifty_fifty_selecting"] = False
                return redirect(url_for("quiz"))

        if fifty_fifty_error is None:
            answer = request.form.get("answer")
            current_number = session["question_number"]
            current_question = session["quiz_questions"][current_number]
            if answer not in session["visible_options"]:
                return redirect(url_for("quiz"))

            answer_position = current_question["answers"].index(answer)
            scores = session["scores"]
            scores[answer_position] += 1
            session["scores"] = scores
            generation = GENERATIONS[answer_position]
            previous_comments = session.get("previous_generation_comments", {})
            available_comments = [
                comment
                for comment in GENERATION_COMMENTS[generation]
                if comment != previous_comments.get(generation)
            ]
            selected_comment = random.choice(available_comments)
            previous_comments[generation] = selected_comment
            session["previous_generation_comments"] = previous_comments
            answered_question_number = current_number + 1
            current_number += 1
            session["question_number"] = current_number
            session["fifty_fifty_selecting"] = False
            session["answer_feedback"] = {
                "selected_answer": answer,
                "generation": generation,
                "comment": selected_comment,
                "question": current_question["question"],
                "question_number": answered_question_number,
                "is_final": current_number == len(session["quiz_questions"]),
            }
            return redirect(url_for("quiz"))

    answer_feedback = session.get("answer_feedback")
    if answer_feedback:
        return render_template(
            'quiz.html',
            question=answer_feedback["question"],
            question_number=answer_feedback["question_number"],
            total_questions=len(session["quiz_questions"]),
            options=[],
            fifty_fifty_available=False,
            fifty_fifty_selecting=False,
            fifty_fifty_error=None,
            generations=GENERATIONS,
            feedback=answer_feedback,
        )

    current_number = session["question_number"]
    current_question = session["quiz_questions"][current_number]
    return render_template(
        'quiz.html',
        question=current_question["question"],
        question_number=current_number + 1,
        total_questions=len(session["quiz_questions"]),
        options=session["visible_options"],
        fifty_fifty_available=session["fifty_fifty_available"],
        fifty_fifty_selecting=session.get("fifty_fifty_selecting", False),
        fifty_fifty_error=fifty_fifty_error,
        generations=GENERATIONS,
        feedback=None,
    )

@app.route('/result')
def result():
    if "scores" not in session:
        return redirect(url_for("index"))

    scores = session["scores"]
    highest_score = max(scores)
    generation = GENERATIONS[scores.index(highest_score)]
    if not session.get("result_saved", False):
        try:
            save_score(scores, generation, len(session["quiz_questions"]))
            session["result_saved"] = True
        except (OSError, json.JSONDecodeError) as error:
            app.logger.error("Could not save quiz score: %s", error)

    return render_template(
        'result.html',
        scores=zip(GENERATIONS, scores),
        generation=generation,
        total_questions=len(session["quiz_questions"]),
    )

@app.route('/start')
def start():
    session.clear()
    return redirect(url_for("quiz"))

def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()