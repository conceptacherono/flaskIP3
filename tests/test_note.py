import unittest
from website.models import Note

class CommentTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the comment class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_note = Note(id =1, comment_content = 'I love this pitch')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_note,Note))