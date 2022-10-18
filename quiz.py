# import modules: random, json, requests and html
import random
import json
import requests
import html

# loop to ask if the user wants to play again
while True:
    url = "https://opentdb.com/api.php?amount=1&category=31&type=multiple"
    q_no = 0
    correct = 0
    # loop for no of questions
    while q_no < 5:
        link = requests.get(url)
        # if the url is unreachable for some reason
        if link.status_code != 200:
            print("Sorry, there was a problem retrieving the question. Press enter to try again or type 'no' to quit the game.")
        else:
            print('###################################################')
            qnas = json.loads(link.text)
            question = qnas['results'][0]['question']
            answers = qnas['results'][0]['incorrect_answers']
            correct_answer = html.unescape(qnas['results'][0]['correct_answer'])
            answers.append(correct_answer)
            random.shuffle(answers)
            options = {
                'A': f'{html.unescape(answers[0])}',
                'B': f'{html.unescape(answers[1])}',
                'C': f'{html.unescape(answers[2])}',
                'D': f'{html.unescape(answers[3])}'
            }
        
            print(f"{html.unescape(question)}")
            print(f'''
        A - {options.get('A')}
        B - {options.get('B')}
        C - {options.get('C')}
        D - {options.get('D')}
            ''')

        # ask and validate user's input
        data_valid = False
        while data_valid == False:
            user_ans = input('Your answer: ').upper()
            try:
                user_ans = str(user_ans)
            except:
                print('Invalid input')
                continue
            if user_ans in options:
                data_valid = True
            else: 
                print('Invalid input')

        # check if answer is correct
        if options.get(user_ans) == correct_answer:
            print('CORRECT')
            correct += 1
        else:
            print('WRONG')
        print(f'The correct answer is: {correct_answer}')

        q_no += 1   # increment question number

    print('###################################################')
    print(f'You got {correct}/{q_no} questions correctly')

    play_again = input("Will you like to play again? Type 'no' to quit: ").lower()
    if play_again == "no":
        break

print('GAME OVER!!! Thanks for playing :)')