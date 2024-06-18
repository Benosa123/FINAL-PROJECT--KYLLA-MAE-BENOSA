questions = {
    "What is the capital of France?": "Paris",
    "What is 2 + 2?": "4",
    "What is the capital of Germany?": "Berlin"
}

def interactive_quiz():
    score = 0

    for question, answer in questions.items():
        user_answer = input(question + " ").strip().lower()
        if user_answer == answer.lower():
            score += 1
            print("Correct!")
        else:
            print(f"Wrong! The correct answer is {answer}.")

    print(f"Final score: {score}/{len(questions)}")

interactive_quiz()
