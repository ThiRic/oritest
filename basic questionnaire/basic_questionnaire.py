from Question import Question

question_prompt = ['Do you have acne? \n(a) Yes\n(b) No\n\n' ,
                   'What is your type of skin?\n(a) Dry\n(b) Normal\n(c) Oily\n\na']

questions = [
    Question(question_prompt[0],score_1='a', score_2='b'),
    Question(question_prompt[1],score_1='c', score_3='b', score_5='a')
]

def run_test(questions):
    score_1=0
    score_2=0
    score_3=0
    score_4=0
    score_5=0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.score_1:
            score_1 += 1
        elif answer == question.score_2:
            score_2 += 1
        elif answer == question.score_3:
            score_3 += 1
        elif answer == question.score_4:
            score_4 += 1
        elif answer == question.score_5:
            score_5 += 1
        else:
            print('Please, enter a valid answer i.e. "a" or "b".')
    print('Your skin score is :\n'+'Score_1 :'+str(score_1)+'\n'+'Score_2 :'+str(score_2)+'\n'

          +'Score_3 :'+str(score_3)+'\n'+'Score_4 :'+str(score_4)+'\n'+'Score_5 :'+str(score_5)+'\n')
    if score_1 >= score_2 and score_1 >= score_3 and score_1 >= score_4 and score_1 >= score_5:
        print('Because your skin score_1 is high, we recommend you to use our set X.')
    else:
        print('Thank you for answering this skin questionnaire!')

run_test(questions)

input("\n\nPress enter to exit")