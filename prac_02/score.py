import random

def main():
    user_input_score = int(input("Please enter your score: "))
    user_result = get_score_result(user_input_score)
    print(f"Result for your entered score: {user_result}")
    random_score = random.randint(0, 100)
    random_result = get_score_result(random_score)
    print(f"Result for randomly generated score {random_score}: {random_result}")

def get_score_result(score):
    if score >= 90:
        return "A (Excellent)"
    elif score >= 80:
        return "B (Good)"
    elif score >= 70:
        return "C (Average)"
    elif score >= 60:
        return "D (Pass)"
    else:
        return "F (Fail)"

main()