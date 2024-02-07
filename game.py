import random
import sys

def checker(guess_num,usr_input):
  if guess_num == usr_input:
    print("Just Right!")
    sys.exit()
  else:
    if guess_num > usr_input:
      print("Too small")
    elif guess_num < usr_input:
      print("Too large")
    usr_input = int(input("Guess:"))
  checker(guess_num,usr_input)
def main():
  level = input("Level: ")
  guess_num = random.randint(1,9)
  usr_input = int(input("Guess: "))
  checker(guess_num,usr_input)


if __name__ == "__main__":
  main()