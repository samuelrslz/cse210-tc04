import random

class Thrower:
    """A code template for a person who throws a card. The responsibility of this 
    class of objects is to throw the card, keep track of the value, the score 
    and determine whether or not it can throw again.
    
    Attributes:
        card (int): An int between 1 and 13.
    """

    def __init__(self):
        """Class constructor. Declares and initializes instance attributes.

        Args:
            self (Thrower): An instance of Thrower.
        """
        self.card = random.randint(1, 13)
        self.card2 = random.randint(1, 13)
        self.num_throws = 0
        
    def can_throw(self, score):
        """Determines whether or not the Thrower can throw again according to 
        the rules. 

        Args: 
            self (Thrower): An instance of Thrower.
        
        Returns:
            If the player still has points than they can play.
        """
        return (score > 0)

        

    def get_points(self, guess):
        """Calculates the total number of points for the current throw. Correct guess is 
         worth 100 points. Wrong guess is worth -75 points. 

        Args: 
            self (Thrower): An instance of Thrower.
        
        Returns:
            number: The total points for the current throw.
        """
        if guess.lower() == "h" and self.card > self.card2:
            return 100

        elif guess.lower() == "l" and self.card < self.card2:
            return 100

        elif self.card2 == self.card:
            return 0

        else:
            return -75
            
        
    def throw_card(self):
        """Throws the card by randomly generating five new values. 

        Args: 
            self (Thrower): An instance of Thrower.
        """
        
        self.card2 = self.card
        self.card = random.randint(1, 13)