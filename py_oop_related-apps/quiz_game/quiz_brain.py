# asking the questions
# checking if the answer was correct
# checking if we're at the end of the quiz

class QuizBrain:

    def __init__(self, q_list):
        # below is a default/initial question_number attribute
        self.question_number = 0
        # the question_bank in main.py will be placed inside the QuizBrain's class question_list attribute
        self.question_list = q_list
        # this is our default/initial score attribute
        self.score = 0

    # creating a method from our class above, to check if there are still questions available or not
    def still_has_questions(self):
        # this returns a boolean, true or false
        return self.question_number < len(self.question_list)

    # creating a method from our class above, this executes next questions
    def next_question(self):
        current_question = self.question_list[self.question_number]
        # below is the print format of how it will prompt the user to respond to questions
        self.question_number += 1  # makes our output counting start from 1, and not the raw 0
        user_answer = input(f"\nQ.{self.question_number} {current_question.text} (True/False): ")
        # compare answers, if they are correct and the same in both sides
        self.check_answer(user_answer, current_question.answer)

    # creating a method from our class above, to check user's answers if its right or wrong
    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it right!")
            print(f"Your current score is: {self.score}/{self.question_number}")
        else:
            print(f"That's wrong!\nThe correct answer is: {correct_answer}")
            print(f"Your current score is: {self.score}/{self.question_number}")


