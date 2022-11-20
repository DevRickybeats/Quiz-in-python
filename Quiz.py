import time
import random

user_score = []


questions_dict = {
    'What is 10 multiplied by 10? ': ['100'],
    'What is the capital of Nigeria? ' : ['lagos'],
    'Which element is said to keep bones strong?': ['calcium'],
    # 'What is the main ingredient in guacamole?' : ['avocado'],
    # 'Rojo is the Spanish word for which colour?' : ['red'],
    # 'The logo for luxury car maker Porsche features which animal?' : ['horse'],
    # 'In tennis, what piece of fruit is found at the top of the mens Wimbledon trophy?' : ['pineapple'],
    # 'What is a female elephant called?' : ['cow'],
    # 'Franz Josef Strauss Airport is located in which country?' : ['germany'],
    # 'Caledonia was the Roman name for which modern day country?' : ['scotland']
    }


# defining a sleep function to control the print timer on the terminal
def some_sleep(x):
    return time.sleep(x)


# converting my questionsss dictionary to a list so I can call random.shuffle on it
questions_list = list(questions_dict.items())
random.shuffle(questions_list)

# defining my function to print the questions and validate the answers
def quiz ():
    correct_answer = 0
    failed_answer = 0
    total_score = 0
    user_score_percentage = 0
    
    User_info = input('Hello, What is your name? ')
    while User_info  == '':
           User_info = input('Please enter your name: ')
    some_sleep(0.3)
    print(f'\nHey {User_info!r}, Welcome to your quiz: ')

    for questions, options in questions_list:
        print (f"\n{questions}") 
        answer = input()
        answer = answer.lower()
    
    #validate answer
        while answer  == '':
            print (questions)
            answer = input('Pls, make an input: ')
            answer = answer.lower()

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
           
    
    print(f'\nYou answered {correct_answer} correctly!')
    print(f'\nYou failed {failed_answer}')
    Percentagemath = int(correct_answer/3 * 100)
    user_score_percentage += Percentagemath
    percentage = print(f'\nYou got {Percentagemath}%')

    user_score.append((User_info,user_score_percentage))
                      
                      
#defined a function to begin the Quiz
def begin ():
    global ready
    ready = input("Would you like to begin? (y/n) ")

#Called the begin function
begin()

#defined a function to check for empty strings
def empty_string(x):
    while x  == '':
            x = input('Pls, make an input: ')
            x = x.lower()


empty_string(ready)

def kick_off(x):
    if x == 'no' or x == 'n':
        close = input("Exit? (y/n) ")
        empty_string(close)
        if close == 'y': exit()
        else: quiz()
    else:
        quiz()
    
kick_off(ready)
      
  
some_sleep(0.2)
prompt = input("\nDo you want to play again? (y/n) 1st")
empty_string(prompt)

while prompt:
    kick_off(prompt)
    prompt = input("\nDo you want to play again? (y/n) ")
    empty_string(prompt)
    if prompt == 'n':
        prompt = False
    
        

# #setting some conditions

# if prompt == 'y' or prompt == 'yes':
#     some_sleep(0.3)
#     quiz()
#     # prompt = input("\nDo you want to play again? (y/n) ") 
# else:
#     some_sleep(0.5)
#     print('\nThe End')

print(user_score)
    


# highest_score = max(user_score)
# print(highest_score)
# print(f"Hey! {highest_score!r} got this highest point")


