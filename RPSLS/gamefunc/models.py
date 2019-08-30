from django.db import models

class Games(models.Model):

    date_created = models.models.DateTimeField(auto_now_add=True)
    date_updated = models.models.DateTimeField(auto_now=True,)

# Make sure to fix this - should like to players// users
    
    player1 = models.ForeignKey("app.Model", verbose_name="Player 1", on_delete=models.SET_NULL)
    player1 = models.ForeignKey("app.Model", verbose_name="Player 2", on_delete=models.SET_NULL)

    player1_score = models.IntegerField(max=5)
    player2_score = models.IntegerField(max=5)

    # champion = TODO: link to players
