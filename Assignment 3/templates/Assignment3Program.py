# application to manage the quiz webapp
# name: Hezra Calventas
# Date: November 13, 2026

"""
AI Note: I used GitHub Copilot as a coding reference to explain and implement
the Flask routes, session data, JSON storage, timed quiz, hint feature,
feedback colors, progress bar, and answer review. I reviewed and integrated
the generated sections into this application and adjusted them to fit my
existing quiz structure and requirements.
"""

# --------------------------------------------------------------------------
# Application imports and file configuration
# --------------------------------------------------------------------------
import json
import random
import time
from pathlib import Path
from datetime import datetime, timezone
from datetime import timedelta

from flask import Flask, jsonify, redirect, render_template, request, session, url_for

# File paths used for questions, comments, and persisted quiz scores.
BASE_DIR = Path(__file__).resolve().parents[2]
QUESTION_FILE = BASE_DIR / "Assignment 3" / "questions.json"
SCORE_FILE = BASE_DIR / "Assignment 3" / "quiz_scores.json"
COMMENTS_FILE = BASE_DIR / "Assignment 3" / "generation_comments.json"

# Quiz configuration constants used throughout the application.
NUM_QUESTIONS_PER_QUIZ = 5
QUESTION_TIME_LIMIT_SECONDS = 15
GENERATIONS = ["Millennial", "Zoomer", "Gen Alpha", "Baby Boomer"]

# Mapping used to make feedback and result colors consistent by generation.
GENERATION_COLORS = {
    "Millennial": "blue",
    "Zoomer": "green",
    "Gen Alpha": "yellow",
    "Baby Boomer": "red",
}

# --------------------------------------------------------------------------
# JSON data loading and score storage
# --------------------------------------------------------------------------
def load_question_bank():
    # Notice: Questions are loaded from an external JSON file instead of being hard-coded.
    """Load quiz questions and answer choices from the JSON data file."""
    with QUESTION_FILE.open(encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, dict):
        raise ValueError("Question data must be a JSON object")
    return data

def load_generation_comments():
    # Individual Requirement 4: Visual and interactive feedback uses comments from external JSON data.
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
    # Notice: The application creates an empty history if the score file does not exist.
    """Retrieve saved quiz results from the JSON score file."""
    if not SCORE_FILE.exists():
        return []
    with SCORE_FILE.open(encoding="utf-8") as file:
        data = json.load(file)
    return data if isinstance(data, list) else []

def save_score(scores, generation, total_questions=None, name=None):
    # Notice: Every completed quiz creates a new JSON record while preserving earlier results.
    """Append one completed quiz result to the JSON score history."""
    score_history = load_scores()
    score_history.append({
        "completed_at": datetime.now(timezone.utc).isoformat(),
        "name": name,
        "generation": generation,
        "scores": dict(zip(GENERATIONS, scores)),
        "total_questions": total_questions if total_questions is not None else sum(scores),
    })
    with SCORE_FILE.open("w", encoding="utf-8") as file:
        json.dump(score_history, file, indent=2)
    return score_history

QUESTION_BANK = load_question_bank()
GENERATION_COMMENTS = load_generation_comments()

# --------------------------------------------------------------------------
# Flask application configuration
# --------------------------------------------------------------------------
app = Flask(
    __name__,
    template_folder=str(Path(__file__).resolve().parent),
    static_folder=str(Path(__file__).resolve().parents[1] / "static"),
)
app.secret_key = "quiz-app-development-key"
app.permanent_session_lifetime = timedelta(days=30)

def get_user_history(name):
    # Individual Requirement: Persistent User Identification and History
    # Notice: A user's history is selected by matching the saved name field.
    """Return all saved quiz results for one identified user."""
    return [
        score_record
        for score_record in load_scores()
        if score_record.get("name") == name
    ]

@app.route('/', methods=['GET', 'POST'])
def index():
    # Individual Requirement: Persistent User Identification and History
    name_error = None

    if request.method == 'POST':
        # Notice: Remove extra spaces before validating the user's name.
        name = request.form.get("name", "").strip()
        if len(name) < 1 or len(name) > 50:
            name_error = "Please enter a name between 1 and 50 characters."
        else:
            # Notice: Permanent sessions let Flask remember the name for 30 days.
            session.permanent = True
            session["user_name"] = name
            session["score_history"] = get_user_history(name)
            return redirect(url_for("index"))

    # Notice: A saved name means this is a returning visitor.
    user_name = session.get("user_name")
    if user_name:
        score_history = get_user_history(user_name)
        session["score_history"] = score_history
        return render_template(
            'index.html',
            user_name=user_name,
            score_history=score_history,
            name_error=name_error,
        )

    return render_template(
        'index.html',
        user_name=None,
        score_history=[],
        name_error=name_error,
    )

@app.route('/api/questions', methods=['GET'])
def get_questions():
    # Core Requirement: Retrieve quiz questions through a RESTful API.
    """Serve the question bank and answer choices from server-side JSON storage."""
    try:
        response = jsonify(load_question_bank())
        response.headers["Cache-Control"] = "no-store"
        return response
    except (OSError, json.JSONDecodeError, ValueError) as error:
        return jsonify({"error": "Questions could not be loaded.", "details": str(error)}), 500

@app.route('/api/scores', methods=['GET', 'POST'])
def score_api():
    # Core Requirement: Retrieve and store quiz scores through a RESTful API.
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
    name = data.get("name")

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
        or (name is not None and (not isinstance(name, str) or not name.strip()))
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
        score_history = save_score(
            score_values,
            generation,
            total_questions,
            name.strip() if isinstance(name, str) else None,
        )
    except (OSError, json.JSONDecodeError) as error:
        return jsonify({"error": "Score could not be saved.", "details": str(error)}), 500
    return jsonify(score_history[-1]), 201

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # Notice: Quiz access requires the user to identify themselves first.
    if not session.get("user_name"):
        return redirect(url_for("index"))

    if "quiz_questions" not in session:
        # Notice: Randomize the quiz questions and initialize all quiz state.
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
        session["answer_history"] = []
        session["visible_options"] = random.sample(
            session["quiz_questions"][0]["answers"],
            k=len(session["quiz_questions"][0]["answers"]),
        )
        session["question_deadline"] = time.time() + QUESTION_TIME_LIMIT_SECONDS

    # Individual Requirement: Timer-Based Challenge Mode
    # Notice: The server checks the deadline so it cannot be bypassed with client refreshes.
    if not session.get("answer_feedback"):
        deadline = session.get("question_deadline")
        if deadline is not None and time.time() >= deadline:
            return redirect(url_for("result"))

    fifty_fifty_error = None
    if request.method == 'POST':
        # Notice: A timeout submission ends the quiz immediately.
        if request.form.get("action") == "timeout":
            session.pop("answer_feedback", None)
            return redirect(url_for("result"))

        # Notice: The continue button closes feedback and advances to the next question.
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
            session["question_deadline"] = time.time() + QUESTION_TIME_LIMIT_SECONDS
            return redirect(url_for("quiz"))

        # Individual Requirement: Hint System
        # Notice: Clicking Hint opens generation selection; it does not use or submit an answer.
        if request.form.get("action") == "fifty_fifty":
            if session["fifty_fifty_available"]:
                session["fifty_fifty_selecting"] = True
            return redirect(url_for("quiz"))

        if request.form.get("action") == "remove_generations":
            # Notice: Request exactly two generation positions for removal.
            selected_generations = request.form.getlist("removed_generations")
            try:
                selected_indices = {int(index) for index in selected_generations}
            except ValueError:
                selected_indices = set()

            if (
                len(selected_indices) != 2
                or not selected_indices.issubset(range(len(GENERATIONS)))
            ):
                # Notice: Invalid Hint selections keep the feature active and display an error.
                fifty_fifty_error = "Please select exactly two generations."
            else:
                # Notice: Answer positions correspond to their original generation indexes.
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
            # Notice: Check that the submitted answer is one of the currently visible choices.
            answer = request.form.get("answer")
            current_number = session["question_number"]
            current_question = session["quiz_questions"][current_number]
            if answer not in session["visible_options"]:
                return redirect(url_for("quiz"))

            # Notice: Find the answer's original position before updating the generation score.
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
            # Notice: Store feedback data for the feedback page.
            session["answer_feedback"] = {
                "selected_answer": answer,
                "generation": generation,
                "color": GENERATION_COLORS[generation],
                "comment": selected_comment,
                "question": current_question["question"],
                "question_number": answered_question_number,
                "is_final": current_number == len(session["quiz_questions"]),
            }
            answer_history = session.get("answer_history", [])
            answer_history.append({
                "question_number": answered_question_number,
                "question": current_question["question"],
                "selected_answer": answer,
                "generation": generation,
                "color": GENERATION_COLORS[generation],
                "comment": selected_comment,
            })
            # Individual Requirement: Question Review
            # Notice: Session history is used to revisit answers after the quiz.
            session["answer_history"] = answer_history
            return redirect(url_for("quiz"))

    answer_feedback = session.get("answer_feedback")
    if answer_feedback:
        # Individual Requirement: Progress Bar
        # Notice: The completed question count is converted into a percentage for Jinja.
        completed_questions = answer_feedback["question_number"]
        progress_percent = int(
            (completed_questions / len(session["quiz_questions"])) * 100
        )
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
            completed_questions=completed_questions,
            progress_percent=progress_percent,
        )

    current_number = session["question_number"]
    current_question = session["quiz_questions"][current_number]
    deadline = session.get("question_deadline")
    seconds_left = max(
        0,
        int(deadline - time.time()) if deadline is not None else QUESTION_TIME_LIMIT_SECONDS,
    )
    # Individual Requirement: Progress Bar
    # Notice: This branch calculates progress for the unanswered question currently on screen.
    completed_questions = session["question_number"]
    progress_percent = int(
        (completed_questions / len(session["quiz_questions"])) * 100
    )
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
        seconds_left=seconds_left,
        completed_questions=completed_questions,
        progress_percent=progress_percent,
    )

@app.route('/result')
def result():
    # Notice: The result page is unavailable until at least one scored quiz exists.
    if "scores" not in session:
        return redirect(url_for("index"))

    scores = session["scores"]
    highest_score = max(scores)
    generation = GENERATIONS[scores.index(highest_score)]
    user_name = session.get("user_name")
    if not session.get("result_saved", False):
        try:
            # Notice: Save only once so refreshing the result page does not duplicate history.
            save_score(
                scores,
                generation,
                len(session["quiz_questions"]),
                user_name,
            )
            session["result_saved"] = True
            session["score_history"] = get_user_history(user_name) if user_name else []
        except (OSError, json.JSONDecodeError) as error:
            app.logger.error("Could not save quiz score: %s", error)

    return render_template(
        'result.html',
        scores=zip(GENERATIONS, scores),
        generation=generation,
        total_questions=len(session["quiz_questions"]),
        generation_colors=GENERATION_COLORS,
    )

@app.route('/review')
def review_answers():
    # Individual Requirement: Question Review
    # Notice: Review requires a completed quiz session; otherwise redirect to the welcome page.
    if "scores" not in session:
        return redirect(url_for("index"))

    return render_template(
        'review.html',
        answer_history=session.get("answer_history", []),
    )

@app.route('/start')
def start():
    # Notice: Preserve identity and history while clearing only the active quiz state.
    user_name = session.get("user_name")
    score_history = session.get("score_history", [])
    session.clear()
    if user_name:
        session["user_name"] = user_name
        session["score_history"] = score_history
        session.permanent = True
    return redirect(url_for("quiz"))

def main():
    # Notice: Start Flask's built-in development server when this file is run directly.
    app.run(debug=True)

if __name__ == '__main__':
    main()