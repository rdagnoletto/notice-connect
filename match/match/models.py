from django.db import models

PROVINCES = [
    ('NL','Newfoundland and Labrador'),
    ('PE','Prince Edward Island'),
    ('NS','Nova Scotia'),
    ('NB','New Brunswick'),
    ('QC','Quebec'),
    ('ON','Ontario'),
    ('MB','Manitoba'),
    ('SK','Saskatchewan'),
    ('AB','Alberta'),
    ('BC','British Columbia'),
    ('YT','Yukon'),
    ('NT','Northwest Territories'),
    ('NU','Nunavut'),
]
class Notice(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    # blank = True because these are optional
    alt_first_name = models.CharField(max_length=100,blank=True)
    alt_last_name = models.CharField(max_length=100,blank=True)

    province = models.CharField(max_length=2,choices=PROVINCES)
    date_of_birth = models.DateField()

class Record(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    province = models.CharField(max_length=2,choices=PROVINCES)
    date_of_birth = models.DateField()

class Match(models.Model):
    # Only first and last name matching
    WEAK = 'W'

    # First and last name matching as well as province
    POSSIBLE = 'P'

    # first_name or alt_first_name of notice matches with first_name of record
    # last_name or alt_last_name of notice matches with last_name of record
    # date_of_birth and province are matching
    STRONG = 'S'

    MATCH_CHOICES = [
        (WEAK, 'Weak'),
        (POSSIBLE, 'Possible'),
        (STRONG, 'Strong'),
    ]
    # On delete cascade ensures matches are deleted when corresponded records or notices are deleted.
    record = models.ForeignKey('match.Record', on_delete=models.CASCADE)
    notice = models.ForeignKey('match.Notice', on_delete=models.CASCADE)

    m_type = models.CharField(max_length=1,choices=MATCH_CHOICES)
    