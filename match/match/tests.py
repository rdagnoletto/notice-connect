from django.test import TestCase

class MatchTestCase(TestCase):

    def test_strong_match(self):
        # create record that results in one strong match
        pass

    def test_possible_match(self):
        # create record that results in one possible match
        pass 

    def test_weak_match(self):
        # create record that results in one weak match
        pass
    
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
    
    