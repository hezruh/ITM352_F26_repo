Lab: Creating HTML Interfaces with Flask 

1.  Install Flask and create a first simple application. 

Run Flask in debug mode. This means you will access your local server at 127.0.0.1
Create a single route for “/”.
Respond to a request for this route by outputting “Welcome to {your name}’s web site!”

# Create a simple HTML Flask application that displays a welcome message
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return ("Welcome to Kazman's really boring web page")

if __name__ == '__main__':
    app.run(debug=True)

2. When creating HTML pages in the Flask framework, they need to be put in a “templates” subdirectory.
Create an index.html page that allows a user to select a link that takes them to a login page.
Create a login.html page--a simple form with a text field for a username, a password field for a password, and a submit button. Create a route for /login. The function for login should present the form.
When this form is submitted, process the data and take the user to a success page. You can hard-code a dictionary of userIDs and passwords such as:

USERS = {"port": "port123",
        	  "kazman": "kazman123"}

# Interactive quiz system, sixth version
# Make a dictionary with the questions and different answers
# Allow the user to choose the option by its label
# Improve the look and usability. Keep track of different answers and which generation they correspond to.
# Randomize the order of the questions and the order of the answers for each question.
# Refactor the code to use functions.
# Author: Hezra Calventas
# Date: October 7, 2026

from string import ascii_lowercase
import random
import json

question_file = open("questions.json", "r")
questions = json.load(question_file)


NUM_QUESTIONS_PER_QUIZ = 5
ScoreMillennial = 0
ScoreGenZ = 0
ScoreGenAlpha = 0
ScoreBabyBoomer = 0


def prepare_questions(questions, num_questions):
    num_questions = min(num_questions, len(questions))
    return random.sample(list(questions.items()), k=num_questions)


def get_answer(question, alternatives, fiftyFiftyAvailable):
    fiftyFiftyUsed = False
    labeled_answers = dict(zip(ascii_lowercase, alternatives))
    fiftyFiftyLabel = None
    if fiftyFiftyAvailable and len(alternatives) == 4:
        fiftyFiftyLabel = ascii_lowercase[len(labeled_answers)]
        labeled_answers[fiftyFiftyLabel] = "Use my 50/50"

    for label, answer in labeled_answers.items():
        print(f"{label}. {answer}")

    while True:
        answer_label = input("Choice? ").lower()
        if answer_label not in labeled_answers:
            print(f"Invalid choice. Please select one of {', '.join(labeled_answers.keys())}.")
            continue

        if answer_label == fiftyFiftyLabel:
            alternatives = random.sample(alternatives, k=2)
            labeled_answers = dict(zip(ascii_lowercase, alternatives))
            fiftyFiftyUsed = True
            print("You used up your 50/50, and now there are only two choices left.")
            for label, answer in labeled_answers.items():
                print(f"{label}. {answer}")
            continue

        return labeled_answers[answer_label], fiftyFiftyUsed


def ask_question(question, alternatives, fiftyFiftyAvailable):    
    ordered_alternatives = random.sample(alternatives, k=len(alternatives))
    answer, fiftyFiftyUsed = get_answer(question, ordered_alternatives, fiftyFiftyAvailable)
    answer_position = alternatives.index(answer)
    return answer_position, fiftyFiftyUsed


# Main program logic starts here
questions = prepare_questions(questions, NUM_QUESTIONS_PER_QUIZ)

# Main Loop
print("\nWelcome to my quiz!\nBased on your answers, I will determine which generation you most likely belong to.\n")
fiftyFiftyAvailable = True
for num, (question, answers) in enumerate(questions, start=1):
    print(f"\nQuestion {num}: {question}")
    print("Alternatively, you can use your one-time 50/50 option to remove two answers.")
    answer_position, fiftyFiftyUsed = ask_question(
        question, answers, fiftyFiftyAvailable
    )
    if fiftyFiftyUsed:
        fiftyFiftyAvailable = False
    if answer_position == 0:
        ScoreMillennial += 1
    elif answer_position == 1:
        ScoreGenZ += 1
    elif answer_position == 2:
        ScoreGenAlpha += 1
    elif answer_position == 3:
        ScoreBabyBoomer += 1

for score, generation in zip([ScoreMillennial, ScoreGenZ, ScoreGenAlpha, ScoreBabyBoomer], ["Millennial", "Zoomer", "Gen Alpha", "Baby Boomer"]):
    if score == 0:
        continue
    elif (score == 1):
        print(f"You answered {score} question the way a {generation} would answer.")
    else:
        print(f"You answered {score} questions the way a {generation} would answer.")


print(f"\nBased on how you responded, you are most likely a {['Millennial', 'Zoomer', 'Gen Alpha', 'Baby Boomer'][[ScoreMillennial, ScoreGenZ, ScoreGenAlpha, ScoreBabyBoomer].index(max([ScoreMillennial, ScoreGenZ, ScoreGenAlpha, ScoreBabyBoomer]))]}.")
with open("scoreHistory.txt", "a") as file:
    file.write("\nYou are most likely a " + ['Millennial', 'Zoomer', 'Gen Alpha', 'Baby Boomer'][[ScoreMillennial, ScoreGenZ, ScoreGenAlpha, ScoreBabyBoomer].index(max([ScoreMillennial, ScoreGenZ, ScoreGenAlpha, ScoreBabyBoomer]))] + ".")

ON YOUR OWN: 3. Create a simple Flask application to retrieve memes from https://meme-api.com/gimme/wholesomememes.  To get the memes you will need to issue a requests.request("GET", url) command.

Present the meme and the meme source (subreddit) to the user. Refresh the meme every 10 seconds.  You can accomplish this by including the following <meta> tags in the <head> of your HTML page.
<head>
   <title>Memes'R'Us</title>
   <meta charset="UTF-8" name="viewport" content="width=device-width, initial-scale=0.8">
   <meta http-equiv="refresh" content="10; url=http://127.0.0.1:5000" />
</head>

import requests
from flask import Flask, render_template

app = Flask(__name__)

MEME_API_URL = "https://meme-api.com/gimme/wholesomememes"


def get_meme():
    response = requests.request("GET", MEME_API_URL, timeout=10)
    response.raise_for_status()
    meme = response.json()

    if not meme.get("url") or not meme.get("subreddit"):
        raise ValueError("The meme API returned incomplete meme data.")

    return meme


@app.route("/")
def memes():
    try:
        meme = get_meme()
    except (requests.RequestException, ValueError) as error:
        return render_template("memes.html", error=str(error)), 502

    return render_template(
        "memes.html",
        meme_url=meme["url"],
        subreddit=meme["subreddit"],
        error=None,
    )


@app.route("/home")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)


ON YOUR OWN: 4. Create a “skeleton” of your quiz game using Flask. There are several approaches to this:
i.  Create “mock up” pages for your quiz game and modify Ex 2 above to navigate to all these pages (e.g. index.html links to “take the quiz” page). 
ii. Another approach  is to ask AI “create a skeleton for a Flask application for a quiz game” and adapt this to your vision of the game. 
iii. Another approach is to give AI your quiz.py from Assignment 1 and prompt “create a Flask application for this quiz game <add your quiz.py code here>”

https://github.com/hezruh/ITM352_F26_repo/blob/2f7e9a0ee44ac54e5f6e0f02a132b231e1b1f226/Assignment%203/templates/webapp_quiz.py

What are the benefits and disadvantages of using a skeleton? 
Discuss the pros and cons of the approach you used (i,ii,iii) and ultimately if it was better than creating the initial quiz game web application from scratch.

The benefits of using a skeleton are comparable to writing your entire program in pseudocode then translating it all into your desired language. By having a skeleton first, all you need to focus on is converting it to an HTML website using flask, as opposed to having to do it all from scratch (the metaphor, not the coding website). The disadvantages are that you technically have to do it twice, so if you're short on time it would be longer than doing it all at once. I used method iii, as it was the most straightforward and worked the best for me. If I wanted more practice, I should have done i, but I don't think I would have been able to finish the lab on time.