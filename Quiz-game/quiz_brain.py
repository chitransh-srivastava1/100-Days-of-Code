class QuizBrain:

    def __init__(self,q_list):
        self.question_number=0
        self.question_list=q_list
        self.score=0

    def check_answer(self,user_answer,correct_answer):
        if (user_answer==correct_answer):
            self.score+=1
            print(f"You are right. Your Score {self.score}/{self.question_number}")
        else:
            print("You are wrong")
        print(f"The correct answer was {correct_answer}")
        print("\n")

    def next_question(self):
        
        current_question=self.question_list[self.question_number]
        self.question_number+=1
        user_answer=input(f"Q.{self.question_number} {current_question.text} True/False ").lower()
        self.check_answer(user_answer,((current_question.answer).lower()))
    
    def has_more_question(self):
        if (len(self.question_list)>self.question_number):
            return True
        else:
            return False
