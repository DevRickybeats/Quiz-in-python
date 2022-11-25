import time
import random

user_score = []

questions_dict = {
    'What is 10 multiplied by 10? ': ['100'],
    'What is the capital of Nigeria? ': ['lagos'],
    'Which element is said to keep bones strong?': ['calcium'],
    'What is the main ingredient in guacamole?': ['avocado'],
    'Rojo is the Spanish word for which colour?': ['red'],
    'The logo for luxury car maker Porsche features which animal?': ['horse'],
    'In tennis, what piece of fruit is found at the top of the mens Wimbledon trophy?': ['pineapple'],
    'What is a female elephant called?': ['cow'],
    'Franz Josef Strauss Airport is located in which country?': ['germany'],
    'Caledonia was the Roman name for which modern day country?': ['scotland'],
    'What was Meta Platforms Inc formerly known as?': ['facebook'],
    'What is the currency of Poland?': ['zloty'],
    'Which is the only planet in our solar system not named after a Roman or Greek god?': ['earth'],
    'What is the capital of Brazil?': ['brasilia'],
    'In which year did the Beatles Band begin?': ['1956'],
    'When was the first World War fought?': ['1914'],
    'How many bones are there in the human body?': ['206'],
    'Who is the founder of Apple Company?': ['steve jobs'],
    'Which planet is closest to Sun?': ['mercury'],
    'Which is the largest planet of the Solar System?': ['jupiter']
}


# defining a sleep function to control the print timer on the terminal
def some_sleep(x):
    return time.sleep(x)


def quiz():
    correct_answer = 0
    user_score_percentage = 0

    User_info = input('Hello, What is your name? ')
    while User_info == '':
        User_info = input('Please enter your name: ')
    some_sleep(0.3)
    print(f'\nHey {User_info!r}, Welcome to your quiz: ')

    length = len(questions_dict)

    def tried():
        while True:
            try:
                global n_o_q
                n_o_q = int(input('\nHow many questions do you want? '))
            except ValueError:
                print(f'Please enter a number from 1-{length} ')
                continue
            else:
                break

    tried()

    while True:
        if n_o_q > length:
            print(f'Out of range, Please enter a number from 1-{length} ')
            tried()
        else:
            break

    questions_list = list(questions_dict.items())
    random.shuffle(questions_list)
    new_questions_list = questions_list[0:n_o_q]

    some_sleep(0.2)

    for questions, options in new_questions_list:  # A for loop to print the questions and validate the answers
        print(f"\n{questions}")
        answer = input().lower()

        while answer == '':  # validate user answer
            print(questions)
            answer = input('Pls, make an input: ').lower()

        right_answer = options[0]  # Check for the right answer
        if answer == right_answer:
            some_sleep(0.2)
            print('\nCorrect Answer!')
            correct_answer += 1
        else:
            some_sleep(0.2)
            print(f'Wrong, The right answer is {right_answer}.')

    print(f'\nYou answered {correct_answer} correctly! out of {n_o_q}.')
    Percentagemath = int(correct_answer/n_o_q * 100)
    user_score_percentage += Percentagemath
    print(f'\nYou got {Percentagemath}%')

    user_score.append((User_info, user_score_percentage))


# Defined a function to begin the Quiz
def begin():
    ready = input("Would you like to begin? (y/n) ").lower()
    if ready != 'y' and ready != 'n':
        begin()
    elif ready == 'n':
        exit()
    quiz()


begin()  # Call the begin function


some_sleep(0.2)
repeat = True


def replay():
    replay_response = input('\nDo you want to play again? (y/n) ').lower()
    if replay_response == 'y':
        quiz()
    elif replay_response == 'n':

        for x, y in user_score:
            print(f'User: {x} scored {y}%')

        winner = max(user_score, key=lambda doc: doc[1])
        some_sleep(0.2)

        for x in winner:
            print(f"\nHey User: {x!r} got the highest score. ")
            break
        average_score = []
        for x in user_score:
            for y in x:
                average_score.append(y)

        only_numbers = [x for x in average_score if isinstance(x, int)]
        len_of_scores = len(only_numbers)
        total = 0
        for i in only_numbers:
            total += i
        avg = int(total / len_of_scores)
        some_sleep(0.3)
        print(f'\nThe average score amongst all users is {avg!r}%')
        exit()
    else:
        print('Please make a valid input')
        replay()


while repeat:
    replay()
