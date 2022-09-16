from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for obj in question_data:
    question_bank.append(Question(obj['question'], obj['correct_answer']))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()
print("You have completed the quiz")
print(f"Your Final score was {quiz.score}/{quiz.question_number}")

