from score import get_score_result
def main():
    current_score = get_valid_score()
    print(f"Initial score: {current_score}")
    display_menu()
    choice = input("Enter your choice: ").lower()
    program_running = True
    while program_running:
        if choice == "q":
            program_running = False
        elif choice == "g":
            current_score = get_valid_score()
            print(f"Score updated to: {current_score}")
        elif choice == "p":
            result = get_score_result(current_score)
            print(f"Result: {result}")
        elif choice == "s":
            print_stars(current_score)
        else:
            print("Invalid choice! Please try again.")
        if program_running:
            display_menu()
            choice = input("Enter your choice: ").lower()
    print("Thank you for using the score menu! Goodbye.")

def get_valid_score():
    valid_input = False
    score = 0
    while not valid_input:
        try:
            score = int(input("Enter a score (0-100): "))
            if 0 <= score <= 100:
                valid_input = True
            else:
                print("Invalid score! Must be between 0 and 100.")
        except ValueError:
            print("Invalid input! Please enter a number.")
    return score

def print_stars(score):
    print("*" * score)

def display_menu():
    print("\nScore Menu")
    print("(G)et a valid score (0-100 inclusive)")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")
main()
