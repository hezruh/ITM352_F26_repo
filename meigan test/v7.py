#interactive quiz system, version7
#make a dictionary with the questions and correct answers
#allow user to choose the option by its label
#improve usablility and look. keep track of correct answers
#randomize the order of the questions and the order of the answers
#refactor code to use functions

from string import ascii_lowercase
import random
import json

#load the questions from a json file
questionFile = open("questions.json", "r")
questions = json.load(questionFile)

NUM_QUESTIONS_PER_QUIZ = 5

#randomizes the order of the questions and selects only 5
def prepareQuestions(questions, numQuestions):
    numQuestions  = min(numQuestions, len(questions))
    return random.sample(list(questions.items()), k = numQuestions)

#labels the answers with letters. allows for user to select answer as lower or upper case.
#prints invalid choice if user selects an invalid option.
def getAnswer(question, alternatives):
    labeledAnswers = dict(zip(ascii_lowercase, alternatives))

    for label, answer in labeledAnswers.items():
        print(f"{label}. {answer}")

    while (answerLabel := input("choice? ").lower()) not in labeledAnswers:
        print(f"invalid choice. please select one of {', '.join(labeledAnswers.keys())}.")

    answer = labeledAnswers.get(answerLabel)
    return labeledAnswers[answerLabel]

#randomizes order of answers from choices dictionary and prints the explanations for the correct answers. 
def askQuestion(questionData):
    choices = questionData["choices"]
    correctAnswer = choices[0] 
    orderedAlternatives = random.sample(choices, k = len(choices)) 
    answer = getAnswer("", orderedAlternatives)
    if answer == correctAnswer:
        print(questionData["explanation"])
        return 1
    else:
        print(f"the answer is '{correctAnswer}', not {answer!r}")
        return 0
    
questions =  prepareQuestions(questions, NUM_QUESTIONS_PER_QUIZ)

numCorrect = 0

#prints the question and keeps track of correct answers.
for num, (question, questionData) in enumerate(questions, start = 1):
    print(f"\nQuestion {num}: {question}")
    numCorrect += askQuestion(questionData)

#print total correct answers
print(f"\nYou got {numCorrect} correct.")

#reads high score from file and compares to current score. replaces high score if higher and in the file.
highScoreFile = open("highScore.txt", "r")
highScore = int(highScoreFile.read())

if numCorrect > highScore:
    highScore = numCorrect

    highScoreFile = open("highScore.txt", "w")
    highScoreFile.write(str(highScore))

    print(f"New high score: {highScore}!")