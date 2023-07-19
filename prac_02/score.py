"""
CP1404/CP5632 - Practical
Broken program to determine score status

get score
print

"""
def get_valid_score():
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def verified_score(score):

    if score < 50:
        return "Bad"
    elif score > 90:
        return "Excellent"
    else:
        return "Passable"


def main():
    
    score = get_valid_score()
    print(f"your score is :{verified_score(score)}")

    # add a new part to the bottom of your main function that generates a random score and prints the result.
    import random
    random_score = random.randint(0, 100)
    print(f"random score is :{random_score}")
    print(f"random score result is: {verified_score(score)}")


main()
    
