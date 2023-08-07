"""
wimbledon.py

estimated time: 30 minutes
actual time:   minutes

Write a program to read this file, process the data and display processed information.

the champions and how many times they have won.
the countries of the champions in alphabetical order


"""


def main():

    filename = "wimbledon.csv"
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        players = []
        line = in_file.readline()[1:]
        for line in in_file:
            line = line.strip()
            parts = line.split(",")
            players.append([parts[1],parts[2]])
        
        players_dict = champions_input(players)    
        countries_list = count_countries(players)
                
        print_results(players_dict, countries_list)



    

# turn the list into a dictionary
def champions_input(players):
    players_dict = {}
    for player in players:
        if player[1] in players_dict:
            players_dict[player[1]] += 1
        else:
            players_dict[player[1]] = 1
        
    return players_dict

def count_countries(players):
    countries = []
    for player in players:
        if player[0] not in countries:
            countries.append(player[0])
    
    countries.sort()
    return countries


def print_results(players_dict, countries_list):
    print("Wimbledon champions")
    for player in players_dict:
        print("{}: {}".format(player, players_dict[player]))
    
    print("\nCountries of champions")
    print(','.join(countries_list))

    




main()