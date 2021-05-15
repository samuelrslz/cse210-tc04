from game.thrower import Thrower

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to keep track of the score and control the 
    sequence of play.
    
    Attributes:
        keep_playing (boolean): Whether or not the player wants to keep playing.
        score (number): The total number of points earned.
        thrower (Thrower): An instance of the class of objects known as Thrower.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.keep_playing = True
        self.score = 300
        self.thrower = Thrower()
        self.guess = ""

    def change_card(self, card):
        if card == 11:
            return "Jack"
        elif card == 12:
            return "Queen"
        elif card == 13:
            return "King"
        else:
            return card
        

    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means throwing the card.

        Args:
            self (Director): An instance of Director.
            thrower (Thrower): An instance of Thrower.
        """
        card = self.thrower.card
        card = self.change_card(card)

        print(f"This card is: {card}")
        self.guess = input("Guess higher or lower (h/l)")

        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means updating the score.

        Args:
            self (Director): An instance of Director.
        """
        self.thrower.throw_card()
        card = self.thrower.card
        card = self.change_card(card)
        print(f"The next card was: {card}")
        points = self.thrower.get_points(self.guess)
        self.score += points
        
    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the card that was drawn and the score.

        Args:
            self (Director): An instance of Director.
        """
        
        print(f"Your score is: {self.score}")
        if self.thrower.can_throw(self.score):


            choice = input("Play again? [y/n] ")
            self.keep_playing = (choice == "y")
            print("\n")
        else:
            print("You Lost sorry. Better luck next time.")
            self.keep_playing = False