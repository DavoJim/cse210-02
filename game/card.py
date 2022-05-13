# Card class and programming
import random

class Card:
    """There will be individual cards numbered 1 to 13.

    The responsibility of Card is to keep track of the card value and determine if the next 
    card is higher or lower than the previous card
    
    Attributes:
    value (Int): the value of the card chosen at random"""
    
    def __init__(self):
        """Constructs a new instance of Card.

        Args:
            self (Card): An instance of Card.
        """
        self.value1 = 0
        self.value2 = 0
        self.points = 0  
        self.correct_guess = ''

    def card_flip(self):
        """Generates a new random value and calculates the points for the Card.
        
        Args:
            self (Card): An instance of Card.
        """
        self.value1 = random.randint(1, 13)
        self.value2 = random.randint(1, 13)

        if self.value1 > self.value2:
            self.hilo = 'l'
        elif self.value1 < self.value2:
            self.hilo = 'h'
        else:
            self.hilo = 'same number'

        

    