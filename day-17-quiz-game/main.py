from question_model import Question
from data import question_data, question_data2
from quiz_brain import QuizBrain

question_bank = []
for question in question_data2:
    temp = Question(question["question"], question["correct_answer"])
    question_bank.append(temp)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the quiz")
print(f"You final score was: {quiz.score}/{quiz.question_number}")