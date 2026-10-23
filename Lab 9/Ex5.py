# save the dictionary to a json file
import json

questions = {
    "what is the capital of france?": ["Paris", "Toulouse", "Nice", "Avignon"],
    "what is the capital of germany?": ["Berlin", "Hamburg", "Munich", "Cologne"],
    "which artist painted the last supper?": ["da Vinci", "Michaelangelo", "Raphael", "Donatello"],
    "what is the airspeed of an unladen swallow?": ["24", "12", "48", "36"],
    "Who wrote the play 'Romeo and Juliet'?": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
}

filename = "quizQuestions.json"

with open(filename, "w") as file:
    json.dump(questions, file, indent=4)


print(f"Questions saved to {filename}.")