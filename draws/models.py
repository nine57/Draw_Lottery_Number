from django.db import models


class Number(models.Model):
    drwNo = models.PositiveIntegerField(unique=True)
    drwNoDate = models.DateTimeField()
    totSellamnt = models.BigIntegerField()
    firstWinamnt = models.BigIntegerField()
    firstPrzwnerCo = models.PositiveIntegerField()
    drwtNo1 = models.PositiveIntegerField()
    drwtNo2 = models.PositiveIntegerField()
    drwtNo3 = models.PositiveIntegerField()
    drwtNo4 = models.PositiveIntegerField()
    drwtNo5 = models.PositiveIntegerField()
    drwtNo6 = models.PositiveIntegerField()
    bnusNo = models.PositiveIntegerField()

    class Meta:
        db_table = "numbers"

    def __str__(self):
        return 'Draw' + str(self.drwNo)


# class DrawnRatio(models.Model):
#     number = models.PositiveIntegerField()
#     drw_count = models.PositiveIntegerField()
#     bonus_count = models.PositiveIntegerField()

#     class Meta:
#         db_table = "drawn_ratios"