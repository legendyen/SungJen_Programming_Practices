class QuizBrain:

    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_list = question_bank

    def still_has_question(self):
        if len(self.question_list) > self.question_number:
            return True
        else:
            print("You've complete the quiz.")
            print(f"Your total score is {self.score} / {self.question_number}")
            return False

    def next_question(self):
        current_question = self.question_list[self.question_number]
        self.question_number += 1
        user_choice = input(f"Q.{self.question_number}: {current_question.text} (True/False): ")
        self.check_answer(user_choice, current_question.answer)

    def check_answer(self, user_choice, correct_answer):
        if user_choice.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print(f"That is wrong. The correct answer is {correct_answer}")
        print(f"Your score is {self.score} / {self.question_number}\n")


