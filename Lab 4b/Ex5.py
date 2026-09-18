# Ask the user for a sentence (using input())
# turn the sentence into a list of strings (using split())
# reverse the list
# join the list back into a string (using join())
# Name: Hezra Calventas
# Date: September 18, 2026

sentence = input("Enter a sentence: \n")
words = sentence.split()
words.reverse()
reversedSentence = " ".join(words)
print("Reversed sentence:\n", reversedSentence)

joinedSentence = sentence + " " + reversedSentence
print("Joined sentence:\n", joinedSentence)