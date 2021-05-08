#SHUFFLE GAME
from random import shuffle

def user_guess():
  guess=''

  while guess not in ['0','1','2']:
    guess=input("pick a no. from 0,1 or 2: ")

  return int(guess)


def check_my_guess(my_list,guess):
  if my_list[guess]=='O':
    print('Correct!')
  else:
    print('Wrong guess!')
    print(my_list)


#initialize list
my_list=['','','O']
#shuffle list
mixed_up_list=shuffle(my_list)
#user guess
guess = user_guess()
#check guess
check_my_guess(my_list,guess)
