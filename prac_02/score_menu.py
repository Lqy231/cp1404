"""
In the lecture there was a "do this now" activity similar to this, so you can use what we did there to help with this program.

Write a complete Python program following the standard structure that uses a main and other functions.
Use a main menu following the standard menu pattern.

The menu should have four separate options:

(G)et a valid score (must be 0-100 inclusive)
(P)rint result (copy or import your function to determine the result from score.py)
(S)how stars (this should print as many stars as the score)
(Q)uit
Handle each of these (except quit) separately, and consider how you can reuse your functions. In main(), before the menu loop, get the valid score.
When the user quits, say some kind of "farewell".
"""


def get_valid_score():
    score = int(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score


def verified_score(score):
        
    while score < 0 or score > 100:
        print("Please enter a valid score first")
        score = get_valid_score()
    
    if score < 50:
        return "Bad"
    elif score > 90:
        return "Excellent"
    else:
        return "Passable"    
        
def show_stars(score):
    for i in range(score):
        print("*", end="")
    print()

def main():
    score = -1
    menu = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"
    print(menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
            
        elif choice == "P":
            print(f"your score is :{verified_score(score)}")
        
        elif choice == "S":

            while score < 0 or score > 100:
                print("Please enter a valid score first")
                score = get_valid_score()
            show_stars(score)
        
        else:
            print("Invalid choice")
        print(menu)
        choice = input(">>> ").upper()
    print("Farewell")


main()
