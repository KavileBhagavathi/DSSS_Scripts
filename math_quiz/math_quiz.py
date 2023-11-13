import random

def generate_random_number(min, max):
    """Returns a random integer between two specified integers"""
    return random.randint(min, max)

def generate_operation():
    """Randomly returns an arithmetical operator sign from a fixed list"""
    return random.choice(['+', '-', '*'])

def solver(first_number, second_number, arith_operation):
    """
    Function to return the calculated result of the arithmetic operation
    chosen by the user.
    """
    problem_string = f"{first_number} {arith_operation} {second_number}"
    if arith_operation == '+': 
        answer = first_number + second_number
    elif arith_operation == '-': 
        answer = first_number - second_number
    else: 
        answer = first_number * second_number
    return problem_string, answer

def math_quiz():
    user_points = 0
    total_questions = 10

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide "\
          "the correct answers.")

    for question_num in range(1,total_questions+1):
        
        first_number = generate_random_number(1, 10)
        second_number = generate_random_number(1, 10)
        arith_operation = generate_operation()

        PROBLEM, ANSWER = solver(first_number, second_number, arith_operation)
        print(f"\nQuestion {question_num}: {PROBLEM}")
        useranswer = input("Your answer: ")
        ###Try and except block to catch invalid user input###
        try:
            useranswer = int(useranswer)
            if useranswer == ANSWER: 
                print("Correct! You earned a point.")
                user_points = user_points + 1
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}.")
        except Exception as e:
            print(f"""
                  You entered a non-number string! Try again. 
                  Error Message: {e}
                  """)
    print(f"\nGame over! Your score is: {user_points}/{total_questions}")

if __name__ == "__main__":
    math_quiz()
