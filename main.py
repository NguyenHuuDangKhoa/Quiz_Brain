from quiz.question_bank import QuestionBank


def main():
    question_bank = QuestionBank()
    question_bank.pull_question()
    print(question_bank.questions)
    print(question_bank)


if __name__ == "__main__":
    main()

