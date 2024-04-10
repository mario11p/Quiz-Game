# Quiz Game in Python

def get_questions():
    # Returns a list of questions and answers
    return [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "Which planet is known as the Red Planet?", "answer": "Mars"},
        {"question": "What is the smallest prime number?", "answer": "2"},
        {"question": "In which year did the Titanic sink?", "answer": "1912"},
        {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"}
    ]

def play_quiz(questions):
    score = 0
    for question in questions:
        user_answer = input(question["question"] + " ")
        if user_answer.lower() == question["answer"].lower():
            print("Correct!")
            score += 1
        else:
            print("Wrong! The correct answer is:", question["answer"])
    print(f"Your final score is: {score}/{len(questions)}")

def main():
    print("Welcome to the Quiz Game!")
    questions = get_questions()
    play_quiz(questions)
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
