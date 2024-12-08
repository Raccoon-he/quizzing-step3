import unittest
from quizzing.do_quiz.quiz_session import QuizSession
class TestQuizSession(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Set up the test class.')
    
    def setUp(self):
        print('Set up a quiz.')
        self.quiz = QuizSession()
        self.questions = [
    {
        "id": 1,
        "text": "What is the capital of France? A) Paris B) London C) Madrid D) Berlin",
        "category": "Geography",
        "difficulty": "Easy",
        "answer": "A",
    },
    {
        "id": 2,
        "text": "What chemical element has the symbol Au? A) Gold B) Silver C) Iron D) Copper",
        "category": "Science",
        "difficulty": "Easy",
        "answer": "A",
    },
    {
        "id": 3,
        "text": "What is the square root of 144? A) 10 B) 12 C) 14 D) 16",
        "category": "Mathematics",
        "difficulty": "Medium",
        "answer": "B",
    }]
        self.quiz.start_quiz(self.questions)
        
    def tearDown(self):
        print('Tear down the quiz.')
        self.quiz.current_question_index = 0
    
    @classmethod
    def tearDownClass(cls):
        print('Tear down the test class.')
        
    
    def test_start_quiz(self): # test the original state for a quiz
        self.assertEqual(len(self.quiz.questions), 3)
        self.assertEqual(self.quiz.score, 0)
        self.assertEqual(self.quiz.current_question_index, 0)
        self.assertEqual(self.quiz.wrong_answers, [])
        
    def test_submit_answers(self):
        self.quiz.submit_answer('B') # Question 1: wrong
        self.assertEqual(self.quiz.score, 0)
        self.assertEqual(self.quiz.current_question_index, 1)
        self.assertEqual(self.quiz.wrong_answers[0]['users_answer'], 'B')
        self.assertEqual(self.quiz.questions[self.quiz.current_question_index]['answer'], 'A') # next correct answer
        
        self.quiz.submit_answer('A') # Question 2: correct
        self.assertEqual(self.quiz.score, 1)
        self.assertEqual(self.quiz.current_question_index, 2)
        self.assertEqual(len(self.quiz.wrong_answers), 1)
        self.assertEqual(self.quiz.questions[self.quiz.current_question_index]['answer'], 'B')
  
        self.quiz.submit_answer('E') # Question 3: invalid
        self.assertEqual(self.quiz.score, 1)
        self.assertEqual(self.quiz.current_question_index, 2)
        self.assertEqual(len(self.quiz.wrong_answers), 1)
        self.assertEqual(self.quiz.questions[self.quiz.current_question_index]['answer'], 'B')
        
        self.quiz.submit_answer('C') # Question 3: wrong
        self.assertEqual(self.quiz.score, 1)
        self.assertEqual(self.quiz.current_question_index, 3)
        self.assertEqual(len(self.quiz.wrong_answers), 2)
        self.assertEqual(self.quiz.wrong_answers[len(self.quiz.wrong_answers)-1]['answer'], 'B') # correct answer
    
    def test_score_wrong_answer(self):
        self.quiz.submit_answer('A')
        self.quiz.submit_answer('B') # wrong
        self.quiz.submit_answer('B')
        self.assertEqual(self.quiz.score, 2)
        self.assertEqual(self.quiz.end_quiz(), "Score you got is: 2.\n")
        self.assertEqual(len(self.quiz.wrong_answers), 1)
        self.assertEqual(self.quiz.wrong_answers[0]['answer'], 'A')
        self.assertEqual(self.quiz.wrong_answers[0]['users_answer'], 'B')
        correct_output = (
            '------ Questions your answered wrong ------\n'
            'Question 2\n'
            'What chemical element has the symbol Au? A) Gold B) Silver C) Iron D) Copper\n'
            'Category: Science\n'
            'Difficulty: Easy\n'
            'Answer: A\n'
            'Your answer: B\n'
            '------ Above are all ------\n'
            'Good luck for next time!'
        )
        self.assertEqual(self.quiz.get_wrong_answers(), correct_output)
        
        
        
# unittest.main(argv=[''], verbosity=2, exit=False)
