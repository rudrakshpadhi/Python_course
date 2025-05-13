from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for dict in question_data:
    text = dict["text"]
    answer = dict["answer"]
    new_q = Question(text,answer)
    question_bank.append(new_q)

current_quiz = QuizBrain(question_bank)
while(current_quiz.still_has_questions()):
    current_quiz.nextQuestion()

print(f"You've completed the quiz. Your final score was {current_quiz.score}/{len(question_bank)}")    

