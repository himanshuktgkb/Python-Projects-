from data import Question
from data import question_data

class QuizBrain:

    def __init__(self,list1):
        self.question_number=0
        self.score=0
        self.questions_list=list1
    def still_has_question(self):
        if self.question_number<len(self.questions_list):
            return True
        else:
            False
    def next_question(self):
        current_question=self.questions_list[self.question_number]
        self.question_number+=1
        ans=input(f"Q-{self.question_number}:{current_question.text} (True/False): ")
        self.check_answer(ans,current_question.answer)
    def check_answer(self,user_ans,actual_answer):
        if user_ans.lower()==actual_answer.lower():
            print("You got it right!")
            self.score+=1
        else :
            print("That's wrong.")
        print(f"Your current score is : {self.score}/{self.question_number}\n")
        # if user_ans.lower()==actual_answer.lower():
    

        
question_bank=[]
for question in question_data:
    question_text=question["text"]
    question_answer=question["answer"]
    new_question=Question(question_text,question_answer)
    question_bank.append(new_question)
quiz=QuizBrain(question_bank)
while quiz.still_has_question():

    quiz.next_question()
    # quiz.check_answer()

print(f"Now Quiz is over and your score is {quiz.score}")

