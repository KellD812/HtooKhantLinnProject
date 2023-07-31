import time

print("This is a simple quiz game made by Htoo Khant Linn.")
time.sleep(1)
print("Do you want to play?")
time.sleep(0.5)
playing = input("Type Yes (or) No\n:").lower()
time.sleep(0.5)

if playing != "yes":
    quit()

print("Okay, let's play.")

question = ('Which planet is known as the "Red Planet"?',
            "What is the tallest mountain in the world?",
            "What is the largest mammal on Earth?",
            "What is the largest organ in the human body?",
            "What is the chemical symbol for potassium?",
            "What does Tr, Will usually wears?",
            "When is Tr, Will birthday?")

options = (("A. Mars", "B. Venus", "C. Jupiter", "D. Neptune"),
           ("A. Kangchenjunga", "B. Mount Godwin-Austen", "C. Mount Everest", "D. Annapurna"),
           ("A. Elephant", "B. Giraffe", "C. Great White Shark", "D. Blue Whale"),
           ("A. Heart", "B. Liver", "C. Lungs", "D. Skin"),
           ("A. Fe", "B. K", "C. H₂O", "D. Cu"),
           ("A. White Tikepone", "B. Swimsuit", "C. Black Lonekyi", "D. Spongebob underwear"),
           ("A. 1997", "B. 1996", "C. 1999", "D. 1998"))

answers = ("A", "C", "D", "D", "B", "A", "C")
question_number = 0
guesses = []
score = 0

time.sleep(1)
for x in question:
    print("---------------------------------------")
    print(x)
    for y in options[question_number]:
        print(y)
    guess = input("Enter A (or) B (or) C (or) D\n:").upper()
    guesses.append(guess)
    if guess == answers[question_number]:
        print("You are CORRECT!")
        score += 1
    else:
        print("You are INCORRECT!")
        time.sleep(1)
        print(f"{answers[question_number]} is the right answer.")
    question_number += 1

time.sleep(1)
print("-------------------------------")
print("           RESULTS             ")
print("-------------------------------")

time.sleep(1)

print("Correct Answers: ", end="")
for y in answers:
    print(y, end=", ")
print()

print("Your Answers: ", end="")
for a in guesses:
    print(a, end=", ")
print()

score = int(score / len(question) * 100)
printi(f"Your score is: {score}%")
time.sleep(1)
print("There will be more projects in the future! :)")
time.sleep(0.5)
print("You can exit the window now or, the program will automatically exit in 30 seconds.")
time.sleep(30)
