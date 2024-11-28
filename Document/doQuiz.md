### `doQuiz` Sub-package
---
#### `quizsession` Module 
This module is responsible for managing the whole quiz session, including starting a quiz, submitting answers, calculating scores and ending the quiz.<br>
**Attributes**
- `score`: The current score of the quiz session.
- `questions`: A list to store questions for this quiz.
- `current_question_index`: Index of the current question to be answered.
- `wrong_answers`: A list to store the incorrect questions, user's answers and the correct answers.

**Methods**
1. `__init__()`: Initialize a new instance of the class with basic attributes.

2. `start_quiz(questions)`: Start a new quiz session and reset the state of quiz. The questions used for the quiz are generated from question manager.
   *Parameters*:<br>
   `questions`: A list of questions selected for this quiz.
   
3. `submit_answer(answer)`: Submit the user's answer for the current question and checks if the user's answer is correct. 
   If correct, add one score, otherwise add the question with the user's answer to `wrong_answers`. After these, add `current_question_index` by one moving to next question.<br>
   *Parameters*:<br>
   `answer`: The answer given by the user.

4. `end_quiz()`: End the quiz and return the total score achieved duiring the session.

5. `get_wrong_answers()`: Check whether users get the full scores. 
   If so, sent them congratulation message, otherwise show them the details of questions they answerd wrong.
---
#### `timer` Module
This module is designed to manage time tracking during the quiz session. It allows us to start a timer, check the remaining time for quiz and end the timer.<br>
**Attributes**
- `start_time`: The timestamp when the timer is started.
- `duration`: Users need to complete the exam within that time.

**Methods**
1. `__init__()`: Initialize a new instance of the class with basic attributes.
2. `start_timer(duration)`: Record the current time as start time and set duration for the timer.<br>
   *Parameters*: 
   `duration`: Total time for the timer.

3. `check_time_remaining()`: Calculate the elapsed time since started and return the remaining time by subtracting it from the duration. Returns 0 if the timer has expired.

4. `end_timer()`: End the timer and reset the start time.