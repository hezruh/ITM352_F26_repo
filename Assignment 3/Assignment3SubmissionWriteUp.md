1. Link to your Assignment 3 folder in your GitHub repo:

 

2. Individual requirements implemented:

 

3. (OPTIONAL) Extra credit implemented: 

 

4. Where is your evidence or documentation of testing:

I placed the application test code in [ExerciseAPI_test.py](/Users/sciskafu/Documents/GitHub/ITM352_F26_repo/Assignment%203/ExerciseAPI_test.py). The test suite uses Flask's built-in test client and temporary JSON storage, so the tests do not overwrite the application's real score history.

The test file verifies first-time and returning-user behavior, JSON question and score APIs, score validation, randomized answer selection, the Hint feature, the 15-second timer, feedback and progress-bar values, generation-specific result colors, and review navigation. It can be run from the Assignment 3 folder with:

```bash
python3 ExerciseAPI_test.py
```

The test suite currently passes 13 tests.

5. How I used AI on this assignment:

I used GitHub Copilot as a coding and explanation assistant throughout this assignment. I had asked Copilot to help move the generation comments from the Python file into a separate JSON file, implement persistent user identification and history, and explain how Flask sessions and the JSON score file work. I also used Copilot to help implement the 15-second per-question timer, the Hint feature, randomized answer order, the feedback page, the progress bar, and the answer-review page.

For the timer, I requested a countdown that must use a server-side deadline as well as the browser display. For the Hint feature, I explained that it should act like a one-use option while allowing the user to remove two selected generations instead of removing random answers. For the score and question requirement, I asked for REST-style Flask routes that read from JSON and validate submitted data before saving it.

I also used Copilot to help create the test file and explain how each test uses Flask's test client and temporary JSON storage. I used Copilot to add comments to the program in a style similar to the comments in my previous assignment. I reviewed and adjusted the generated code rather than copying it without understanding it.