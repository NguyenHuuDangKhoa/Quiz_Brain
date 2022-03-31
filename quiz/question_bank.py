from .data import question_data
from .question import Question


class QuestionBank:

    def __init__(self):
        self.questions = []

    def pull_question(self):
        for question in question_data:
            question_text = question["text"]
            question_answer = question["answer"]
            new_question = Question(question=question_text, answer=question_answer)
            self.questions.append(new_question)

