import unittest
from types import NoneType

from quizzing.question_bank.question_loader import questionloader, random_question
from quizzing.question_bank.question_manager import questionmanager


class TestQuestionLoader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Set up the test class.")

    def setUp(self):
        print("Set up the question bank.")
        self.ql1 = questionloader(questionmanager())
        self.ql2 = questionloader(questionmanager())
        self.questions1 = self.ql1.load_questions_from_file("test1.csv")
        self.questions2 = self.ql2.load_questions_from_file("test2.json")

    def tearDown(self):
        print("Tear down the question bank.")
        self.questions1 = None
        self.questions2 = None

    @classmethod
    def tearDownClass(cls):
        print("Tear down the test class.")

    def test_category(self):
        self.assertEqual(self.ql1.classify_questions_by_category(self.questions1)['geography'], 5)
        self.assertEqual(self.ql1.classify_questions_by_category(self.questions1)['science'], 5)
        self.assertEqual(self.ql2.classify_questions_by_category(self.questions2)['history'], 4)
        self.assertEqual(self.ql2.classify_questions_by_category(self.questions2)['languages'], [])

    def test_difficulty(self):
        self.assertEqual(self.ql1.classify_questions_by_difficulty(self.questions1)['easy'], 10)
        self.assertEqual(self.ql1.classify_questions_by_difficulty(self.questions1)['medium'], 14)
        self.assertEqual(self.ql1.classify_questions_by_difficulty(self.questions1)['hard'], 1)
        self.assertEqual(self.ql2.classify_questions_by_difficulty(self.questions2)['easy'], 10)
        self.assertEqual(self.ql2.classify_questions_by_difficulty(self.questions2)['medium'], 12)
        self.assertEqual(self.ql2.classify_questions_by_difficulty(self.questions2)['hard'], 2)

    def test_random_question(self):
        rd = random_question(self.questions1)
        self.assertEqual(len(rd.get_random_questions(category='geography', difficulty='easy', number=1)),1)
        self.assertEqual(len(rd.get_random_questions(category='geography', difficulty='medium', number=2)), 2)
        self.assertEqual(len(rd.get_random_questions(category='science', difficulty='easy', number=1)), 1)
        self.assertEqual(type(rd.get_random_questions(category='science', difficulty='easy', number=100)),NoneType)


