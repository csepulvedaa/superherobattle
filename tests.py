"""
Unit tests for Methods And Classes .

Access Token Needed for running this tests.
Author: Cristobal Sepúlveda
2021
"""

import unittest
import numpy as np
from logic import Team

ACCESS_TOKEN = 10225038964217338

class CharacterTest(unittest.TestCase):
    """Character Class Test

    """
    def test_create_character(self):
        """We create a character and manually set the random values (AS y FB)
        This is for checking that the base stats are calculated without errors
        In this test we set stamina as 5 and Filliation Coeficient as 10
        asuming that the team has the same aligment that spiderman.
        The values are calculated by hand using the Base Stats formula
        health_points is calculated with the strenght,durability
        and power calculated with the base stats formula
        """
        team=Team([620],ACCESS_TOKEN)
        spiderman = team.character_list[0]
        spiderman.actual_stamina=5
        spiderman.filiation_coeficient=10
        self.assertEqual(spiderman.name,'Spider-Man',
            "It shold be named Spider-Man")
        self.assertEqual(spiderman.aligment,'good',
            "Spiderman aligment is good")
        self.assertEqual(spiderman.team_aligment,'good',
            msg="There's only one good member in team => Team good")
        self.assertEqual(spiderman.actual_stamina,5,"The AS Should Have Changed")
        self.assertEqual(spiderman.filiation_coeficient,10,"The FB Should Have Changed")
        self.assertAlmostEqual(spiderman.intelligence, 1681.8181818181816,
            msg="It should have an intelligence boost")
        self.assertAlmostEqual(spiderman.strength,1045.4545454545453,
            msg="It should have a strength boost")
        self.assertAlmostEqual(spiderman.speed,1263.6363636363635,
            msg="It should have a speed boost")
        self.assertAlmostEqual(spiderman.durability,1409.090909090909,
            msg="It should have a durability boost")
        self.assertAlmostEqual(spiderman.power,1390.909090909091,
            msg="It should have a power boost")
        self.assertAlmostEqual(spiderman.combat,1590.9090909090905,
            msg="It should have a durability boost")
        self.assertAlmostEqual(spiderman.health_points,2510.2272727272725,
            msg="It shouldCalculate New health_points with the new Stats")
        self.assertAlmostEqual(spiderman.current_damage,0,
            msg="health_points==current_damage at beggining")
    def test_mental_attack(self):
        """Test if Damage == Mental Attack Rate.
        First Attack is over 15.000 because of the high filiation Coeficient
        Second attack is less than 10 because of the low filiation Coeficient (11^-1)
        """
        team=Team([620,619,225],ACCESS_TOKEN)
        spiderman = team.character_list[0]
        dr_octopus = team.character_list[1]
        spider_gwen = team.character_list[2]
        spiderman.filiation_coeficient=10
        spiderman.actual_stamina=5

        spiderman.attack1(dr_octopus)
        spiderman.filiation_coeficient=(1+10)**-1
        spiderman.attack1(spider_gwen)

        self.assertAlmostEqual(dr_octopus.current_damage, 15890.909090909088,
            msg="Damage taken == (Intelligence * 0,2 + speed *0.2 + combat * 0.1 )*FB ")
        self.assertAlmostEqual(spider_gwen.current_damage,1.3132982719759576,
            msg="Damage taken == (Intelligence * 0,2 + speed *0.2 + combat * 0.1 )*FB ")

    def test_strong_attack(self):
        """Test if Damage == Strong Attack Rate.
    First Attack is over 10.000 because of the high filiation Coeficient
    Second attack is less than 10 because of the low filiation Coeficient (11^-1)
    """
        team=Team([620,299,346],ACCESS_TOKEN)
        spiderman = team.character_list[0]
        green_goblin = team.character_list[1]
        iron_man = team.character_list[2]
        spiderman.actual_stamina=5
        spiderman.filiation_coeficient=10
        spiderman.attack2(green_goblin)
        spiderman.filiation_coeficient=(1+10)**-1
        spiderman.attack2(iron_man)
        self.assertAlmostEqual(green_goblin.current_damage, 12236.363636363636,
            msg="Damage taken == (strength * 0,6 + power *0.2 + combat * 0.2 )*FB ")
        self.assertAlmostEqual(iron_man.current_damage,1.0112697220135236,
            msg="Damage taken == (strength * 0,6 + power *0.2 + combat * 0.2 )*FB  ")
    def test_fast_attack(self):
        """Test if Damage == Fast Attack Rate.
    First Attack is over 10.000 because of the high filiation Coeficient
    Second attack is less than 10 because of the low filiation Coeficient (11^-1)
    """
        team=Team([620,687,618],ACCESS_TOKEN)
        spiderman = team.character_list[0]
        venom = team.character_list[1]
        spider_girl = team.character_list[2]
        spiderman.actual_stamina=5
        spiderman.filiation_coeficient=10
        spiderman.attack3(venom)
        spiderman.filiation_coeficient=(1+10)**-1
        spiderman.attack3(spider_girl)
        self.assertAlmostEqual(venom.current_damage, 12563.636363636362,
            msg="Damage taken == (speed * 0.55 + durability *0.25 + strength * 0.2 )*FB ")
        self.assertAlmostEqual(spider_girl.current_damage,1.0383170548459804,
            msg="Damage taken == (speed * 0.55 + durability *0.25 + strength * 0.2)*FB  ")
    def test_alive(self):
        """Test if character status changes after a random attack over 10.000
        """
        team=Team([620,687,618],ACCESS_TOKEN)
        spiderman = team.character_list[0]
        venom = team.character_list[1]
        spiderman.actual_stamina=5
        spiderman.filiation_coeficient=10
        spiderman.attack(venom)

        self.assertEqual(venom.is_alive,False,"Venom is out of combat")
        self.assertEqual(spiderman.is_alive,True,"Spiderman Is Alive")


class TeamTest(unittest.TestCase):
    """Team Class Test

    """
    def testTeamAligment(self):
        """
        Checks if team aligment it's correctly setted
        good and bad are ID arrays of good aligment heroes and bad aligment villians.
        """
        good = np.array([687,332,346,313,659])
        bad = np.array([149,639,680,370,374])

        good_team=Team(good,ACCESS_TOKEN)
        bad_team=Team(bad,ACCESS_TOKEN)

        self.assertEqual(good_team.aligment,'good',msg="Team Aligment Should Be good")
        self.assertEqual(bad_team.aligment,'bad',msg="Team Aligment Should Be good")

    def test_team_status(self):
        """Sets some characters as is_alive = False and checks if team status change
        """
        good = np.array([687,332,346,313,659])
        good_team=Team(good,ACCESS_TOKEN)
        for i in range(0,5):
            good_team.character_list[i].is_alive=False
        good_team.get_alive_heroes()
        good_team.print_alive_heroes()
        self.assertEqual(len(good_team.character_list),0,"Should be no characters on the list")

    def test_team_batteling(self):
        """Test the status of the team during the battle
        Both teams should be able to battle at first.
        Then, good_team will attack bad_team until bad_team is not batteling
        """
        good = np.array([687,332,346,313,659])
        bad = np.array([149,639,680,370,374])

        good_team=Team(good,ACCESS_TOKEN)
        bad_team=Team(bad,ACCESS_TOKEN)

        self.assertEqual(good_team.batteling,True,msg="Team should be able to battle")
        self.assertEqual(bad_team.batteling,True,msg="Team should be able to battle")
        while good_team.batteling and bad_team.batteling:
            good_team.attack_team(bad_team)
        self.assertEqual(good_team.batteling,True,msg="Team should be able to battle")
        self.assertEqual(bad_team.batteling,False,msg="Team shouldn't be able to battle")

        bad_team=Team(bad,ACCESS_TOKEN)
        self.assertEqual(bad_team.batteling,True,msg="Team should be able to battle")
        while good_team.batteling and bad_team.batteling:
            bad_team.attack_team(good_team)
        self.assertEqual(bad_team.batteling,True,msg="Team should be able to battle")
        self.assertEqual(good_team.batteling,False,msg="Team shouldn't be able to battle")

if __name__ == '__main__':
    unittest.main()