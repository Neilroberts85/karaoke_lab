import unittest
from src.guest import Guest
from src.song import Song

class TestGuest(unittest.TestCase):
    
    def setUp(self):
        self.song_2 = Song("Help!", "Beatles")
        self.song_3 = Song("Angie", "Stones")
        self.song_4 = Song("Shout", "Tears")


        self.guest1 = Guest("Happy", 2, self.song_2)
        self.guest2 = Guest("Sleepy", 3, self.song_3)
        self.guest3 = Guest("Dozy", 0, self.song_4)
        
        
    def test_guest_has_same_name(self):
        self.assertEqual("Happy", self.guest1.name)

    def test_has_same_fav_song(self):
        self.assertEqual("Angie", self.guest2.fav_song.name)

   