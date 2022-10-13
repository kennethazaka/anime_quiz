# import modules, 'random' and 'time'
import random as r
from questions import qnas

# loop to ask if the user wants to play again
while True:
    r.shuffle(qnas)

    # blank space
    print()
    n = 0
    no_question = 0 # question number
    correct = 0     # number of correct answers

    # loop to count correct answers and number of questions asked
    while no_question < 5:
        print('-----------------------------------------------------')
        # define question
        question = qnas[n]['results'][0]['question']

        # print question
        print(question)
        
        # define answers
        answers = [
            qnas[n]['results'][0]['correct_answer'],
            qnas[n]['results'][0]['incorrect_answers'][0],
            qnas[n]['results'][0]['incorrect_answers'][1],
            qnas[n]['results'][0]['incorrect_answers'][2]
        ]
        r.shuffle(answers)

        # define options
        options = {
            'A': f'{answers[0]}',
            'B': f'{answers[1]}',
            'C': f'{answers[2]}',
            'D': f'{answers[3]}'
        }

        # print options
        print(f'''
    A - {options.get("A")}
    B - {options.get("B")}
    C - {options.get("C")}
    D - {options.get("D")}    
        ''')

        # validate user's input to prevent wrong input data types and letters that aren't a,b,c or d
        data_valid = False
        while data_valid == False:
            user_ans = input("Your answer: ").upper()
            try:
                user_ans = str(user_ans)
            except:
                print('Invalid input')
                continue
            if (user_ans in options):
                data_valid = True
            else:
                print('Invalid input')
        
        # check if answer is correct
        if options.get(user_ans) == qnas[n]['results'][0]['correct_answer']:
            print('CORRECT')
            correct += 1
        else:
            print('WRONG')

        no_question += 1    # increment number of questions
        n += 1
        # end of loop
    print('-----------------------------------------------------')
    print(f'You got {correct}/{no_question} questions correctly')

    play_again = input("Will you like to play again? Type 'no' to quit: ").lower()
    if play_again == "no":
        break

print('GAME OVER!!! Thanks for playing :)')
# END OF CODE