from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone

class Team(models.Model):
    nome = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2)],
        help_text="Enter the team name (2-20 characters)"
    )
    logo = models.ImageField(
        upload_to='team_logos/',
        null=True,
        blank=True,
        help_text="Upload team logo (optional)"
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

class Rank(models.TextChoices):
    IRON = 'IRON', 'Iron'
    BRONZE = 'BRONZE', 'Bronze'
    SILVER = 'SILVER', 'Silver'
    GOLD = 'GOLD', 'Gold'
    PLATINUM = 'PLATINUM', 'Platinum'
    DIAMOND = 'DIAMOND', 'Diamond'
    ASCENDANT = 'ASCENDANT', 'Ascendant'
    IMMORTAL = 'IMMORTAL', 'Immortal'
    RADIANT = 'RADIANT', 'Radiant'

class Agent(models.Model):
    """
    Abstract base class for all agent types in the system.
    """
    nome = models.CharField(
        max_length=20,
        validators=[MinLengthValidator(2)],
        default="insert RiotID",
        help_text="Enter your Riot ID (2-20 characters)"
    )
    team = models.ForeignKey(
        Team,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        default="LFT",
        help_text="Select a team or leave as LFT (Looking For Team)"
    )
    rank = models.CharField(
        max_length=10,
        choices=Rank.choices,
        default=Rank.IRON,
        help_text="Select your current rank"
    )
    image = models.ImageField(
        upload_to='player_images/',
        null=True,
        blank=True,
        help_text="Upload player image (optional)"
    )
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nome} - {self.rank}"

    class Meta:
        abstract = True
        ordering = ['-rank', 'nome']

class Flex(Agent):
    """Flexible player who can play multiple roles"""
    pass

class Controller(Agent):
    """Controller role player"""
    pass

class Duelist(Agent):
    """Duelist role player"""
    pass

class Sentinel(Agent):
    """Sentinel role player"""
    pass

class Initiator(Agent):
    """Initiator role player"""
    pass