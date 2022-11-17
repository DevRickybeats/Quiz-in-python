import time
import random

user_score = {}

questionsss = {
    'What is 10 multiplied by 10? ': ['100'],
    'What is the capital of Nigeria? ' : ['lagos'],
    'Which element is said to keep bones strong?': ['calcium'],
    'What is the main ingredient in guacamole?' : ['avocado'],
    'Rojo is the Spanish word for which colour?' : ['red'],
    'The logo for luxury car maker Porsche features which animal?' : ['horse'],
    'In tennis, what piece of fruit is found at the top of the mens Wimbledon trophy?' : ['pineapple'],
    'What is a female elephant called?' : ['cow'],
    'Franz Josef Strauss Airport is located in which country?' : ['germany'],
    'Caledonia was the Roman name for which modern day country?' : ['scotland']
    }




def some_sleep(x):
    return time.sleep(x)


User_info = input('Hello, What is your name? ')
while User_info  == '':
           User_info = input('Please enter your name: ')

some_sleep(0.3)
print(f'\nHey {User_info!r}, Welcome to your quiz: \n')




questionsss = list(questionsss.items())
random.shuffle(questionsss)


def quiz ():
    correct_answer = 0
    failed_answer = 0
    total_score = 0
    for questions, options in questionsss:
        print (f"\n{questions}") 
        answer = input()
        answer = answer.lower()
    
    #validate answer
        while answer  == '':
            print (questions)
            answer = input('Pls, Make an input: ')

    #Check for the right answer
        right_answer = options[0]
        if answer == right_answer:
            some_sleep(0.2)
            print('\nCorrect Answer!')
            correct_answer += 1
            total_score += 1
        else:
            some_sleep(0.2)
            print(f'\nWrong Answer, The answer is {right_answer}')
            failed_answer += 1
            # correct_answer = correct_answer - 1
            
    
    print(f'\nYou answered {correct_answer} correctly!')
    print(f'\nYou failed {failed_answer}')
    Percentagemath = correct_answer/5 * 100
    percentage = print(f'\nYou got {Percentagemath}%')


ready = input("Would you like to begin? (y/n) ")
#setting some conditions
# while ready != 'Y' or ready != 'y' or ready != 'n' or ready != 'N':
#     ready = input("Pls make an input")

if ready == 'Y' or ready == 'y' or ready == 'yes':
    some_sleep(0.4)
    quiz()
elif ready == 'N' or ready == 'n':
    ready = input("Exit? (y/n) ")
    if ready == 'Y' or ready == 'y': exit()
else: 
    some_sleep(0.4)
    print('\nThe End')
    exit()
  
  
  

some_sleep(0.2)
prompt = input("\nDo you want to play again? (y/n) ")
#setting some conditions
while True:
    if prompt == 'Y' or prompt== 'y':
        some_sleep(0.1)
        new_User_info = input('\nHi, What is your name? ')
        some_sleep(0.3)
        print(f'\nHey {new_User_info!r}, Welcome to your quiz: \n')
        quiz()
        prompt = input("\nDo you want to play again? (y/n) ")
    else:
        some_sleep(0.5)
        print('\nThe End')
        exit()

