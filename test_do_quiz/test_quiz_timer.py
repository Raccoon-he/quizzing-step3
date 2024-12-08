import unittest
import time
from quizzing.do_quiz.quiz_timer import Timer

class TestQuizTimer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('Set up the timer test class.')
        
    def setUp(self):
        print('Set up a timer.')
        self.timer = Timer()
    
    def tearDown(self):
        print('Tear down the timer.')
        self.timer.end_timer()
    
    @classmethod
    def tearDownClass(cls):
        print('Tear down the timer test class.')
        
    def test_start_timer(self):
        self.assertIsNone(self.timer.start_time)
        self.assertEqual(self.timer.duration, 0)
        self.timer.start_timer(60)
        self.assertIsNotNone(self.timer.start_time) # test timer starts successfully
        self.assertEqual(self.timer.duration, 60)
        self.timer.start_timer(60)
            
    def test_check_time_remaining(self):
        self.timer.end_timer()
        self.timer.start_timer(30)
        time.sleep(5)
        self.assertEqual(self.timer.duration, 30)
        self.assertLessEqual(self.timer.check_time_remaining(), 25)
        self.assertGreaterEqual(self.timer.check_time_remaining(), 15)
        time.sleep(3)
        self.assertLessEqual(self.timer.check_time_remaining(), 22)

        
# unittest.main(argv=[''], verbosity=2, exit=False)        
