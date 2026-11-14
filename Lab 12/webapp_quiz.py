# application to manage the quiz webapp
# name: Hezra Calventas
# Date: November 13, 2026

import json
import random
from pathlib import Path

from flask import Flask, redirect, render_template, request, session, url_for

BASE_DIR = Path(__file__).resolve().parents[2]
QUESTION_FILE = BASE_DIR / "Assignment 1" / "questions.json"
NUM_QUESTIONS_PER_QUIZ = 5
GENERATIONS = ["Millennial", "Zoomer", "Gen Alpha", "Baby Boomer"]

with QUESTION_FILE.open(encoding="utf-8") as file:
    QUESTION_BANK = json.load(file)

app = Flask(__name__, template_folder=str(Path(__file__).resolve().parent))
app.secret_key = "quiz-app-development-key"

@app.route('/')
def index():
    return render_template('index.html')

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
        session["visible_options"] = session["quiz_questions"][0]["answers"]

    if request.method == 'POST':
        if request.form.get("action") == "fifty_fifty":
            if session["fifty_fifty_available"]:
                session["visible_options"] = random.sample(
                    session["visible_options"], k=2
                )
                session["fifty_fifty_available"] = False
            return redirect(url_for("quiz"))

        answer = request.form.get("answer")
        current_number = session["question_number"]
        current_question = session["quiz_questions"][current_number]
        if answer not in session["visible_options"]:
            return redirect(url_for("quiz"))

        answer_position = current_question["answers"].index(answer)
        scores = session["scores"]
        scores[answer_position] += 1
        session["scores"] = scores
        current_number += 1
        session["question_number"] = current_number

        if current_number == len(session["quiz_questions"]):
            return redirect(url_for("result"))

        session["visible_options"] = session["quiz_questions"][current_number]["answers"]

    current_number = session["question_number"]
    current_question = session["quiz_questions"][current_number]
    return render_template(
        'quiz.html',
        question=current_question["question"],
        question_number=current_number + 1,
        total_questions=len(session["quiz_questions"]),
        options=session["visible_options"],
        fifty_fifty_available=session["fifty_fifty_available"],
    )

@app.route('/result')
def result():
    if "scores" not in session:
        return redirect(url_for("index"))

    scores = session["scores"]
    highest_score = max(scores)
    generation = GENERATIONS[scores.index(highest_score)]
    with (BASE_DIR / "Assignment 1" / "scoreHistory.txt").open("a", encoding="utf-8") as file:
        file.write(f"\nYou are most likely a {generation}.")

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