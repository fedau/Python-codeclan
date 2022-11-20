from classes.guest import Guest


class Room:
    def __init__(self, name, capacity, guests):
        self.name = name
        self.capacity = capacity
        self.songs = []
        self.revenue = 0
        self.people_in_room = []

        for guest in guests:
            self.add_guest(guest)


    def amount_in_room(self):
            return len(self.people_in_room)

    def add_guest(self, guest):
        if self.amount_in_room() < self.capacity:
            self.people_in_room.append(guest)
            self.revenue = self.revenue + 2
            return self.people_in_room 
        return "room is full"

    def get_money_from_guest(self, guest):
        guest.cash - 2
        return 2


    def add_song_to_room(self, song):
        self.songs.append(song.name)
        return self.songs


# already_in_room = lamba 2, len(self.people_in_room) : 2 * len(self.people_in_room)
# revenue = already_in_room 
# if add_guest():
# revenue += 2 

