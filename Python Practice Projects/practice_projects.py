##############  Guess the number using python ###############
import random

def guess(x):
    random_no = random.randint(1,x)
    guess = 0
    count = 0
    print('Hey this is a small game of guessing a number between a range of 1 and 100..\n')
    print('if the number of attempts are less than or equal to 5 then you will get 1st prize\n')
    print('if the number of attempts greater than 5 but less than 10 then you will get 2nd prize\n')
    print('if the number of attempts greater than or equal to 10 then you will get 3rd prize\n')
    while (guess != random_no):
        guess = int(input(f'Enter a number between 1 and {x} :'))
        count += 1
        if (guess < random_no):
            print('Higher number please..!')
        elif (guess > random_no):
            print('Lower number please..!')
        else:
            print(f'Yay..! you have guessed the number {random_no}')
    print(f'you have guessed the number in {count} attempts..')
    if (count <= 5):
        print('Congrats ! you got 1st prize.')
    elif (5 < count < 10 ):
        print('Congrats ! you got 2nd prize.')
    else:
        print('Congrats ! You got 3rd prize')

guess(100)
