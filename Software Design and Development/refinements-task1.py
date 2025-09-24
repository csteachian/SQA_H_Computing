def initialize_quiz_data():
    """
    Step 1: Initialise quiz data
    Returns: questions[], answers[], correctAnswers[]
    """
    questions = [
        "What is the capital of France?",
        "Which planet is known as the Red Planet?",
        "What is 2 + 2?",
        "Who wrote 'Romeo and Juliet'?",
        "What is the largest mammal in the world?"
    ]
    
    answers = [
        ["A) London", "B) Berlin", "C) Paris", "D) Madrid"],
        ["A) Venus", "B) Mars", "C) Jupiter", "D) Saturn"],
        ["A) 3", "B) 4", "C) 5", "D) 6"],
        ["A) Charles Dickens", "B) William Shakespeare", "C) Jane Austen", "D) Mark Twain"],
        ["A) Elephant", "B) Blue Whale", "C) Giraffe", "D) Hippopotamus"]
    ]
    
    correct_answers = ["C", "B", "B", "B", "B"]
    
    return questions, answers, correct_answers

def start_quiz_and_get_player_name():
    """
    Step 2: Start quiz and get player name
    Returns: playerName
    """
    print("=" * 50)
    print("🎯 WELCOME TO THE MULTIPLE CHOICE QUIZ GAME! 🎯")
    print("=" * 50)
    print("Instructions:")
    print("- Answer each question by typing A, B, C, or D")
    print("- You'll get one point for each correct answer")
    print("- Good luck!")
    print("-" * 50)
    
    player_name = input("Please enter your name: ").strip()
    while not player_name:
        player_name = input("Name cannot be empty. Please enter your name: ").strip()
    
    print(f"\nHello {player_name}! Let's start the quiz!\n")
    return player_name

def present_questions_and_collect_answers(questions, answers):
    """
    Step 3: Present questions and collect answers
    Input: questions[], answers[]
    Returns: playerAnswers[]
    """
    player_answers = []
    
    for i in range(len(questions)):
        print(f"Question {i + 1}: {questions[i]}")
        
        # Display answer options
        for answer_option in answers[i]:
            print(f"  {answer_option}")
        
        # Get player's answer
        while True:
            player_answer = input("\nYour answer (A/B/C/D): ").strip().upper()
            if player_answer in ["A", "B", "C", "D"]:
                player_answers.append(player_answer)
                break
            else:
                print("Invalid input! Please enter A, B, C, or D.")
        
        print("-" * 40)
    
    return player_answers

def calculate_score(player_answers, correct_answers):
    """
    Step 4: Calculate score
    Input: playerAnswers[], correctAnswers[]
    Returns: score
    """
    score = 0
    for i in range(len(player_answers)):
        if player_answers[i] == correct_answers[i]:
            score += 1
    
    return score

def display_final_result(player_name, score, total_questions, player_answers, correct_answers, questions):
    """
    Step 5: Display final result
    Input: playerName, score
    """
    print("\n" + "=" * 50)
    print("🏆 QUIZ RESULTS 🏆")
    print("=" * 50)
    
    print(f"Player: {player_name}")
    print(f"Final Score: {score}/{total_questions}")
    
    # Calculate percentage
    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage:.1f}%")
    
    # Provide feedback based on score
    if percentage >= 80:
        print("🌟 Excellent work! You're a quiz master!")
    elif percentage >= 60:
        print("👍 Good job! Well done!")
    elif percentage >= 40:
        print("👌 Not bad! Keep practicing!")
    else:
        print("📚 Keep studying and try again!")
    
    # Show detailed results
    print("\n" + "-" * 50)
    print("DETAILED RESULTS:")
    print("-" * 50)
    
    for i in range(len(questions)):
        status = "✅ Correct" if player_answers[i] == correct_answers[i] else "❌ Wrong"
        print(f"Q{i+1}: Your answer: {player_answers[i]} | Correct: {correct_answers[i]} | {status}")
    
    print("\nThank you for playing! 🎮🍕")

def main():
    """
    Main program function that orchestrates all steps
    """
    # Step 1: Initialize quiz data
    questions, answers, correct_answers = initialize_quiz_data()
    
    # Step 2: Start quiz and get player name
    player_name = start_quiz_and_get_player_name()
    
    # Step 3: Present questions and collect answers
    player_answers = present_questions_and_collect_answers(questions, answers)
    
    # Step 4: Calculate score
    score = calculate_score(player_answers, correct_answers)
    
    # Step 5: Display final result
    display_final_result(player_name, score, len(questions), player_answers, correct_answers, questions)

# Run the quiz game
if __name__ == "__main__":
    main()
