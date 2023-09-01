import unittest
from src.room import Room
from src.song import Song
from src.guest import Guest

class TestRoom(unittest.TestCase):
    
    def setUp(self):

        self.song_1 = Song("Breathe", "Faith")

        self.guest1 = Guest("Happy", 2, self.song_1)
        self.guest2 = Guest("Sleepy", 3, self.song_1)
        self.guest3 = Guest("Dozy", 0, self.song_1)

        self.room_1 = Room("Rock", [self.guest1], [self.song_1], 5)
        self.room_2 = Room("Pop!", [], [], 4)
        # self.room_3 = Room("Metal", self.guest1, self.song_1)
        # self.room_4 = Room("Jazz", self.guest1, self.son_1)

    def test_name_is_same(self):
        self.assertEqual("Rock", self.room_1.name)

    def test_if_room_has_artist(self):
        self.assertEqual("Faith", self.room_1.songs[0].artist)

    def test_if_singer_in_room(self):
        self.room_2.add_guest(self.guest1)
        self.assertEqual("Happy", self.room_2.guests[0].name)

    def test_if_singer_has_been_removed(self):
        self.room_1.remove_guest(self.guest1)
        self.assertEqual([], self.room_1.guests)

    def test_if_song_has_added(self):
        self.room_2.add_song(self.song_1)
        self.assertEqual("Faith", self.room_2.songs[0].artist)

    def test_has_room_any_room(self):
        self.room_1.add_guest(self.guest2)
        self.room_1.add_guest(self.guest3)
        self.assertEqual(2, len(self.room_1.guests))

    def test_entry_has_been_added(self):
        self.room_1.add_guest(self.guest2)
        self.assertEqual(5, self.room_1.till)

    def test_money_has_been_deducted(self):
        self.guest1.pay_entry_fee(self.room_1.entry_fee)
        self.assertEqual(-3, self.guest1.wallet)

    def test_whoo(self):
        result = self.room_1.shout_whoo(self.guest1)
        self.assertEqual(result, "Whoooo!")

