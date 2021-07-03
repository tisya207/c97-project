import random

number = random.randint(1,9)
#print(number)
print('GUESS A NUMBER: (you random no. range is 1-9)')
chances=1
while chances <=5:
    guess=int(input('enter your guess '))
    print(guess)
    if guess == number:
        print("congo you've guessed the no. right!!")
        break
    elif guess > number:
        print('the no is smaller than the no. you have guessed')
    elif guess < number:
        print('the no is greater than the no. you have guessed')
    chances+=1

if not chances<5:
        print('you lose, the correct number is ' + number)