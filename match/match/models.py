from django.db import models

class Notice(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    alt_first_name = models.CharField(max_length=100,blank=True)
    alt_last_name = models.CharField(max_length=100,blank=True)

    province = models.CharField(max_length=100)
    date_of_birth = models.DateField()

class Record(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    province = models.CharField(max_length=100)
    date_of_birth = models.DateField()

class Match(models.Model):
    WEAK = 'W'
    POSSIBLE = 'P'
    STRONG = 'S'
    MATCH_CHOICES = [
        (WEAK, 'Weak'),
        (POSSIBLE, 'Possible'),
        (STRONG, 'Strong'),
    ]
    record = models.ForeignKey('match.Record', on_delete=models.CASCADE)
    notice = models.ForeignKey('match.Notice', on_delete=models.CASCADE)

    m_type = models.CharField(max_length=1,choices=MATCH_CHOICES,default=STRONG)