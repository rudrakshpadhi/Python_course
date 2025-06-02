from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
TICK_IMG = "images/true.png"
WRONG_IMG = "images/false.png"
class User_Interface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.configure(bg = THEME_COLOR,padx=20,pady = 20)
        self.score_label = Label(text="Score: 0",fg = "white",bg = THEME_COLOR)
        self.score_label.grid(row = 0,column = 1)
        self.canvas = Canvas(bg = "white")
        self.canvas.config(height = 250,width = 300)
        self.canvas.grid(row = 1,column = 0,columnspan=2,pady = 50)
        self.curr_question = self.canvas.create_text(150,125,width = 280,text = "Nigga",font = ("Arial",20,"italic"),fill=THEME_COLOR)
        self.tick_img = PhotoImage(file = TICK_IMG)
        self.wrong_img = PhotoImage(file = WRONG_IMG)
        self.tick_button = Button(image = self.tick_img,highlightthickness=0,command = self.TruePressed)
        self.tick_button.grid(row = 2,column = 0)
        self.wrong_button = Button(image = self.wrong_img,highlightthickness=0,command = self.FalsePressed)
        self.wrong_button.grid(row=2,column = 1)
        self.getNextQuestion()
        self.window.mainloop()
    def getNextQuestion(self):
        if(self.quiz.still_has_questions()):
            question_text = self.quiz.next_question()
            self.score_label.config(text = f"Score: {self.quiz.score}")
            self.canvas.config(bg = "white")
            self.canvas.itemconfig(self.curr_question,text = question_text)
        else:
            self.canvas.config(bg = "white")
            self.canvas.itemconfig(self.curr_question,text = "You have reached the end of the quiz")
            self.tick_button.config(state="disabled")
            self.wrong_button.config(state="disabled")   
    def TruePressed(self):
        is_right = self.quiz.check_answer("True")
        self.giveFeedback(is_right)
    def FalsePressed(self):
        is_right = self.quiz.check_answer("False")
        self.giveFeedback(is_right)
    def giveFeedback(self,is_right):
        if(is_right):
            self.canvas.config(bg = "green")
        else:
            self.canvas.config(bg = "red")
        self.window.after(1000,self.getNextQuestion)        
