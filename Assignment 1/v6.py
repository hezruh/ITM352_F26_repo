#interactive quiz system, version 4
#make a dictionary with the questions and correct answers
#allow user to choose option by its label
#improve the look and usability. keep track of correct answers

from string import ascii_lowercase
import random

questions = {
    "what is the capital of france?": ["Paris", "Toulouse", "Nice", "Avignon"],
    "what is the capital of germany?": ["Berlin", "Hamburg", "Munich", "Cologne"],
    "which artist painted the last supper?": ["da Vinci", "Michaelangelo", "Raphael", "Donatello"],
    "what is the airspeed of an unladen swallow?": ["24", "12", "48", "36"],
}

numQuestionsPerQuiz = 5
numQuestions = min(numQuestionsPerQuiz, len(questions))
selectedQuestions = random.sample(list(questions.items()), k=numQuestions)

numCorrect = 0

for num, (question, answers) in enumerate(questions.items(), start=1):
    correctAnswer = answers[0]
    print(f"\nQuestion {num}: {question}")

    sortedAnswers = sorted(answers)
    labeledAnswers = dict(zip(ascii_lowercase, random.sample(sortedAnswers, k=len(sortedAnswers))))

    for label, answer in labeledAnswers.items():
        print(f"  {label}. {answer}")

    while (answerLabel := input("choice? ").lower()) not in labeledAnswers:
        print(f"Invalid choice. Please select from {', '.join(labeledAnswers.keys())}.")
    answer = labeledAnswers.get(answerLabel)

    if answer == correctAnswer:
        print("correct")
        numCorrect += 1
    else:
        print(f"the answer is '{correctAnswer}', not {answer!r}")

print(f"\nYou got {numCorrect} out of {len(questions)} correct.")