from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzy")
        self.window.config(padx=20, pady=25, bg=THEME_COLOR)

        self.score = Label(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white", font=("arial", 14, "bold"))
        self.score.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250, highlightthickness=0, bg="white")
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125,
                                                     text="test",
                                                     width=280,
                                                     font=("arial", 16, "italic"), fill=THEME_COLOR)

        false_img = PhotoImage(file="images/false.png")
        true_img = PhotoImage(file="images/true.png")

        self.false_btn = Button(image=false_img, highlightthickness=0, command=self.wrong_ans)
        self.false_btn.grid(row=2, column=0)
        self.true_btn = Button(image=true_img, highlightthickness=0, command=self.right_ans)
        self.true_btn.grid(row=2, column=1)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.canvas.config(bg="white")
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of quiz.")
            self.false_btn.config(state="disabled")
            self.true_btn.config(state="disabled")

    def right_ans(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_ans(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
