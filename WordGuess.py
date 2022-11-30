#Word Guessing Game

word = input()
for i in range(500):
    print("*")
visible = ["*"] * len(word)
lives = 5
used = ""
starCounter = len(word)
while True:
    print()
    for i in range(len(word)):
        print(visible[i], end = "")
    print()    
    letter = input("Enter a lower case letter:")
    if (used.find(letter) != -1):
        while (used.find(letter) != -1):
            print("You have used this letter before. Please enter again:")
            letter = input()
    if (word.find(letter)) != -1:
        print()
        used += letter
        print()
        for i in range(len(word)):
            if word[i] == letter:
                visible[i] = letter
                starCounter -= 1
        for i in range(len(word)):
            print(visible[i], end = "")
        print()
        print("Life left:"+str(lives))
        print("So far you have used these letters:"+str(used))
        if starCounter == 0:
            print("You won!")
            break
    elif (word.find(letter)) == -1:
        lives -= 1
        used += letter
        print("Life left:"+str(lives))
        print("So far you have used these letters:"+str(used))
        if lives == 0:
            print("The correct word is", word)
            print("You lost!")
            break