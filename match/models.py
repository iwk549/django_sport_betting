from django.db import models

class Sport(models.Model):
    name = models.CharField(max_length=255)

class Team(models.Model):
    name = models.CharField(max_length=255)
    sport_id = models.ForeignKey(Sport, on_delete=models.PROTECT)

class Match(models.Model):
    date_time = models.DateTimeField()
    home_team_id = models.ForeignKey(Team, related_name='+', on_delete=models.PROTECT)
    away_team_id = models.ForeignKey(Team, related_name='+', on_delete=models.PROTECT)
    
    class Meta:
        indexes = [
            models.Index(fields=['home_team_id', 'away_team_id'])
        ]
        unique_together = [
            ['home_team_id', 'away_team_id', 'date_time']
        ]
        ordering = ['-date_time']

class Odds(models.Model):
    match_id = models.OneToOneField(Match, on_delete=models.CASCADE, primary_key=True)
    home_team_moneyline_odds = models.IntegerField()
    away_team_moneyline_odds = models.IntegerField()
    home_team_spread_Line = models.DecimalField(max_digits=4, decimal_places=1)
    away_team_spread_line = models.DecimalField(max_digits=4, decimal_places=1)
    home_team_spread_odds = models.IntegerField()
    away_team_spread_odds = models.IntegerField()
    over_under_line = models.DecimalField(max_digits=4, decimal_places=1)
    over_odds = models.IntegerField()
    under_odds = models.IntegerField()

class Prediction(models.Model):
    match_id = models.OneToOneField(Match, on_delete=models.CASCADE, primary_key=True)
    home_team_expected_score = models.DecimalField(max_digits=8, decimal_places=5)
    away_team_expected_score = models.DecimalField(max_digits=8, decimal_places=5)
    moneyline_predicted_winning_team_id = models.ForeignKey(Team, related_name='+', on_delete=models.PROTECT)
    moneyline_expected_payout = models.DecimalField(max_digits=6, decimal_places=2)
    spread_predicted_winning_team_id = models.ForeignKey(Team, related_name='+', on_delete=models.PROTECT)
    spread_expected_payout = models.DecimalField(max_digits=6, decimal_places=2)
    over_under_predicted_winning_team_id = models.ForeignKey(Team, related_name='+', on_delete=models.PROTECT)
    over_under_expected_payout = models.DecimalField(max_digits=6, decimal_places=2)

class Result(models.Model):
    match_id = models.OneToOneField(Match, on_delete=models.CASCADE, primary_key=True)
    home_team_score = models.SmallIntegerField()
    away_team_score = models.SmallIntegerField()
    moneyline_payout = models.DecimalField(max_digits=6, decimal_places=2)
    spread_payout = models.DecimalField(max_digits=6, decimal_places=2)
    over_under_payout = models.DecimalField(max_digits=6, decimal_places=2)
