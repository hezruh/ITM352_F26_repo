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