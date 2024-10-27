class Question:
    text: str
    answer: str
    dupa: str

    def __init__(self, text, answer):
        self.answer = answer

    def print(self):
        print(f"{self.text}: {self.answer}")
