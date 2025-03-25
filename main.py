import random

print("Welcome to the QUIZ GAME!\nChoose A, B, C or D")

questions = [
    {"question": "What is the capital of France?", "options": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"], "answer": 'C'},
    {"question": "Which planet is known as the red planet?", "options": ["A. Venus", "B. Mars", "C. Jupiter", "D. Saturn"], "answer": 'B'},
    {"question": "Who wrote Romeo and Julet?", "options": ["A. Charles Dickens", "B. William Shakespeare", "C. Mark Twain", "D. Jane Austen"], "answer": 'B'},
    {"question": "What is the largest ocean on Earth?", "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"], "answer": 'D'},
    {"question": "Which animal is known as the \"King of the Jungle\"?", "options": ["A. Tiger", "B. Elephant", "C. Lion", "D. Gorilla"], "answer": 'C'},
    {"question": "What is the Chemical symbol for Gold?", "options": ["A. Au", "B. Ag", "C. Pb", "D. Go"], "answer": 'A'},
    {"question": "What year did the Titanic sink?", "options": ["A. 1912", "B. 1921", "C. 1905", "D. 1898"], "answer": 'A'},
    {"question": "What is the only metal that is liquid at room temperature?", "options": ["A. Gallium", "B. Mercury", "C. Cesium", "D. Lead"], "answer": 'B'},
    {"question": "What is the smallest country in the world by land area?", "options": ["A. Monaco", "B. Nauru", "C. Vatican City", "D. San Marino"], "answer": 'C'},
    {"question": "What was the first-ever video game?", "options": ["A. Pong", "B. Space Invaders", "C. Tennis for Two", "D. Pac-Man"], "answer": 'C'},
    {"question": "Which element is named after the greek for \"green\"?", "options": ["A. Greenium", "B. Beryllium", "C. Oxygen", "D. Chlorine"], "answer": 'D'},
    {"question": "What was the first country to grant women the right to vote?", "options": ["A. USA", "B. New Zealand", "C. France", "D. Sweden"], "answer": 'B'},
]

random.shuffle(questions)

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

questions_no = len(questions)
if score <= 4:
    print(f"\n{score} / {questions_no}.\nKeep trying!")
elif score <= 8:
    print(f"\n{score} / {questions_no}.\nGood job!")
else:
    print(f"\n{score} / {questions_no}.\nYou're a quiz master!")
