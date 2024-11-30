from do_quiz.quizsession import QuizSession
from do_quiz.timer import Timer

questions = [
    {
        "id": 1,
        "text": "What is the capital of France? A) Paris B) London C) Madrid D) Berlin",
        "category": "Geography",
        "difficulty": "Easy",
        "answer": "C",
    },
    {
        "id": 3,
        "text": "What chemical element has the symbol Au? A) Gold B) Silver C) Iron D) Copper",
        "category": "Math",
        "difficulty": "Easy",
        "answer": "B",
    }
] # return by get_random_questions

quiz = QuizSession()
quiz.start_quiz(questions)

timer = Timer()
timer.start_timer(3)

while quiz.current_question_index < len(quiz.questions):
    remaining_time = timer.check_time_remaining()
    if remaining_time <= 0:
        print("Time is up!")
        break
            
    current_question = quiz.questions[quiz.current_question_index]
    
    # Question id & content
    print("Question {}\n{}".format(current_question['id'],current_question['text']))
    answer = input("Your Answer: ").upper()
    print('\n')
    quiz.submit_answer(answer)
    
timer.end_timer()  
quiz.end_quiz()
if quiz.wrong_answers == []:
    print('Congratulations! You got full points!')
else:
    wrong_answers = quiz.get_wrong_answers()
    print(wrong_answers)
