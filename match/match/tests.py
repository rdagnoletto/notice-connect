from django.test import TestCase
from .models import Record, Notice, Match
from .views import make_matches
import datetime

class MatchTestCase(TestCase):
    fixtures = ['notices.json', ]

    def test_strong_match(self):
        # create record that results in one strong match
        r = Record(first_name="Robert",  last_name="Age", province="YK", date_of_birth=datetime.date(1992,4,15))
        r.save()
        make_matches(r)
        matches = Match.objects.all()
        self.assertEqual(len(matches),1)
        n = matches[0].notice
        self.assertTrue(r.first_name in [n.first_name,n.alt_first_name])
        self.assertTrue(r.last_name in [n.last_name,n.alt_last_name])
        self.assertEqual(r.province, n.province)
        self.assertEqual(r.date_of_birth, n.date_of_birth)
        self.assertEqual(matches[0].record, r)
        self.assertEqual(matches[0].m_type,'S')

    def test_possible_match(self):
        # create record that results in one possible match
        r = Record(first_name="Matt",  last_name="Agnoletto", province="BC", date_of_birth=datetime.date(1991,4,15))
        r.save()
        make_matches(r)
        matches = Match.objects.all()
        self.assertEqual(len(matches),1)
        n = matches[0].notice
        self.assertTrue(r.first_name in [n.first_name,n.alt_first_name])
        self.assertTrue(r.last_name in [n.last_name,n.alt_last_name])
        self.assertEqual(r.province, n.province)
        self.assertEqual(matches[0].record, r)
        self.assertEqual(matches[0].m_type,'P')


    def test_weak_match(self):
        # create record that results in one weak match
        r = Record(first_name="Tony",  last_name="Agnoletto", province="AB", date_of_birth=datetime.date(1992,4,17))
        r.save()
        make_matches(r)
        matches = Match.objects.all()
        self.assertEqual(len(matches),1)
        n = matches[0].notice
        self.assertTrue(r.first_name in [n.first_name,n.alt_first_name])
        self.assertTrue(r.last_name in [n.last_name,n.alt_last_name])
        self.assertEqual(matches[0].record, r)
        self.assertEqual(matches[0].m_type,'W')
    
    def test_multiple_matches(self):
        # create record that results in multiple matches
        # confirm the matches are of the correct type and no duplicates
        pass
    
    def test_delete_record(self):
        # create record that results in matches and confirm 
        # matches are deleted when the record is deleted
        pass

    def test_delete_notice(self):
        # create record that results in a match with a notice and 
        # confirm the match is deleted when the notice is delete
        pass
    
    