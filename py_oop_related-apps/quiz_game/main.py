from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    # constructing the question_model.py Question class below
    new_question = Question(question_text, question_answer)
    # new questions will now be added to our question_bank list
    question_bank.append(new_question)

# tests: print(question_bank), print(question_bank[0].text), print(question_bank[0].answer)

# constructing the quiz_brain.py QuizBrain class below
quiz = QuizBrain(question_bank)
# let's loop for next questions by first checking if the while loop is true or false with a method
# but if it is false, it will exit the while loop
while quiz.still_has_questions():
    quiz.next_question()

# this below should happen once all questions has been answered
print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")

# or print(f"Your final score is: {quiz.score}/{len(question_bank)}")
