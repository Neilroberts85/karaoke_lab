import unittest
from src.song import Song

class TestSong(unittest.TestCase):
    
    def setUp(self):
        self.song_1 = Song("Breathe", "Faith")
        self.song_2 = Song("Help!", "Beatles")
        self.song_3 = Song("Angie", "Stones")
        self.song_4 = Song("Shout", "Tears")
        self.song_5 = Song("Jump", "VanHalen")
        self.song_6 = Song("Creep", "Radiohead")
        self.song_7 = Song("Roxanne", "Police")
        self.song_8 = Song("Breed","Live")

    def test_song_has_same_name(self):
        self.assertEqual("Shout", self.song_4.name)  

    def test_song_has_same_artist(self):
        self.assertEqual("VanHalen", self.song_5.artist)  
    