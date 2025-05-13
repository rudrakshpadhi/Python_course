class QuizBrain:
    def __init__(self,questions_list):
        self.question_number = 0
        self.questions_list = questions_list
        self.score = 0
    def nextQuestion(self):
        question =  self.questions_list[self.question_number] 
        self.question_number+=1  
        user_answer = input(f"Q.{self.question_number}: {question.text} (True/False) ")
        self.checkAnswer(user_answer,question)
        self.points_management()
        print("\n")
    def still_has_questions(self):
        return self.question_number<len(self.questions_list)
    def checkAnswer(self,user_input,question):
        if(user_input.lower()==question.answer.lower()):
            self.score+=1
            print("You got it right! You got a point.")
        else:
            print("That's wrong!")
        print(f"The correct answer is {question.answer}")
    def points_management(self):
        print(f"Your current points are {self.score}/{self.question_number}")    

