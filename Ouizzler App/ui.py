import tkinter as tk
from gc import disable
from tkinter import Canvas
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = tk.Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, pady=20, padx=20)

        self.score_label = tk.Label(text="Score: ", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)
        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150,125, width=280, text="Question",  font=("Arial", 20, "italic"), fill=THEME_COLOR)
        self.canvas.grid(column=0, columnspan=2, row=1, pady=50)

        self.button_true_img = tk.PhotoImage(file="images/true.png")
        self.button_true=tk.Button(image=self.button_true_img, highlightthickness=0, command=self.answer_true)
        self.button_true.grid(column=0, row=2)

        self.button_false_img = tk.PhotoImage(file="images/false.png")
        self.button_false = tk.Button(image=self.button_false_img, highlightthickness=0, command=self.answer_false)
        self.button_false.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the game.")

    def answer_true(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)


    def answer_false(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        elif not is_right:
            self.canvas.config(bg="red")

        self.canvas.update()
        self.window.after(1000)
        self.canvas.config(bg="white")
        self.get_next_question()
