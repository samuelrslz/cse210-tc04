import random

class Thrower:
    """A code template for a person who throws dice. The responsibility of this 
    class of objects is to throw the dice, keep track of the values, the score 
    and determine whether or not it can throw again.
    
    Attributes:
        dice (list): A list of five numbers representing the dice values.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Thrower): An instance of Thrower.
        """
        self.dice = random.randint(1, 13)
        self.card2 = random.randint(1, 13)
        self.num_throws = 0
        
    def can_throw(self):
        """Determines whether or not the Thrower can throw again according to 
        the rules. 

        Args: 
            self (Thrower): An instance of Thrower.
        
        Returns:
            boolean: True if the list of dice has at least a five, or a one, or 
            the number of throws is zero; false if otherwise.
        """
        return (self.dice > 0 or self.dice > 0 
                or self. num_throws == 0)

        

    def get_points(self, guess):
        """Calculates the total number of points for the current throw. Fives 
        are worth 50 points. Ones are worth 100 points. 

        Args: 
            self (Thrower): An instance of Thrower.
        
        Returns:
            number: The total points for the current throw.
        """
        if guess.lower() == "h" and self.dice > self.card2:
            return 100

        else:
            return -75
        # return self.dice.count(5) * 50 + self.dice.count(1) * 100
        
    def throw_dice(self):
        """Throws the dice by randomly generating five new values. 

        Args: 
            self (Thrower): An instance of Thrower.
        """
        self.dice.clear()
        self.card2 = self.dice
        self.dice = random.randint(1, 13)