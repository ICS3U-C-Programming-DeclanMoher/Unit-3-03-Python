#!/usr/bin/env python3
import random


def main():
    random_variable = random.randint(0, 9)
    user_guess = int(input("Number: "))
    if random_variable != user_guess:
        print("You are wrong")
    if random_variable == user_guess:
        print("You are right")


if __name__ == "__main__":
    main()
