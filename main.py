print("Welcome to the QUIZ GAME!\nChoose A, B, C or D")

score = 0

answer = input("\nWhat is the capital of France?\nA. Berlin\nB. Madrid\nC. Paris\nD. Rome\n").lower()
if answer == 'c':
    print("👏 You got it right.\nYou got 1 point.")
    score += 1
else:
    print("Oh no you got it wrong!")

answer = input("\nWhich planet is known as the Red Planet?\nA. Venus\nB. Mars\nC. Jupiter\nD. Saturn\n").lower()
if answer == 'b':
    print("👏 You got it right.\nYou got 1 point.")
    score += 1
else:
    print("Oh no you got it wrong!")

answer = input("\nWho wrote Romeo and Juliet?\nA. Charles Dickens\nB. William Shakespeare\nC. Mark Twain\nD. Jane Austen\n").lower()
if answer == 'b':
    print("👏 You got it right.\nYou got 1 point.")
    score += 1
else:
    print("Oh no you got it wrong!")

answer = input("\nWhat is the largest ocean on Earth?\nA. Atlantic Ocean\nB. Indian Ocean\nC. Arctic Ocean\nD. Pacific Ocean\n").lower()
if answer == 'd':
    print("👏 You got it right.\nYou got 1 point.")
    score += 1
else:
    print("Oh no you got it wrong!")

answer = input("\nWhich animal is known as the \"King of the Jungle\"?\nA. Tiger\nB. Elephant\nC. Lion\nD. Gorilla\n").lower()
if answer == 'c':
    print("👏 You got it right.\nYou got 1 point.")
    score += 1
else:
    print("Oh no you got it wrong!")

answer = input("\nWhat is the chemical symbol for gold?\nA. Au\nB. Ag\nC. Pb\nD. Go\n").lower()
if answer == 'a':
    print("👏 You got it right.\nYou got 1 point.")
    score += 1
else:
    print("Oh no you got it wrong!")

print(f"\nGreat!\nYou got {score} / 6")