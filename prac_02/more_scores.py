"""

"""
# Ask the user for a number of scores
def get_number_of_scores():
    number_of_scores = int(input("Enter number of scores: "))
    while number_of_scores < 0:
        print("Invalid number of scores")
        number_of_scores = int(input("Enter number of scores: "))
    return number_of_scores

# Generate that many random numbers (scores) between 0 and 100 inclusive
def generate_random_scores(number_of_scores):
    import random
    scores = []
    for i in range(number_of_scores):
        scores.append(random.randint(0, 100))
    return scores
# verify the score
def verified_score(score):
    if score < 50:
        return "Bad"
    elif score > 90:
        return "Excellent"
    else:
        return "Passable"

# For each of those scores, write the "result" to a file called "results.txt" as below:
def write_results_to_file(scores):
    results_file = open("results.txt", "w")
    for score in scores:
        results_file.write(f"{score} is {verified_score(score)}\n")
    results_file.close()
