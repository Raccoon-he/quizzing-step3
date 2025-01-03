# `quizzing` Package
### Author: Huan He, Qijia Zheng

The quizzing Package is about creating, managing, and conducting interactive quizzes for users, divided into two sub-packages: question_bank and doquiz.
[![Build Status](https://app.travis-ci.com/Raccoon-he/quizzing-step3.svg?token=5JNBS28ypyizgLzVxcpv&branch=main)](https://app.travis-ci.com/Raccoon-he/quizzing-step3)

Pypi Link: https://pypi.org/project/quizzing/0.0.1/
Download: pip install quizzing==0.0.1


### `question_bank` Sub-package
---
#### `question_loader` Module 
This module is responsible for loading, classifying, and analyzing quiz questions. It provides utilities to organize questions and perform statistical analysis on them. **This module uses inheritance.**

**Methods**
1. `load_questions_from_file(filepath)`: Load questions from a JSON or CSV file and return them as a list of dictionaries.<br>
   *Parameters*:  
   `filepath`: The file path of the JSON or CSV file containing questions.

2. `classify_questionsby_by_category(questions)`: Classify questions by category and calculate questions numbers.
   Returns a dictionary with:
   - `classification`: Questions grouped by their categories.
   - `stats`: A count of questions per category.  
   *Parameters*:  
   `questions`: A list of question dictionaries.

3. `classify_questionsby_by_difficulty(questions)`: Classify questions by difficulty and calculate questions numbers. 
   Returns a dictionary with:
   - `classification`: Questions grouped by their difficulties.
   - `stats`: A count of questions per difficulty.  
   *Parameters*:  
   `questions`: A list of question dictionaries.

4. `get_random_questions(category, difficulty, number)`: Retrieve a specified number of random questions from the given category and difficulty.  
   *Parameters*:  
   `questions`: A list of available questions.  
   `category`: The category to filter questions by.  
   `difficulty`: The difficulty to filter questions by.
   `number`: The number of questions to retrieve.

---
#### `question_manager` Module
This module is responsible for managing the question bank, including adding, removing, and updating questions.

**Methods**
1. `add_question(question)`: Add a new question to the question bank.  
   *Parameters*:  
   `question`: A dictionary representing the question to add.

2. `remove_question(question_id)`: Remove a question from the question bank by its unique identifier.  
   *Parameters*:  
   `question_id`: The ID of the question to be removed.

3. `update_question(question_id, updated_data)`: Update the details of an existing question, such as its text or answer options.  
   *Parameters*:  
   `question_id`: The ID of the question to update.  
   `updated_data`: A dictionary containing the updated question information.

4. `get_question_by_id(question_id)`: Retrieve a specific question from the question bank by its unique identifier.
    *Parameters*:
    `question_id`: The ID of the question to retrieve.
    *Returns*: The question matching the ID or None if not found.

5. `list_all_questions()`: List all the questions currently stored in the question bank.
    *Returns*: A list of all available questions.

### `do_quiz` Sub-package
---
#### `quiz_session` Module 
This module is responsible for managing the whole quiz session, including starting a quiz, submitting answers, calculating scores and ending the quiz.<br>
**Attributes**
- `score`: The current score of the quiz session.
- `questions`: A list to store questions for this quiz.
- `current_question_index`: Index of the current question to be answered.
- `wrong_answers`: A list to store the incorrect questions, user's answers and the correct answers.

**Methods**
1. `__init__()`: Initialize a new instance of the class with basic attributes.

2. `start_quiz(questions)`: Start a new quiz session and reset the state of quiz. The questions used for the quiz are generated from question manager.<br>
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
#### `quiz_timer` Module
This module is designed to manage time tracking during the quiz session. It allows us to start a timer, check the remaining time for quiz and end the timer.<br>
**Attributes**
- `start_time`: The timestamp when the timer is started.
- `duration`: Users need to complete the exam within that time.

**Methods**
1. `__init__()`: Initialize a new instance of the class with basic attributes.
2. `start_timer(duration)`: Record the current time as start time and set duration for the timer.<br>
   *Parameters*: <br>
   `duration`: Total time for the timer.
3. `check_time_remaining()`: Calculate the elapsed time since started and return the remaining time by subtracting it from the duration. Returns 0 if the timer has expired.

4. `end_timer()`: End the timer and reset the start time.
