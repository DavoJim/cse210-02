#Here will be the code for the user
from game.card import Card


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        card (List[Card]): A list of Card instances.
        is_playing (boolean): Whether or not the game is being played.
        score (int): The score for one round of play.
        total_score (int): The score for the entire game.
    """

    def __init__(self):
        """Constructs a new Director.
        
        Args:
            self (Director): an instance of Director.
        """
        self.is_playing = True
        self.score = 0
        self.total_score = 300

    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.is_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Ask the user if they want to flip cards.

        Args:
            self (Director): An instance of Director.
        """
      
        # guess = input("Do you think the next card will be higher or lower? [h/l] ")

        play_again = input('Keep playin HiLo? [y/n] ')
        self.is_playing = (play_again == "y")
       
    def do_updates(self):
        """Updates the player's score.

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return 
        
        card = Card()
        card.card_flip()
        print(f'The first card is {card.value1}. ')
        guess = input('Do you think the next card will be higher or lower? [h/l] ')
        print(f'The second cared is {card.value2}.')

        if guess == card.hilo:
            correct_guess = 'y'
            points = 100
        else:
            correct_guess = 'n'    
            points = (-75)        
        print(card.hilo)
        print(correct_guess)

        # points = 100 if correct_guess == 'y'  else (-75) if correct_guess == 'n' else 0


        self.score = points 
        self.total_score += self.score

    def do_outputs(self):
        """Displays the cards and the score. Also asks the player if they want to flip again. 

        Args:
            self (Director): An instance of Director.
        """
        if not self.is_playing:
            return

        print(f"Your score is: {self.total_score}\n")
        if self.total_score <= 0:
            print('You lose!')
            self.is_playing = False
            return
        # self.is_playing == (self.total_score > 0)