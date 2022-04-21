from data import question_data


class Question:

    def __init__(self, text, answer):
        self.text = text
        self.answer = answer


class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        answer = input(f"Q: {self.question_list[self.question_number].text} (True/False)?: ")
        self.check_answer(answer, self.question_list[self.question_number].answer)
        self.question_number += 1

    # return True/False
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, answer, actual_answer):
        if answer.lower() == actual_answer.lower():
            print("Correct")
            self.score += 1
        else:
            print("Incorrect")
        print(f"Your current score is {self.score}/{self.question_number+1}")
        print("\n")



question_bank = []

for q in question_data:
    qa = Question(q["question"], q["correct_answer"])
    question_bank.append(qa)

quiz = QuizBrain(question_bank)


while quiz.still_has_questions():

    quiz.next_question()

print(f"End of quiz.\nFinal score {quiz.score}/{quiz.question_number}")