class QuizBrain:
    def __init__(self, q_bank):
        self.question_number = 0
        self.question_list = q_bank
        self.score = 0


    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def current_question(self):
        new_question = self.question_list[self.question_number]
        self.question_number += 1
        user_answer = input(f'Q.{self.question_number}: {new_question.text} True/False: ')
        self.check_answer(user_answer, new_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print('right')
            self.score += 1
        else:
            print('wrong')

        print(f'Answer is {correct_answer}')
        print(f'current score: {self.score}/{self.question_number}\n ')
