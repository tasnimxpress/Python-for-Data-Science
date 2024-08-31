# create quizzbrain class
class QuizBrain:

    # define attribute
    def __init__(self, question_list):
        self.question_number = 0
        self.list = question_list

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        input(f"Q.{self.question_number} {
              current_question.text}: (True/False) ")
