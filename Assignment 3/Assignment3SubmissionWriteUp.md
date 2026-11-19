1. Link to your Assignment 3 folder in your GitHub repo:
    https://github.com/hezruh/ITM352_F26_repo/tree/17288142ce183e11deb0af41b7daba4ee885564f/Assignment%203
 

2. Individual requirements implemented:
    Persistent User Identification and History
        Use cookies or sessions to check if a user has already visited the quiz game. If so, welcome them back and show them their score history. If it’s their first visit, ask them for their name and save it in a cookie/session which will be used to identify them in subsequent visits. Use sessions and cookies to track the user’s quiz score history.

    Interactive Visual Feedback
        Implement animations or visual effects for correct and incorrect answers. For example, correct answers could turn green, while incorrect answers turn red with an explanation.
 

3. (OPTIONAL) Extra credit implemented: 
    Timer-Based Challenge Mode
        Include a timed quiz mode where each question must be answered within a certain time. Display a countdown timer and end the quiz if the timer reaches zero.
 
    Hint System
        Add a hint system where users can request a hint on a question (for mine, I just let them pick two generations and remove the answers corresponding to the ones they selected). For balance, deduct points when hints are used, or limit hints to one per quiz.

    Progress Bar
        Include a progress bar to visually represent quiz completion status. The bar should fill as the user answers each question.
    
    Question Review and Explanation
        After each question, show a brief explanation of the correct answer (or in my case, an explanation of which generation corresponds to their answer). At the end, provide a review screen for users to revisit questions they missed with explanations.

4. Where is your evidence or documentation of testing:
    https://github.com/hezruh/ITM352_F26_repo/blob/17288142ce183e11deb0af41b7daba4ee885564f/Assignment%203/quiz_scores.json



5. How I used AI on this assignment:

    I used GitHub Copilot as a coding and explanation assistant throughout this assignment. I had asked Copilot to help move the generation comments from the Python file into a separate JSON file, implement persistent user identification and history, and explain how Flask sessions and the JSON score file work. I also used Copilot to help implement the 15-second per-question timer, the Hint feature, randomized answer order, the feedback page, the progress bar, and the answer-review page.

    For the timer, I requested a countdown that must use a server-side deadline as well as the browser display. For the Hint feature, I explained that it should act like a one-use option while allowing the user to remove two selected generations instead of removing random answers. For the score and question requirement, I asked for REST-style Flask routes that read from JSON and validate submitted data before saving it.

    I also used Copilot to help create the test file and explain how each test uses Flask's test client and temporary JSON storage. I used Copilot to add comments to the program in a style similar to the comments in my previous assignment. I reviewed and adjusted the generated code rather than copying it without understanding it.