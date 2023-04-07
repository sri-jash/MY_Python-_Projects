from question_model import Question
from data import  question_data
from quiz_brain import QuizBrain
question_bank=[]
for question in question_data:
    question_text = question["text"]
    question_answer=question["answer"]
    new_question =Question(question_text,question_answer)
    question_bank.append(new_question)

# print(question_bank)
quiz=QuizBrain(question_bank)
quiz.next_question()

while quiz.still_has_question():
    quiz.next_question()

print("You've completed the Quiz👍👍👍👍")
print(f"your Final Score was :{quiz.score}/{len(question_bank)}")
