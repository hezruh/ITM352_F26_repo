isIt = "hello"
isItCheck = ""
print(isIt)

def is_palindrome(isIt, isItCheck):
    for letters in range(len(isIt), 0, -1):
        if (isIt[letters - 1] != isIt[len(isIt) - letters]):
            return False
        else:
            return True

print(is_palindrome(isIt, isItCheck))
print(isItCheck)