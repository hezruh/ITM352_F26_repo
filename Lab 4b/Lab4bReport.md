Lab Part b - More practice with Strings


1. Go to w3schools.com and look up “String Methods”.  Find a method that you think is interesting.  Describe the method and describe something interesting and useful that you could do with it in a program.
    swapcase() - it swaps the case of each character in a string. An example of where this could be useful is if you are trying to create a program that takes user input and formats it in a specific way, such as making all letters uppercase or lowercase.


2. Use the input() function to get a name from the user and put it into title case.

Code here:
# Properly format an inputted name in title case

rawName = input("Enter your name: \n")
strippedName = rawName.strip()
titleCaseName = strippedName.title()
print("Formatted name:", titleCaseName)

Explain when/where you might use this functionality.
If you want all of your records to be uniformly formatted in a way that is easy to read such as in a database or a contact list, you would want to format names in title case. This ensures that names are consistently presented, regardless of how the user inputs them.


3. Use the input() function to get a URL from the user (the entire URL, e.g. https://shidler.hawaii.edu/).  Parse the string to get just the domain name and just the TLD (top-level domain) and print these.  

Code here:
# Get a URL from the user, clean it, and extract the domain name and TLD
# Name: Hezra Calventas
# Date: September 18, 2026

url = input("Enter a URL: \n")
cleanedUrl = url.replace("https://", "")
cleanedUrl = cleanedUrl.replace("/","")
print("Cleaned URL:", cleanedUrl)

parts = cleanedUrl.split(".")
print("The parts are: ", parts)

domainName = parts[1]
tld = parts[2]
print("Domain name:", domainName)
print("TLD:", tld)


Why might you want to parse a URL in this way?
If you are asking for a link to a website, you may want to parse the URL to extract the domain name and TLD for validation purposes.

4. Similar to exercise 3, use the input() function to get an email address from the user.  


Parse the string using split() to get just the username and just the domain and print these.  Code here:
# Parse through portions of email address, print out username and domain name
# Name: Hezra Calventas
# Date: September 18, 2026

emailAddress = input("Enter an email address: \n")
parts = emailAddress.split("@")
username = parts[0]

print("Parts of the email address:", parts)
print("Username:", username)

domainName = parts[1]
print("Domain name:", domainName)



Now do the same thing using index() and slicing.  Code here:
atSignIndex = emailAddress.index("@")
username2 = emailAddress[:atSignIndex]
domainName2 = emailAddress[atSignIndex + 1:]

print("Username (method 2):", username2)
print("Domain name (method 2):", domainName2)

5. Ask for a sentence from the user (using input()).  Turn the sentence into a list of strings. Reverse the list.  Join the reversed list back into a string.

Code here:
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