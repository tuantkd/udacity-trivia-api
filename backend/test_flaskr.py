import unittest
import requests
from dotenv import dotenv_values

config = dotenv_values(".env")

class TriviaTestCase(unittest.TestCase):
    URL = config["FLASK_HOST"]

    data = {
        "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?",
        "answer": "Tom Cruise",
        "difficulty": 4,
        "category": 4
    }

    data_quizzes = {
        "previous_questions": [14, 15],
        "quiz_category": 3
    }
    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    def test_get_categories(self):
        res = requests.get(self.URL + '/get-categories')
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 2)
        print("Test get_categories completed")


    def test_get_questions(self):
        res = requests.get(self.URL + "/get-questions")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 5)
        print("Test get_questions completed")


    def test_delete_question(self):
        res = requests.delete(self.URL + "/delete-question/38")
        self.assertEqual(res.status_code, 200)
        print("Test delete_question completed")


    def test_create_question(self):
        res = requests.post(self.URL + "/create-questions", json=self.data)
        self.assertEqual(res.status_code, 200)
        print("Test create_question completed")


    def test_search_questions(self):
        res = requests.post(self.URL + "/search-questions", json={"searchTerm" : "Whose autobiography"})
        self.assertEqual(res.status_code, 200)
        self.assertEqual(len(res.json()), 5)
        print("Test search_questions completed")
        

    def test_categories_questions(self):
        res = requests.get(self.URL + "/categories/4/questions")
        self.assertEqual(res.status_code, 200)
        print("Test categories_questions completed")


    def test_quizzes(self):
        res = requests.post(self.URL + "/quizzes", json=self.data_quizzes)
        self.assertEqual(res.status_code, 200)
        print("Test quizzes completed")


    def test_delete_question_error(self):
        res = requests.delete(self.URL + "/delete-question/90")
        self.assertEqual(res.status_code, 404)
        print("Test test_delete_question_error completed")


    def test_categories_questions_error(self):
        res = requests.get(self.URL + "/categories/90/questions")
        self.assertEqual(res.status_code, 404)
        print("Test test_categories_questions_error completed")

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest = TriviaTestCase()
    # unittest.test_get_categories()
    # unittest.test_get_questions()
    # unittest.test_delete_question()
    # unittest.test_create_question()
    # unittest.test_search_questions()
    # unittest.test_categories_questions()
    # unittest.test_quizzes()
    unittest.test_delete_question_error()
    unittest.test_categories_questions_error()