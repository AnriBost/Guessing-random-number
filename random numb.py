import random
num = random.randint(1,10)
num_guess = 0

while num_guess != num:
    num_guess = int(input('Enter Guess : '))
    if (num_guess < num):
        print('wrong')
    elif (num_guess > num):
        print('wrong')
    else:
        print('correct')