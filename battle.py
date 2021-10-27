"""
Battle Script
Usage:
 "python battle.py [AccessToken]"

Author : Cristobal Sepulveda
2021
"""
import sys
import time
import numpy as np
from colorama import Fore, Style, init
from logic import Team



def choose_winner(team_a, team_b):
    """Method for choosing the winner team

    Args:
        team_a (team): Batteling Team
        team_b (team): Batteling Team
    """
    if len(team_a.character_list)>len(team_b.character_list):
        print(Fore.GREEN+Style.BRIGHT+"Team A Wins.")
    else:
        print(Fore.GREEN+Style.BRIGHT+"Team B Wins.")



def battle(team_a,team_b):
    """
    Battle between 2 teams
    While both teams can battle, randomly one of both teams attack the other.
    The character that attack and the character attacked also is randomly selected
    between the ones that can battle.

    Args:
        team_a (Team): Team to battle
        team_b (Team): Team to battle
    """
    i=1
    while team_b.batteling and team_a.batteling:
        time.sleep(3)
        print(f"{'-'*40}")
        print(Style.BRIGHT+"SuperHero / Villian Status: Team A ")
        team_a.print_alive_heroes()
        print(f"{'-'*40}")
        print(Style.BRIGHT+"SuperHero / Villian Status: Team B")
        team_b.print_alive_heroes()

        time.sleep(3)

        k = np.random.randint(1,3)
        if k==1:
            print(f"{'-'*40}")
            print(Style.BRIGHT+Fore.CYAN+"Battle Turn " +str(i)+" Team A attacks-> Team B")
            print(f"{'-'*40}")
            team_a.attack_team(team_b)
            team_b.attack_team(team_a)
        elif k==2:
            print(f"{'-'*40}")
            print(Style.BRIGHT+Fore.CYAN+"Battle Turn "+str(i)+" Team B attacks -> Team A")
            print(f"{'-'*40}")
            team_b.attack_team(team_a)
            team_a.attack_team(team_b)


        i=i+1

    choose_winner(team_a, team_b)

def buildTeams(access):
    """
    Generate Random unique SuperHeroes and Villians for the battle

    Args:
        access (int): SuperHeroApi Access Token

    Returns:
        [team,team]: Team A and team B
    """
    unique_ints = np.random.choice(732, 10)
    print("Building Team A")
    first_team = Team(unique_ints[:5],access)
    print("Building Team B")
    second_team= Team(unique_ints[-5:],access)
    return first_team,second_team

if len(sys.argv) < 2:
    print("SuperHero Battle Using SuperHero Api")
    print(f"Uso: {sys.argv[0]} [AcessToken]")
    sys.exit(1)

init(autoreset=True)

access_token = sys.argv[1]
a,b = buildTeams(access_token)
battle(a,b)
