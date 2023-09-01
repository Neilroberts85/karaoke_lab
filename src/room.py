class Room:
    def __init__(self, input_room_name, input_guest_list, input_song_list, input_entry_fee):
        self.name = input_room_name
        self.guests = input_guest_list
        self.songs = input_song_list
        self.entry_fee = input_entry_fee
        self.till = 0
        self.capacity = 2

    def add_guest(self, input_guest):
        if self.is_there_space():
            self.guests.append(input_guest)
            input_guest.pay_entry_fee(self.entry_fee)
            self.increase_till()
    
    def remove_guest(self, input_guest):
        self.guests.remove(input_guest)

    def add_song(self, input_song):
        self.songs.append(input_song)
    
    def is_there_space(self):
        return len(self.guests) < self.capacity

    def increase_till(self):
        self.till += self.entry_fee

    def shout_whoo(self, input_guest):
        if input_guest.fav_song in self.songs:
            return "Whoooo!"