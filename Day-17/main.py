# import data and question class

from data import question_data
from quiz_brain import QuizBrain
from question_model import Question


# create question bank
question_bank = []

for key in question_data:
    text = key['text']
    answer = key['answer']
    question = Question(text, answer)
    question_bank.append(question)


# print(question_bank[0].question)
quiz = QuizBrain(question_bank)
quiz_continue = True

while quiz.still_has_question():
    quiz.next_question()
