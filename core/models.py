from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):

    COLORS = (
        ('viridis', 'Viridis'),
        ('plasma', 'Plasma'),
        ('magma', 'Magma'),
        ('inferno', 'Inferno'),
        ('Blues', 'Blues'),
        ('BrBG', 'Brown-Blue-Green'),
        ('BuGn', 'Blue-Green'),
        ('BuPu', 'Blue-Purple'),
        ('CMRmap', 'CMRmap'),
        ('GnBu', 'Green-Blue'),
        ('Greens', 'Green'),
        ('Greys', 'Grey'),
        ('OrRd', 'Orange-Red'),
        ('Oranges', 'Orange'),
        ('PRGn', 'Pink-Red-Green'),
        ('PiYG', 'Pink-Yellow-Green'),
        ('PuBu', 'Purple-Blue'),
        ('PuBuGn', 'Purple-Blue-Green'),
        ('PuOr', 'Purple-Orange'),
        ('PuRd', 'Purple-Red'),
        ('Purples', 'Purples'),
        ('RdBu', 'Red-Blue'),
        ('RdGy', 'Red-Grey'),
        ('RdPu', 'Red-Purple'),
        ('RdYlBu', 'Red-Yellow-Blue'),
        ('RdYlGn', 'Red-Yellow-Green'),
        ('Reds', 'Reds'),
        ('Spectral', 'Spectral'),
        ('Wistia', 'Wistia'),
        ('YlGn', 'Yellow-Green'),
        ('YlGnBu', 'Yellow-Green-Blue'),
        ('YlOrBr', 'Yellow-Orange-Brown'),
        ('YlOrRd', 'Yellow-Orange-Red'),
        ('afmhot', 'Afmhot'),
        ('autumn', 'Autumn'),
        ('binary', 'Binary'),
        ('bone', 'Bone'),
        ('brg', 'BRG'),
        ('bwr', 'BWR'),
        ('cool', 'Cool'),
        ('coolwarm', 'Coolwarm'),
        ('copper', 'Copper'),
        ('cubehelix', 'Cubehelix'),
        ('flag', 'Flag'),
        ('gist_earth', 'Gist-earth'),
        ('gist_gray', 'Gist-gray'),
        ('gist_heat', 'Gist-heat'),
        ('gist_ncar', 'Gist-nicar'),
        ('gist_rainbow', 'Gist-rainbow'),
        ('gist_stern', 'Gist-stern'),
        ('gist_yarg', 'Gist-yarg'),
        ('gnuplot', 'Gnuplot'),
        ('gnuplot2', 'Gnuplot2'),
        ('gray', 'Gray'),
        ('hot', 'Hot'),
        ('hsv', 'Hsv'),
        ('jet', 'Jet'),
        ('nipy_spectral', 'Nipy-spectral'),
        ('ocean', 'Ocean'),
        ('pink', 'Pink'),
        ('prism', 'Prism'),
        ('rainbow', 'Rainbow'),
        ('seismic', 'Seismic'),
        ('spring', 'Spring'),
        ('summer', 'Summer'),
        ('terrain', 'Terrain'),
        ('winter', 'Winter'),
        # Qualitative
        ('Accent', 'Accent'),
        ('Dark2', 'Dark2'),
        ('Paired', 'Paired'),
        ('Pastel1', 'Pastel1'),
        ('Pastel2', 'Pastel2'),
        ('Set1', 'Set1'),
        ('Set2', 'Set2'),
        ('Set3', 'Set3'),
        ('tab10', 'Tab10'),
        ('tab20', 'Tab20'),
        ('tab20b', 'Tab20b'),
        ('tab20c', 'Tab20c'),
    )

    email = models.EmailField(max_length=150, unique=True)
    user_credits = models.PositiveIntegerField(default=0)
    colors = models.CharField(max_length=50, choices=COLORS, default='viridis', blank=True)

    #USERNAME_FIELD = 'email'
    #REQUIRED_FIELDS = ['username']
    
    def __str__(self):
        return f"{self.username} {self.user_credits}"
