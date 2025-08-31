import random

def get_user_guess():
    """Get a valid integer guess from  the user within the range 1-100."""
    while True:
        guess=input("Enter your guess(1-100):  ").strip()
        if not guess.isdigit():
            print("⚠️ Invalid input! Please enter a number.")
            continue
        
        guess = int(guess)
        if 1 <=guess <=100:
            return guess
        else:
            print("⚠️ Please enter a number between 1 and 100.")
            
def play_game():
    """"Run one round of the number between 1 and 100."""
    number = random.randint(1, 100)
    attempts = 0
    
    print("\n🎲 I have picked a number between 1 and 100. Can you guess it?")
    
    while True:
        guess = get_user_guess()
        attempts += 1
        
        if guess < number:
            print("📉 Too low! Try again.")
        elif guess > number:
            print("📈 Too high! Try again.")
        else:
            print(f"✅ Correct! The number was {number}.")
            print(f"🎉 You guessed it in {attempts} attempts.\n")
            return attempts
         
def main():
    """Main game loop with replay and high score tracking."""
    print("===🎮 Welcome to the Number Guessing Game🎮===")
    best_score = None
    
    while True:
        attempts = play_game()
        
        # Track high score
        if best_score is None or attempts < best_score:
            best_score =attempts
            print(f"🎖️ New High Score! Best attempts: {best_score}\n")
            
        # Ask if user wants to play again
        play_again = input("🔁 Do you want to play again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\n👋 Thanks for playing! Goodbye!")
            break
        
if __name__=="__main__":
    main()

    
        
        
    
