# main.py

# import sub_package1
from quizzing.question_bank.question_loader import questionloader, random_question
from quizzing.question_bank.question_manager import questionmanager
# import sub_package2
from quizzing.do_quiz.quiz_session import QuizSession
from quizzing.do_quiz.quiz_timer import Timer

# initialize the question bank
manager = questionmanager()

# initialize the loader with the shared question_bank
loader = questionloader(manager)

# load questions from file
print(f"Please upload the questions file and enter the file name.")
file_name = input()
question_bank = loader.load_questions_from_file(file_name)
print(f"{file_name} has been loaded.")

while True:
    print(f"Please enter 'category' or 'difficulty' of the question bank. If you do not want to display anything, enter 'x'.")
    x1 = input()
    if x1 == 'x':
        break

    # show questions' categories and numbers
    elif x1 == 'category':
        q_category = loader.classify_questions_by_category(question_bank)
        print(q_category)

    # show questions' difficulties and numbers
    elif x1 == 'difficulty':
        q_difficulty = loader.classify_questions_by_difficulty(question_bank)
        print(q_difficulty)

while True:
    print(f"Please choose how to modify the question bank (add, remove, update). If you do not want to display anything, enter 'x'.")
    x2 = input()
    if x2 == 'x':
        break

    # add a new question
    elif x2 == 'add':
        add_id = int(input(f"Please enter the question id you want to add."))
        add_text = input(f"Please enter the question text you want to add.")
        add_answer = input(f"Please enter the question answer you want to add.")
        add_category = input(f"Please enter the question category you want to add.")
        add_difficulty = input(f"Please enter the question difficulty you want to add.")
        q_add = {"id": add_id, "text": add_text, "answer": add_answer, "category": add_category, "difficulty": add_difficulty}
        manager.add_question(q_add)
        print(f"{add_id} has been added.")

    # remove a question
    elif x2 == 'remove':
        remove_id = int(input(f"Please enter the question id you want to remove."))
        manager.remove_question(remove_id)
        print(f"{remove_id} has been removed.")

    # update a question
    elif x2 == 'update':
        update_id = int(input(f"Please enter the question id you want to update."))
        update_text = input(f"Please enter the question text you want to update.")
        update_answer = input(f"Please enter the question answer you want to update.")
        update_category = input(f"Please enter the question category you want to update.")
        update_difficulty = input(f"Please enter the question difficulty you want to update.")
        manager.update_question(update_id, {"text": update_text, "answer": update_answer, "category": update_category, "difficulty": update_difficulty})
        print(f"{update_id} has been updated.")

while True:
    print(f"Please choose how to display the question bank (byid, all). If you do not want to display anything, enter 'x'.")
    x3 = input()
    if x3 == 'x':
        break

    # display the question bank
    if x3 == 'all':
        print(manager.list_all_questions())

    # check the specific question
    if x3 == 'byid':
        check_id = int(input(f"Please enter the question id you want to check."))
        print(manager.get_question_by_id(check_id))

# get random questions
random_questions =[]
while True:
    random_question_bank = random_question(question_bank)
    print(f"Please enter 'y' to choose random questions for quiz. If you have chosen enough questions, enter 'x'.")
    x4 = input()
    if x4 == 'x':
        break

    if x4 == 'y':
        random_category = input(f"Please enter the question category you want to choose.\n")
        random_difficulty = input(f"Please enter the question difficulty you want to choose.\n")
        random_number = int(input(f"Please enter the question number you want to choose.\n"))
        random_questions.extend(random_question_bank.get_random_questions(category=random_category, difficulty=random_difficulty, number=int(random_number)))
        print(f"Random questions has been chosen for quiz.")
        
quiz = QuizSession()
quiz.start_quiz(random_questions)

timer = Timer()
timer.start_timer(60) # set time for 1min and start

while quiz.current_question_index < len(quiz.questions):
    remaining_time = timer.check_time_remaining()
    if remaining_time <= 0:
        print("Time is up!") # If time is run out, end the quiz
        break
            
    current_question = quiz.questions[quiz.current_question_index]
    
    # Question id & content
    print("Question {}\n{}".format(current_question['id'],current_question['text']))
    answer = input("Your Answer: ").upper()
    print('\n')
    quiz.submit_answer(answer)
    
# close timer and quiz
timer.end_timer()  
print(quiz.end_quiz()) 
if quiz.wrong_answers == []:
    print('Congratulations! You got full points!') # set message to users who get full scores
else:
    print(quiz.get_wrong_answers()) # show details of wrong answers

