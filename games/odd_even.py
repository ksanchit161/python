import random

def odd_even_game():
    print("Welcome to Odd-Even Bat Ball Game!")
    print("Rules:")
    print("1. You and computer will choose a number between 1 and 6.")
    print("2. If total is EVEN and you chose EVEN, you win toss. Otherwise computer wins.")
    print("3. Toss winner decides to BAT or BALL first.")
    print("4. In batting, runs are added until both choose same number (OUT!).")
    print("-" * 40)

    # Toss
    user_choice = input("Choose Odd or Even: ").strip().lower()
    user_num = int(input("Enter your number (1-6): "))
    comp_num = random.randint(1, 6)
    total = user_num + comp_num
    
    print(f"Computer chose: {comp_num}, Total = {total}")
    
    if (total % 2 == 0 and user_choice == "even") or (total % 2 == 1 and user_choice == "odd"):
        print("You won the toss!")
        decision = input("Do you want to BAT or BALL first? ").strip().lower()
        user_bats_first = decision == "bat"
    else:
        print("Computer won the toss!")
        comp_choice = random.choice(["bat", "ball"])
        print(f"Computer chose to {comp_choice} first.")
        user_bats_first = (comp_choice == "ball")

    # Function to play innings
    def play_innings(batting_first=True):
        score = 0
        while True:
            user_num = int(input("Enter your number (1-6): "))
            comp_num = random.randint(1, 6)
            print(f"Computer chose: {comp_num}")
            if user_num == comp_num:
                print("OUT!")
                break
            if batting_first:
                score += user_num
            else:
                score += comp_num
            print(f"Score: {score}")
        return score

    # First Innings
    if user_bats_first:
        print("\nYou are Batting first!")
        user_score = play_innings(batting_first=True)
        print(f"Your total score: {user_score}\n")
        
        print("Computer is Batting now!")
        comp_score = 0
        while comp_score <= user_score:
            user_num = int(input("Enter your number (1-6): "))
            comp_num = random.randint(1, 6)
            print(f"Computer chose: {comp_num}")
            if user_num == comp_num:
                print("Computer OUT!")
                break
            comp_score += comp_num
            print(f"Computer Score: {comp_score}")
        
        print(f"Computer total: {comp_score}")
        if comp_score > user_score:
            print("Computer Wins!")
        elif comp_score < user_score:
            print("You Win!")
        else:
            print("Match Tied!")

    else:
        print("\nComputer is Batting first!")
        comp_score = 0
        while True:
            user_num = int(input("Enter your number (1-6): "))
            comp_num = random.randint(1, 6)
            print(f"Computer chose: {comp_num}")
            if user_num == comp_num:
                print("Computer OUT!")
                break
            comp_score += comp_num
            print(f"Computer Score: {comp_score}")
        print(f"Computer total: {comp_score}\n")

        print("You are Batting now!")
        user_score = 0
        while user_score <= comp_score:
            user_num = int(input("Enter your number (1-6): "))
            comp_num = random.randint(1, 6)
            print(f"Computer chose: {comp_num}")
            if user_num == comp_num:
                print("OUT!")
                break
            user_score += user_num
            print(f"Your Score: {user_score}")
        
        print(f"Your total: {user_score}")
        if user_score > comp_score:
            print("You Win!")
        elif user_score < comp_score:
            print("Computer Wins!")
        else:
            print("Match Tied!")

# Run game
odd_even_game()
