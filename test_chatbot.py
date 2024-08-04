
import unittest
from chatbot import get_ai_response

class TestChatbot(unittest.TestCase):
    def test_response(self):
        response = get_ai_response("Hello")
        self.assertIsInstance(response, str)
        self.assertGreater(len(response), 0)

if __name__ == '__main__':
    unittest.main()

