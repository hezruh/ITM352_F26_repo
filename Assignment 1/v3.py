#interactive quiz system, version
#make a dictionary with the questions and correct answers

questions = {
    "what is the capital of france?": ["Paris", "Toulouse", "Nice", "Avignon"],
    "what is the capital of germany?": ["Berlin", "Hamburg", "Munich", "Cologne"],
    "which artist painted the last supper?": ["da Vinci", "Michaelangelo", "Raphael", "Donatello"]
}

for question, answers in questions.items():
    correctAnswer = answers[0]
    for answer in answers:
        print(f"  {answer}")
    answer = input(f"{question} ")
    if answer == correctAnswer:
        print("correct")
    else:
        print(f"the answer is '{correctAnswer}', not {answer!r}")