from question_model import q_quiz
from data import question_data
from quiz_brain import QuizBrain

question_bank=[]

for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    obj=q_quiz(question_text,question_answer)
    question_bank.append(obj)

quiz=QuizBrain(question_bank)

while quiz.has_more_question():
    quiz.next_question()

print("You have completed the Quiz")
print(f"Your final score is {quiz.score}/{len(question_bank)}")
