from django.contrib import admin
from django.utils.html import format_html
from .models import Team, Flex, Controller, Duelist, Sentinel, Initiator

class TeamAdmin(admin.ModelAdmin):
    list_display = ('nome', 'logo_preview', 'created_at', 'updated_at')
    readonly_fields = ('created_at', 'updated_at')
    fieldsets = (
        (None, {
            'fields': ('nome', 'logo')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def logo_preview(self, obj):
        if obj.logo:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 50%;" />', obj.logo.url)
        return "Nessun logo"
    
    logo_preview.allow_tags = True
    logo_preview.short_description = "Anteprima Logo"

class AgentAdmin(admin.ModelAdmin):
    list_display = ('nome', 'rank', 'team', 'team_logo_preview', 'player_image_preview', 'created_at')
    readonly_fields = ('created_at', 'updated_at', 'player_image_preview')
    list_filter = ('rank', 'team')
    search_fields = ('nome',)
    fieldsets = (
        (None, {
            'fields': ('nome', 'team', 'rank', 'image', 'player_image_preview')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def team_logo_preview(self, obj):
        if obj.team and obj.team.logo:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 50%;" />', obj.team.logo.url)
        return "Nessun logo"
    
    team_logo_preview.allow_tags = True
    team_logo_preview.short_description = "Logo Team"

    def player_image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: 100px; object-fit: cover; border-radius: 50%; border: 2px solid #ddd;" />', obj.image.url)
        return "Nessuna immagine"
    
    player_image_preview.allow_tags = True
    player_image_preview.short_description = "Anteprima Immagine"

class FlexAdmin(AgentAdmin):
    pass

class ControllerAdmin(AgentAdmin):
    pass

class DuelistAdmin(AgentAdmin):
    pass

class SentinelAdmin(AgentAdmin):
    pass

class InitiatorAdmin(AgentAdmin):
    pass

admin.site.register(Team, TeamAdmin)
admin.site.register(Flex, FlexAdmin)
admin.site.register(Controller, ControllerAdmin)
admin.site.register(Duelist, DuelistAdmin)
admin.site.register(Sentinel, SentinelAdmin)
admin.site.register(Initiator, InitiatorAdmin) 	