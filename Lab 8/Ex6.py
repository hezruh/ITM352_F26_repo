userNum = int(input("enter a number: "))
searchMe  = [ 2, 5, 7, 11, 15, 22, 27, 30, 34, 41, 55, 57, 58, 60, 77]

def numSearch(userNum, searchme):
    for i in range(len(searchMe)):
        if searchMe[i] == userNum:
            return True
    return False

print(numSearch(userNum, searchMe))