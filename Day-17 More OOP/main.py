from data import question_data, open_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []

for question in open_data:
    q1 = question['question']
    a1 = question['correct_answer']
    new_question = Question(q1, a1)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.current_question()

print("You've completed the quiz.")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
