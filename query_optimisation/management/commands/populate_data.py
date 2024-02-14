from django.core.management.base import BaseCommand
from query_optimisation.models import Organization, Team, Member, TeamMemberThrough


class Command(BaseCommand):
    help = "Add data in Organization, Team, and Team member model."
    
    def handle(self, *args, **kwargs):
        # Data to be created
        organizations_data = [
            ('Technology Organization', ['Development Team', 'Design Team']),
            ('Marketing Organization', ['Marketing Team']),
            ('Sales Organization', ['Sales Team (North)', 'Sales Team (South)']),
        ]
        
        members_data = [
            'John Doe', 'Emily Smith', 'Michael Johnson', 'Sarah Brown', 'David Lee'
        ]
        
        # Create Organizations
        org_mapping = {}
        for org_name, teams in organizations_data:
            org, created = Organization.objects.get_or_create(name=org_name)
            org_mapping[org_name] = org
            
            for team_name in teams:
                team, created = Team.objects.get_or_create(name=team_name, organization=org)
        
        # Create Members
        member_mapping = {}
        for member_name in members_data:
            member, created = Member.objects.get_or_create(name=member_name)
            member_mapping[member_name] = member
        
        # Create TeamMemberThrough instances
        for team_name, members in {
            'Development Team': ['John Doe', 'Emily Smith'],
            'Design Team': ['Emily Smith', 'Michael Johnson'],
            'Marketing Team': ['Michael Johnson'],
            'Sales Team (North)': ['Sarah Brown', 'David Lee'],
            'Sales Team (South)': ['David Lee'],
        }.items():
            team = Team.objects.get(name=team_name)
            for member_name in members:
                member = member_mapping[member_name]
                TeamMemberThrough.objects.get_or_create(team=team, member=member)
        
        self.stdout.write(self.style.SUCCESS('Data populated successfully'))
