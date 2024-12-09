import unittest
from types import NoneType

from quizzing.question_bank.question_manager import questionmanager as qm

class TestQuestionManager(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print("Set up the test class.")

    def setUp(self):
        print("Set up the question manager.")
        self.manager = qm()
        self.questions = [
            {
                "id": 20,
                "text": "When did the Roman Empire fall? A) 376 AD B) 476 AD C) 576 AD D) 676 AD",
                "answer": "B",
                "difficulty": "medium",
                "category": "history"
            },
            {
                "id": 21,
                "text": "What is the boiling point of water? A) 90\u00a1C B) 95\u00a1C C) 100\u00a1C D) 105\u00a1C",
                "answer": "C",
                "difficulty": "easy",
                "category": "science"
            },
            {
                "id": 22,
                "text": "What is the capital of Russia? A) St. Petersburg B) Moscow C) Kiev D) Minsk",
                "answer": "B",
                "difficulty": "easy",
                "category": "geography"
            },
            {
                "id": 23,
                "text": "What is 3^2 + 4^2? A) 20 B) 25 C) 30 D) 35",
                "answer": "B",
                "difficulty": "medium",
                "category": "mathematics"
            },
            {
                "id": 24,
                "text": "Which company owns Android? A) Apple B) Microsoft C) Google D) Samsung",
                "answer": "C",
                "difficulty": "easy",
                "category": "technology"
            },
            {
                "id": 24,
                "text": "Which company owns Android? A) Apple B) Microsoft C) Google D) Samsung",
                "answer": "C",
                "difficulty": "easy",
                "category": "technology"
            }
        ]

    def tearDown(self):
        print("Tear down the question manager.")
        self.manager = None
        self.questions = None

    @classmethod
    def tearDownClass(cls):
        print("Tear down the test class.")

    def test_add_question(self):
        self.manager.add_question(self.questions[0])
        self.assertEqual(len(self.manager.question_bank), 1)
        self.assertEqual(self.manager.question_bank[0]['id'], 20)
        self.manager.add_question(self.questions[1])
        self.manager.add_question(self.questions[2])
        self.manager.add_question(self.questions[3])
        self.manager.add_question(self.questions[4])
        self.assertEqual(len(self.manager.question_bank), 5)
        self.assertEqual(self.manager.question_bank[4]['id'], 24)
        self.assertEqual(self.manager.add_question(self.questions[5]), None)

    def test_remove_question(self):
        self.test_add_question()
        self.manager.remove_question(20)
        self.assertEqual(len(self.manager.question_bank), 4)
        self.assertEqual(self.manager.question_bank[3]['id'], 24)
        self.manager.remove_question(24)
        self.assertEqual(len(self.manager.question_bank), 3)
        self.assertEqual(self.manager.question_bank[2]['id'], 23)
        self.assertEqual(self.manager.remove_question(25), None)


    def test_update_question(self):
        self.test_add_question()
        self.manager.update_question(20, {"answer": "C","difficulty": "hard","category": "technology"})
        self.assertEqual(self.manager.question_bank[0]['answer'], 'C')
        self.assertEqual(self.manager.question_bank[0]['difficulty'], 'hard')
        self.assertEqual(self.manager.question_bank[0]['category'], 'technology')
        self.manager.update_question(24, {"answer": "D", "difficulty": "medium"})
        self.assertEqual(self.manager.question_bank[4]['answer'], 'D')
        self.assertEqual(self.manager.question_bank[4]['difficulty'], 'medium')
        self.assertEqual(self.manager.update_question(25,{"answer": "D", "difficulty": "medium"}), None)

    def test_get_question(self):
        self.test_add_question()
        self.assertEqual(self.manager.get_question_by_id(20)['answer'], 'B')
        self.assertEqual(self.manager.get_question_by_id(21)['difficulty'], 'easy')
        self.assertEqual(self.manager.get_question_by_id(22)['category'], 'geography')
        self.assertEqual(self.manager.get_question_by_id(23)['answer'], 'B')
        self.assertEqual(self.manager.get_question_by_id(24)['difficulty'], 'easy')
        self.assertEqual(len(self.manager.list_all_questions()), 5)
        self.assertEqual(self.manager.get_question_by_id(25), None)


