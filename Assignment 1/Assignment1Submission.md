1. Link to your Assignment 1 folder in your GitHub repo:

https://github.com/hezruh/ITM352_F26_repo/tree/d93ea2cd46af7d40673cf165af60a2755c16dcba/Assignment%201



2. Individual requirements implemented (and which requirements you may have implemented for extra credit):

&nbsp; &nbsp; 1. Write the history of scores out to a file.&nbsp; [You may use File I/O]

&nbsp; &nbsp; 10. Add a 50/50 feature (eliminating 2 of the 4 answers, wrong ones that is) that can only be used once per game instance.



3. Where is your evidence or documentation of testing:

sciskafu@Hezras-MacBook-Air-3 ITM352_F26_repo % &nbsp;source /Users/sciskafu/Documents/GitHub/ITM352_F26_repo/.venv/bin/activate
(.venv) sciskafu@Hezras-MacBook-Air-3 ITM352_F26_repo % /Users/sciskafu/Documents/GitHub/ITM352_F26_repo/.venv/bin/python "/Users/sciskafu/Documents/G
itHub/ITM352_F26_repo/Assignment 1/Assignment1Final.py"
Traceback (most recent call last):
&nbsp; File "/Users/sciskafu/Documents/GitHub/ITM352_F26_repo/Assignment 1/Assignment1Final.py", line 14, in <module>
&nbsp; &nbsp; question_file = open("questions.json", "r")
FileNotFoundError: [Errno 2] No such file or directory: 'questions.json'
(.venv) sciskafu@Hezras-MacBook-Air-3 ITM352_F26_repo % cd "Assignment 1"
(.venv) sciskafu@Hezras-MacBook-Air-3 Assignment 1 % /Users/sciskafu/Documents/GitHub/ITM352_F26_repo/.venv/bin/python "/Users/sciskafu/Documents/GitH
ub/ITM352_F26_repo/Assignment 1/Assignment1Final.py"

Welcome to my quiz!
Based on your answers, I will determine which generation you most likely belong to.


Question 1: Which is Your Most Used Social Media Platform?
Alternatively, you can use your one-time 50/50 option to remove two answers.
a. Tumblr
b. Facebook
c. Instagram
d. TikTok
e. Use my 50/50
Choice? l
Invalid choice. Please select one of a, b, c, d, e.
Choice? a

Question 2: When you want to wind down, which game do you pick up?
Alternatively, you can use your one-time 50/50 option to remove two answers.
a. Minecraft
b. Solitaire
c. The Legenend of Zelda: Ocaria of Time
d. Roblox
e. Use my 50/50
Choice? b

Question 3: Pick a Celebrity
Alternatively, you can use your one-time 50/50 option to remove two answers.
a. Elvis Presley
b. Lindsay Lohan
c. MrBeast
d. Zac Effron
e. Use my 50/50
Choice? c

Question 4: Which is your Most Listened to Song?
Alternatively, you can use your one-time 50/50 option to remove two answers.
a. Look at Me - XXXTentacion
b. Hey Jude - The Beatles
c. Baby Shark - Pinkfong
d. We Are Young - Fun.
e. Use my 50/50
Choice? d

Question 5: Which Movie Makes You Feel Nostalgia for Your Childhood?
Alternatively, you can use your one-time 50/50 option to remove two answers.
a. Avengers: Endgame
b. Rebel Without a Cause
c. Shark Boy and Lava Girl
d. Toy Story
e. Use my 50/50
Choice? e
You used up your 50/50, and now there are only two choices left.
a. Shark Boy and Lava Girl
b. Avengers: Endgame
Choice? a
You answered 2 questions the way a Millennial would answer.
You answered 1 question the way a Zoomer would answer.
You answered 1 question the way a Gen Alpha would answer.
You answered 1 question the way a Baby Boomer would answer.

Based on how you responded, you are most likely a Millennial.
(.venv) sciskafu@Hezras-MacBook-Air-3 Assignment 1 % /Users/sciskafu/Documents/GitHub/ITM352_F26_repo/.venv/bin/python "/Users/sciskafu/Documents/GitH
ub/ITM352_F26_repo/Assignment 1/Assignment1Final.py"

Welcome to my quiz!
Based on your answers, I will determine which generation you most likely belong to.


Question 1: Pick a Celebrity
Alternatively, you can use your one-time 50/50 option to remove two answers.
a. Lindsay Lohan
b. MrBeast
c. Zac Effron
d. Elvis Presley
e. Use my 50/50
Choice? 1
Invalid choice. Please select one of a, b, c, d, e.
Choice? ab
Invalid choice. Please select one of a, b, c, d, e.
Choice? \n
Invalid choice. Please select one of a, b, c, d, e.
Choice? a

Question 2: What is your go-to treat for yourself?
Alternatively, you can use your one-time 50/50 option to remove two answers.
a. ice cream
b. whatever's trending on TikTok right now.
c. boba tea
d. gluten-free, dairy-free frozen yogurt
e. Use my 50/50
Choice? a

Question 3: Which is your Most Listened to Song?
Alternatively, you can use your one-time 50/50 option to remove two answers.
a. We Are Young - Fun.
b. Baby Shark - Pinkfong
c. Look at Me - XXXTentacion
d. Hey Jude - The Beatles
e. Use my 50/50
Choice? a

Question 4: Which is your favorite novel?
Alternatively, you can use your one-time 50/50 option to remove two answers.
a. The Official Skibidi Toilet Survival Guide
b. Today's newspaper
c. Harry Potter and the Philosopher's/Sorcerer's Stone
d. Five Nights at Freddy's: The Silver Eyes
e. Use my 50/50
Choice? a

Question 5: Which Movie Makes You Feel Nostalgia for Your Childhood?
Alternatively, you can use your one-time 50/50 option to remove two answers.
a. Rebel Without a Cause
b. Avengers: Endgame
c. Toy Story
d. Shark Boy and Lava Girl
e. Use my 50/50
Choice? a
You answered 2 questions the way a Millennial would answer.
You answered 1 question the way a Gen Alpha would answer.
You answered 2 questions the way a Baby Boomer would answer.

Based on how you responded, you are most likely a Millennial.
(.venv) sciskafu@Hezras-MacBook-Air-3 Assignment 1 %&nbsp;



4. How I used AI on this assignment:

To be completely honest, I used AI to help with the comparison of the user's input to their results. Specifically, I had asked Copilot to help me with the formatting of line 98, which functionally checks the generation that the user had earned the most points in, before printing out the name of the generation. After going back and forth trying to figure it out by myself, trying to use zip() and a for loop just as I had used in line 91, I had reached a point of intense frustration and asked for help from Copilot. It should be known, however, that even with the solution provided by Copilot, I have yet to find a way to print a message stating that a tie had occurred between two or more generations. Also, I had somewhat utilized Copilot to assist me with learning about how to implement File I/O in lines 99 and 100; I was unsure if we had covered how to implement File I/O in class, as I was sick from a heat stroke at the time. Regardless, I had headed to the File I/O module in the course website and followed the Part 1: File Basics tutorial instructions provided at https://uhm-itm.github.io/ITM352/morea/090-fileio/reading-fileio.html. Based upon the instructions of asking Copilot "How do I read and write files in python? Show me the basics of opening files, reading content, and properly closing files" (my exact prompt), I was able to learn the implementation of File I/O for usage in FileIOTutorial.py, then from there I was able to implement it into my Assignment1Final.py file.</module>