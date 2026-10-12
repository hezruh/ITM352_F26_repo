#interactive quiz system, version2
#make a list with the questions and correct answers

questions = [
    {"question": "what is the capital of france?", "answer": "Paris"},
    {"question": "what is the capital of germany?", "answer": "Berlin"},
    {"question": "what is the capital of italy?", "answer": "Rome"}
]

for question, correctAnswer in questions:
    answer = input(f"{questions} ")
    if answer == correctAnswer:
        print("correct")
    else:
        print(f"the answer is '{correctAnswer}', not {answer!r}")