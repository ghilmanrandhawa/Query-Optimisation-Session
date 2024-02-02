from django.db import models


class Organization(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"Organization {self.id}"


class Team(models.Model):
    name = models.CharField(max_length=255)
    
    organization = models.ForeignKey("query_optimisation.Organization", on_delete=models.CASCADE, related_name="teams")
    
    def __str__(self):
        return f"Team {self.pk} - Organization {self.organization_id}"


class TeamMemberThrough(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    
    team = models.ForeignKey("query_optimisation.Team", on_delete=models.CASCADE, related_name="team_members")
    member = models.ForeignKey("query_optimisation.Member", on_delete=models.CASCADE, related_name="teams_joined")
    
    def __str__(self):
        return f"TeamMemberThrough - Team {self.team_id}, Member {self.member_id}"


class Member(models.Model):
    name = models.CharField(max_length=255)
    
    teams = models.ManyToManyField("query_optimisation.Team", through="query_optimisation.TeamMemberThrough",
                                   related_name="members")
    
    def __str__(self):
        return f"Member {self.pk}"