import time
import random

user_score = []

questions_dict = {
    # 'What is 10 multiplied by 10? ': ['100'],
    # 'What is the capital of Nigeria? ' : ['lagos'],
    # 'Which element is said to keep bones strong?': ['calcium'],
    # 'What is the main ingredient in guacamole?' : ['avocado'],
    'Rojo is the Spanish word for which colour?' : ['red'],
    # 'The logo for luxury car maker Porsche features which animal?' : ['horse'],
    # 'In tennis, what piece of fruit is found at the top of the mens Wimbledon trophy?' : ['pineapple'],
    'What is a female elephant called?' : ['cow'],
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
    Percentagemath = int(correct_answer/2 * 100)
    user_score_percentage += Percentagemath
    print(f'\nYou got {Percentagemath}%')

    user_score.append((User_info,user_score_percentage))
 
                      
#defined a function to begin the Quiz
def begin ():
    ready = input("Would you like to begin? (y/n) ").lower()
    if ready != 'y' and ready != 'n':
        begin()
    quiz()

#Call the begin function
begin()
   
   
some_sleep(0.2)
iop = True

def replay():
    replay_response = input('\nDo you want to play again? ').lower()
    if replay_response == 'y':
        quiz()
    elif replay_response == 'n':
        winner = max(user_score, key=lambda tup: tup[1])
        print(user_score)
        for x in winner:
            print(f"\nHey! {x!r} got the highest point ")
            break
        average_score = []
        for x in user_score:
            for y in x:
                average_score.append(y)
                
        only_numbers = [x for x in average_score if isinstance(x,int)]
        len_of_scores = len(only_numbers)
        total = 0
        for i in only_numbers:
            total += i
        avg = int(total / len_of_scores)
        print(f'\nThe average score amongst all users is {avg!r}%')
        exit()
    else:
        replay()


while iop: replay()
    

