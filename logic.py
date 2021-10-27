import requests
import numpy as np
from colorama import Fore, Style

URL = "https://superheroapi.com/api/10225038964217338/200"


class Character:
    """
    Contains the methods and stats to represent a hero or villain of a team.
    The filiation coeficient variable is a bonus
    if the character has the same alignment as his team, otherwise it is a penalty.
    The stamina variable is a randomly generated variable between 1 and 10,
    which is a constant in the result of the base stats.
    The variable is_alive indicates if the character is available to fight or not
    if  it's false the character is not available in the list of available characters to attack.
    """

    def __init__(
            self, name, aligment, intelligence, strength, speed, durability, power, combat):
        """
        Contructor method for Character Class
        Args:
            name (string): Name of the Hero/Villian
            aligment (string): Aligment of the Hero/Villian
            intelligence (string): Intelligence of the Hero/Villian
            strength (string): Strength of the Hero/Villian
            speed (string): Speed of the Hero/Villian
            durability (string): Durability of the Hero/Villian
            power (string): Power of the Hero/Villian
            combat (string): Combat of the Hero/Villian
        """
        self.__name = name
        self.__filiation_coeficient = 1
        self.__actual_stamina = np.random.randint(0, 11)
        self.__intelligence = 0 if intelligence == 'null' else float(
            intelligence)
        self.__strength = 0 if strength == 'null' else float(strength)
        self.__speed = 0 if speed == 'null' else float(speed)
        self.__durability = 0 if durability == 'null' else float(durability)
        self.__power = 0 if power == 'null' else float(power)
        self.__combat = 0 if combat == 'null' else float(combat)
        self.__aligment = aligment
        self.__team_aligment = 'neutral'
        self.__is_alive = True
        self.__current_damage = 0

    @property
    def name(self):
        """Name Property

        Returns:
            string: Character Name
        """
        return self.__name

    @property
    def aligment(self):
        """Aligment Property

        Returns:
            string: Character Aligment
        """
        return self.__aligment

    @property
    def health_points(self):
        """health_points property getter

        Returns:
            float: health_points Calculed by given formula
        """

        return (self.strength*0.8+self.durability*0.7+self.power)*(0.5)*(1+(self.actual_stamina/10))+100

    @property
    def current_damage(self):
        """ Current Damage Property

        Returns:
            float: current damage taken
        """
        return self.__current_damage

    @current_damage.setter
    def current_damage(self, value):
        """Setter for Current Damage

        Args:
            value (float): New value for current damage
        """
        self.__current_damage = value

    @property
    def intelligence(self):
        """Ingelligence Property

        Returns:
            float: Intelligence Calculated by formula
        """
        return ((2*self.__intelligence+self.__actual_stamina)/1.1)*self.__filiation_coeficient

    @property
    def strength(self):
        """Strenght Property

        Returns:
            float: Strenght Calculated by formula
        """
        return ((2*self.__strength+self.__actual_stamina)/1.1)*self.__filiation_coeficient

    @property
    def power(self):
        """Power Property

        Returns:
            float: Power Calculated by formula
        """
        return ((2*self.__power+self.__actual_stamina)/1.1)*self.__filiation_coeficient

    @property
    def speed(self):
        """Speed Property

        Returns:
            float: Speed Calculated by formula
        """
        return ((2*self.__speed+self.__actual_stamina)/1.1)*self.__filiation_coeficient

    @property
    def durability(self):
        """Durability Property

        Returns:
            float: Durability Calculated by formula
        """
        return ((2*self.__durability+self.__actual_stamina)/1.1)*self.__filiation_coeficient

    @property
    def combat(self):
        """Combat Property

        Returns:
            float: Combat Calculated by formula
        """
        return ((2*self.__combat+self.__actual_stamina)/1.1)*self.__filiation_coeficient

    @property
    def actual_stamina(self):
        """Stamina Property

        Returns:
            float: returns Stamina, randomly calculated
        """
        return self.__actual_stamina

    @actual_stamina.setter
    def actual_stamina(self, stamina):
        """Stamina Setter
        Stamina variable setter for testing purposes
        Args:
            stamina (float): Stamina Value
        """
        self.__actual_stamina = stamina

    @property
    def team_aligment(self):
        """Team Aligment Property

        Returns:
            string: Returns Team Aligment 'good' or 'bad'
        """
        return self.__team_aligment

    @team_aligment.setter
    def team_aligment(self, aligment):
        """Team Aligment Setter
            Setter for Team Aligment
        Args:
            aligment (string): New Value for Team Aligment
        """
        self.__team_aligment = aligment

    @property
    def is_alive(self):
        """Is Alive Property

        Returns:
            boolean: True if Character is alive, False if not
        """
        return self.__is_alive

    @is_alive.setter
    def is_alive(self, value):
        """Is Alive Setter
            Setter for Is Alive Value
        Args:
            value (boolean): New Value for is_alive
        """
        self.__is_alive = value

    @property
    def filiation_coeficient(self):
        """Filiaton Coeficient Property

        Returns:
            float: Filiaton Coeficient calculated by team aligment
        """
        return self.__filiation_coeficient

    @filiation_coeficient.setter
    def filiation_coeficient(self, coeficient):
        """Filation Coeficient Setter

        Args:
            coeficient (float): New Value for Filiaton Coeficient
        """
        self.__filiation_coeficient = coeficient

    def attack(self, character):
        """ Method for Attacking a Character
        Attack type is randomly select bettween
        Mental Attack, Strong Attack or Fast Attack
        If the attacked character recieved damage is more
        than their Health points, the attacked character is out of combat
        Args:
            character (Character): Atacked Character
        """
        i = np.random.randint(1, 4)

        attack_type = 'attack'+str(i)

        attack_method = getattr(self, attack_type, lambda: 'Invalid')

        attack_method(character)

        if character.current_damage >= character.health_points:
            character.is_alive = False
            print(character.name+ Fore.RED+ " Fainted")

    def attack1(self, character):
        """Metal Attack
        Mental Attack rate is calculated by given formula,
        then it's added to the attacked character current damage
        Args:
            character (Character): Atacked Character
        """
        print("> "+self.name +" Attacks " + str(character.name)+" With a "+Style.BRIGHT+Fore.YELLOW+"Mental Attack")

        mental_attack_rate = (
            self.intelligence*0.7+self.speed*0.2+self.combat*0.1)*self.filiation_coeficient

        print(">> "+str(character.name)+" Took " + str(round(mental_attack_rate,3))+ " Damage")

        character.current_damage = character.current_damage+mental_attack_rate

    def attack2(self, character):
        """Strong Attack
        Strong Attack rate is calculated by given formula,
        then it's added to the attacked character current damage
        Args:
            character (Character): Atacked Character
        """
        print("> "+self.name +" Attacks " + str(character.name)+" With a "+Style.BRIGHT+Fore.BLUE+"Strong Attack")

        strong_attack_rate = (self.strength*0.6+self.power *
                              0.2+self.combat*0.2)*self.filiation_coeficient

        print(">> "+str(character.name)+" Took " + str(round(strong_attack_rate,3))+ " Damage")

        character.current_damage = character.current_damage+strong_attack_rate

    def attack3(self, character):
        """Fast Attack
        Fast Attack rate is calculated by given formula
        then it's added to the attacked character current damage
        Args:
            character (Character): Atacked Character
        """
        print("> "+self.name +" Attacks " + str(character.name)+" With a "+Style.BRIGHT+Fore.MAGENTA+"Fast Attack")

        fast_attack_rate = (self.speed*0.55+self.durability *
                            0.25+self.strength*0.2)*self.filiation_coeficient

        print(">> "+str(character.name)+" Took " + str(round(fast_attack_rate,3))+ " Damage")

        character.current_damage = character.current_damage+fast_attack_rate


class Team:
    """Team Class
    Contains the methods and instance variables to represent a team.
    The character_list variable is a Character object array
    containing the heroes belonging to the team.
    The variable aligment contains the alignment of the team.
    The boolean variable batteling contains the team state,
    if there's no Characters available to fight it's setted to False.
    The Access Token is requiered to consume the data from the API.
    """

    def __init__(self, id_list, access_token):
        """Constructor of the Team Class

        Args:
            idList (array[int]): List of Characters Id
            access_token (int): SuperHeroApi Access Token
        """
        self.access_token = access_token
        self.character_list = np.array([])
        self.get_character_list(id_list)
        self.__aligment = self.calculate_aligment()
        self.set_team_aligment(self.aligment)
        self.batteling = True

    def create_character(self, character_id):
        """ Creates a Character of given ID
        This method consumes the API response and
        creates a Character from the received data
        Args:
            character_id (int): Hero or Villian ID

        Returns:
            Character: The character with calculated stats
        """
        url = "https://superheroapi.com/api/" + \
            str(self.access_token)+"/"+str(character_id)
        response = requests.get(url)
        hero = response.json()
        character = Character(
            hero['name'],
            hero['biography']['alignment'],
            hero['powerstats']['intelligence'],
            hero['powerstats']['strength'],
            hero['powerstats']['speed'],
            hero['powerstats']['durability'],
            hero['powerstats']['power'],
            hero['powerstats']['combat'])
        return character

    def get_character_list(self, id_list):
        """ Obtains the Characters List
        For every character_id in the id_list creates a character and
        added to the Team's characters_list

        Args:
            idList (array[int]): idList (array[int]): List of Characters Id
        """
        for character_id in id_list:
            charater = self.create_character(character_id)
            self.character_list = np.append(self.character_list, charater)

    def get_alive_heroes(self):
        """Checks the status of the characters in charachters list.
            If the character can't battle anymore, it's removed from the list
        """
        for charater in self.character_list:
            if not charater.is_alive:
                index = np.argwhere(self.character_list == charater)
                self.character_list = np.delete(self.character_list, index)

    def print_alive_heroes(self):
        """ Print the actual characters list"""
        self.get_alive_heroes()
        if len(self.character_list)==0:
            print(Style.BRIGHT+Fore.RED+"No one left to battle")
        for charater in self.character_list:
            print(Fore.GREEN+Style.BRIGHT+" Alive : "+Fore.WHITE+Style.NORMAL+charater.name)

    def set_team_aligment(self, aligment):
        """Sets Filiation Coeficient for every member of the team
        If the Character's aligment is the same of the team, it's a bonus
        If not, it's a penalty.
        It the character's aligment is neutral remains as 1.

        Args:
            aligment (string): Team Aligment
        """
        for charater in self.character_list:
            charater.team_aligment = aligment
            if charater.aligment == aligment:
                charater.filiation_coeficient = 1+np.random.randint(0, 11)
            elif charater.aligment == 'neutral':
                charater.filiation_coeficient = 1
            else:
                charater.filiation_coeficient = (
                    1+np.random.randint(0, 11))**-1

    def calculate_aligment(self):
        """ Calculates the team aligment with a point system.
        The team starts with 0 aligments points points.
        For every member in characters_list, if the member aligment is good adds 1 point.
        If the member aligment is bad substracts 1 point.
        If the aligment points >0 the team is good, else the team it's bad
        Returns:
            string: Team Aligment
        """
        aligment_points = 0
        for hero in self.character_list:
            if hero.aligment == 'good':
                aligment_points += 1
            elif hero.aligment == 'bad':
                aligment_points += -1
            else:
                aligment_points += 0
        return 'good' if aligment_points > 0 else 'bad'

    @property
    def aligment(self):
        """Aligment Proprerty

        Returns:
            string: Team Aligment
        """
        return self.__aligment

    def attack_team(self, team):
        """ Class Method for attacking other team.
            If there's no availabale characters to fight
            the team status is set to False.
            Get's a random member from every team and
            the member of the target team is attacked.

        Args:
            team (Team): The target team.
        """
        self.get_alive_heroes()
        team.get_alive_heroes()
        my_characters = len(self.character_list)
        enemy_characters = len(team.character_list)

        if my_characters == 0:
            self.batteling = False

        elif enemy_characters == 0:
            team.batteling = False

        else:
            attacker_index = np.random.randint(0, my_characters)
            attacked_index = np.random.randint(0, enemy_characters)

        if self.batteling and team.batteling:
            self.character_list[attacker_index].attack(
                team.character_list[attacked_index])
