import pygame, os
from pygame.sprite import Sprite

class Alien(Sprite):
    """A class to represent a single alient in the fleet."""

    def __init__(self, ai_settings, screen):
        """Initialize the alient and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Load the alien and set its rect attribute
        self.image = pygame.image.load(
            os.path.dirname(__file__) + "/images/alien.bmp")
        self.rect = self.image.get_rect()

        # Start each new alien near the top left of the scren.
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Store the alient's exact position
        self.x = float(self.rect.x)

    def blitme(self):
        """Draw the alien as its current location."""
        self.screen.blit(self.image, self.rect)

    def check_edges(self):
        """Return True if alient is at edge of screen."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self, *args):
        """Move the alien right or left."""
        self.x += (self.ai_settings.alien_speed_factor *
            self.ai_settings.fleet_direction)
        self.rect.x = self.x


        