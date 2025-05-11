import random

EMOJIS = {
    "Rock": "🪨",
    "Paper": "📄",
    "Scissors": "✂️"
}

WIN_RULES = {
    "Rock": "Scissors",
    "Paper": "Rock",
    "Scissors": "Paper"
}

CHOICES = {
    1: "Rock",
    2: "Paper",
    3: "Scissors"
}

def print_rules():
    print("\n🎮 Welcome to Rock-Paper-Scissors Showdown! 🎮")
    print("Winning rules:")
    for winner, loser in WIN_RULES.items():
        print(f" - {winner} beats {loser}")
    print()

def get_user_choice():
    print("\nMake your move:")
    for key, val in CHOICES.items():
        print(f" {key}. {val} {EMOJIS[val]}")
    try:
        user_input = int(input("Your choice (1-3): "))
        if user_input not in CHOICES:
            raise ValueError
        return CHOICES[user_input]
    except ValueError:
        print("❌ Invalid choice! Please enter 1, 2, or 3.")
        return get_user_choice()

def get_computer_choice():
    return CHOICES[random.randint(1, 3)]

def determine_winner(user, computer):
    if user == computer:
        return "Draw"
    elif WIN_RULES[user] == computer:
        return "User"
    else:
        return "Computer"

def play_game():
    user_score = 0
    comp_score = 0
    rounds_played = 0

    print_rules()

    while True:
        user_choice = get_user_choice()
        comp_choice = get_computer_choice()

        print(f"\n🧑 You chose: {user_choice} {EMOJIS[user_choice]}")
        print(f"🤖 Computer chose: {comp_choice} {EMOJIS[comp_choice]}")

        result = determine_winner(user_choice, comp_choice)
        rounds_played += 1

        if result == "Draw":
            print("🔁 It's a tie!")
        elif result == "User":
            print("✅ You win this round!")
            user_score += 1
        else:
            print("❌ Computer wins this round!")
            comp_score += 1

        print(f"🏁 Score => You: {user_score} | Computer: {comp_score} | Rounds Played: {rounds_played}")
        
        play_again = input("\nPlay again? (Y/N): ").strip().lower()
        if play_again != 'y':
            break

    print("\n🎉 Thanks for playing Rock-Paper-Scissors Showdown!")
    print(f"Final Score => You: {user_score} | Computer: {comp_score} | Rounds: {rounds_played}")
    if user_score > comp_score:
        print("🏆 You are the overall winner!")
    elif user_score < comp_score:
        print("🤖 Computer takes the crown!")
    else:
        print("🔔 It's an overall draw!")

if __name__ == "__main__":
    play_game()
