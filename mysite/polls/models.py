from django.db import models
from django.core.validators import MinLengthValidator
from django.utils import timezone
# modello del team che permette di inserire il nome, il logo e la data di creazione
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
#modello del rank che permette di inserire il rank di appartenenza del giocatore e si collega al modello dell'agente
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
# modello dell'agente che permette di inserire il nome, il team, il rank e l'immagine del giocatore
class Agent(models.Model):
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
#sottoclasse del modello dell'agente per ciascun ruolo
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

class Tournament(models.Model):
    STATUS_CHOICES = [
        ('UPCOMING', 'Upcoming'),
        ('ONGOING', 'Ongoing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    name = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    prize_pool = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    max_teams = models.IntegerField(default=8)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='UPCOMING')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-start_date']

class TournamentTeam(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='teams')
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    seed = models.IntegerField(null=True, blank=True)
    is_eliminated = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.team.nome} in {self.tournament.name}"

    class Meta:
        ordering = ['seed']

class Match(models.Model):
    STATUS_CHOICES = [
        ('SCHEDULED', 'Scheduled'),
        ('ONGOING', 'Ongoing'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]

    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE, related_name='matches')
    round_number = models.IntegerField()
    match_number = models.IntegerField()
    team1 = models.ForeignKey(TournamentTeam, on_delete=models.CASCADE, related_name='matches_as_team1', null=True, blank=True)
    team2 = models.ForeignKey(TournamentTeam, on_delete=models.CASCADE, related_name='matches_as_team2', null=True, blank=True)
    winner = models.ForeignKey(TournamentTeam, on_delete=models.CASCADE, related_name='won_matches', null=True, blank=True)
    score_team1 = models.IntegerField(null=True, blank=True)
    score_team2 = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SCHEDULED')
    scheduled_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Match {self.match_number} - Round {self.round_number} - {self.tournament.name}"

    class Meta:
        ordering = ['round_number', 'match_number']