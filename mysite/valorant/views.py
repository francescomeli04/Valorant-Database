from django.shortcuts import render
from django.db.models import Q
from .models import Team, Flex, Controller, Duelist, Sentinel, Initiator, Rank

def index(request):
    # Get all teams ordered by name
    teams = Team.objects.all().order_by('nome')
    
    # Get all players grouped by role, ordered by rank and name
    players = {
        "flex": Flex.objects.all().order_by('-rank', 'nome'),
        "duelist": Duelist.objects.all().order_by('-rank', 'nome'),
        "controller": Controller.objects.all().order_by('-rank', 'nome'),
        "sentinel": Sentinel.objects.all().order_by('-rank', 'nome'),
        "initiator": Initiator.objects.all().order_by('-rank', 'nome'),
    }
    
    # Get search query if present
    search_query = request.GET.get('search', '')
    
    # Filter players if search query exists
    if search_query:
        for role in players:
            players[role] = players[role].filter(
                Q(nome__icontains=search_query) |
                Q(team__nome__icontains=search_query)
            )
    
    # Get rank filter if present
    rank_filter = request.GET.get('rank', '')
    
    # Filter players by rank if rank filter exists
    if rank_filter:
        for role in players:
            players[role] = players[role].filter(rank=rank_filter)
    
    # Get team filter if present
    team_filter = request.GET.get('team', '')
    
    # Filter players by team if team filter exists
    if team_filter:
        for role in players:
            players[role] = players[role].filter(team_id=team_filter)
    
    # Get available ranks for filter
    available_ranks = Rank.choices
    
    # Calculate total players and radiant players
    total_players = sum(len(players[role]) for role in players)
    radiant_players = sum(len(players[role].filter(rank='RADIANT')) for role in players)
    
    context = {
        "teams": teams,
        "players": players,
        "search_query": search_query,
        "rank_filter": rank_filter,
        "team_filter": team_filter,
        "available_ranks": available_ranks,
        "total_players": total_players,
        "total_teams": teams.count(),
        "radiant_players": radiant_players,
        "total_agents": total_players,  # Since each player is an agent
    }
    
    return render(request, "polls/index.html", context)

def team_detail(request, team_id):
    """View for displaying detailed information about a specific team"""
    try:
        team = Team.objects.get(id=team_id)
        players = {
            "flex": Flex.objects.filter(team=team).order_by('-rank', 'nome'),
            "duelist": Duelist.objects.filter(team=team).order_by('-rank', 'nome'),
            "controller": Controller.objects.filter(team=team).order_by('-rank', 'nome'),
            "sentinel": Sentinel.objects.filter(team=team).order_by('-rank', 'nome'),
            "initiator": Initiator.objects.filter(team=team).order_by('-rank', 'nome'),
        }
        
        context = {
            "team": team,
            "players": players,
        }
        return render(request, "polls/team_detail.html", context)
    except Team.DoesNotExist:
        return render(request, "polls/404.html", status=404)
