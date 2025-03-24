print("Welcome to the QUIZ GAME!\nChoose A, B, C or D")

questions = [
    {"question": "What is the capital of France?", "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"], "answer": 'C'},
    {"question": "Which planet is known as the red planet?", "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"], "answer": 'B'},
    {"question": "Who wrote Romeo and Julet?", "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"], "answer": 'B'},
    {"question": "What is the largest ocean on Earth?", "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"], "answer": 'D'},
    {"question": "Which animal is known as the \"King of the Jungle\"?", "options": ["A. Tiger", "B. Elephant", "C. Lion", "D. Gorilla"], "answer": 'C'},
    {"question": "What is the Chemical symbol for Gold?", "options": ["A. Au", "B. Ag", "C. Pb", "D. Go"], "answer": 'A'},
]

score = 0

for question in questions:
    print(f"\n{question['question']}")
    for option in question['options']:
        print(option)
    answer = input("Enter the correct option: ")
    if answer.lower() == question['answer'].lower():
        print("👏 You got that right!\nYou win 1 point.")
        score += 1
    else:
        print("Oh no you got it wrong.")

if score <= 2:
    print(f"\n{score} / 6\nKeep trying!")
elif score <= 4:
    print(f"\n{score} / 6.\nGood job!")
else:
    print(f"\n{score} / 6\nYou're a quiz master!")
