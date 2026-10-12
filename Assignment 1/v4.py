#interactive quiz system, version 4
#make a dictionary with the questions and correct answers
#allow user to choose option by its label

questions = {
    "what is the capital of france?": ["Paris", "Toulouse", "Nice", "Avignon"],
    "what is the capital of germany?": ["Berlin", "Hamburg", "Munich", "Cologne"],
    "which artist painted the last supper?": ["da Vinci", "Michaelangelo", "Raphael", "Donatello"]
}

for question, answers in questions.items():
    correctAnswer = answers[0]
    sortedAnswers = sorted(answers)
    for label, answer in enumerate(sortedAnswers, start=1):
        print(f"  {label}. {answer}")
    answerLabel = int(input(f"{question} "))
    answer = sortedAnswers[answerLabel - 1]
    if answer == correctAnswer:
        print("correct")
    else:
        print(f"the answer is '{correctAnswer}', not {answer!r}")