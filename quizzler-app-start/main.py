from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from ui import User_Interface
question_bank = []
for question in question_data:
    question_text = question["question"]
    question_answer = question["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
UI = User_Interface(quiz)

# while quiz.still_has_questions():
#     quiz.next_question()


