### `question_bank` Sub-package
---
#### `question_loader` Module 
This module is responsible for loading, classifying, and analyzing quiz questions. It provides utilities to organize questions and perform statistical analysis on them.

**Methods**
1. `load_questions_from_file(filepath)`: Load questions from a JSON or CSV file and return them as a list of dictionaries.
   *Parameters*:  
   `filepath`: The file path of the JSON or CSV file containing questions.

2. `classify_questions(questions)`: Classify questions into categories and calculate statistics (e.g., counts of questions per category).  
   Returns a dictionary with:
   - `classification`: Questions grouped by their categories.
   - `stats`: A count of questions per category.  
   *Parameters*:  
   `questions`: A list of question dictionaries.

3. `get_random_questions(questions, category, number)`: Retrieve a specified number of random questions from the given category.  
   *Parameters*:  
   `questions`: A list of available questions.  
   `category`: The category to filter questions by.  
   `number`: The number of questions to retrieve.

4. `filter_questions_by_difficulty(questions, difficulty)`: Filter questions based on their difficulty level (e.g., Easy, Medium, Hard).
    *Parameters*: 
    `questions`: A list of questions.
    `difficulty`: The difficulty level to filter by.
    *Returns*: A list of questions matching the specified difficulty.
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
