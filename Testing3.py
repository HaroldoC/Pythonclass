# import random


# def run_guess(guess, answer):
#     if 0 < guess < 11:
#         if guess == answer:
#             print("you are a genius!")
#             return True
#     else:
#         print("hey bozo, I said 1~10")
#         return False


# if __name__ == "__main__":
#     answer = random.randint(1, 10)
# while True:
#     try:
#         guess = int(input("guess a number 1 to 10: "))
#         run_guess(guess, answer)
#         if 0 < guess < 11:
#             if guess == answer:
#                 print("you are a genius!")
#                 break
#         else:
#             print("hey bozo, I said 1~10")
#     except ValueError:
#         print("please enter a number")
#         continue

# unittest


import unittest

import Testing3


class TestGame(unittest.TestCase):
    def test_input(self):
        result = Testing3.run_guess(5, 5)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = Testing3.run_guess(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = Testing3.run_guess(5, 11)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()


#     def test_do_stuff(self):
#         test_param = 10
#         result = main.do_stuff(test_param)
#         self.assertEqual(result, 15)

#     def test_do_stuff2(self):
#         test_param = "asdf"
#         result = main.do_stuff(test_param)
#         self.assertIsInstance(result, ValueError)

#     def test_do_stuff3(self):
#         test_param = None
#         result = main.do_stuff(test_param)
#         self.assertEqual(result, "please enter number")

#     def test_do_stuff4(self):
#         test_param = ""
#         result = main.do_stuff(test_param)
#         self.assertEqual(result, "please enter number")


# if __name__ == "__main__":
#     unittest.main()
