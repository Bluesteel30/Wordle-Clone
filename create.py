#This program is inspired by the New York Times game "Spelling Bee," go to https://www.nytimes.com/puzzles/spelling-bee to see the real thing.
fin = open('words_all_lengths.txt').readlines()
import random

def swap(mode: str):
    words_to_guess = []
    if mode == "EASY":
        max = 10
    elif mode == "MEDIUM":
        max = 20
    else:
        max = 40
    while len(words_to_guess) < max-5 or len(words_to_guess) > max+10:
        words_to_guess = []
        letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        t = []
        letters_to_use = []
        for i in range(7):
            x = random.choice(letters)
            letters_to_use.append(x)
            letters.remove(x)
        for line in fin:
            word = line.strip()
            for i in range(len(word)):
                if word[i] in letters:
                    break
                elif i == (len(word)-1):
                    t.append(word)
        score = 0
        must_use = letters_to_use[3]
        for i in t:
            if must_use in i and len(i)>3:
                words_to_guess.append(i)
    print(letters_to_use, "you must use the letter", must_use)
    print("you have up to", len(words_to_guess), "words to guess")
    return words_to_guess

def guess(words_to_guess: list):
    score = 0
    guess = input("Enter a word to guess or \" I QUIT \" to quit: " )
    while guess.strip() != "I QUIT":
        if guess.strip() in words_to_guess:
            words_to_guess.remove(guess.strip())
            print("You have", len(words_to_guess), "words to guess")
            score += len(guess.strip())
            print("Score: ", score)
        if len(words_to_guess) == 0:
            print("You Win!")
            break
        guess = input("Enter a word to guess or \" I QUIT \" to quit: " )
    print("Your final score is ", score, "The words to guess were", words_to_guess)
   
guess(swap(input("Enter a mode, EASY, MEDIUM, or HARD: ")))




