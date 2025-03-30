# Description:- This project implements a playlist management system using a doubly linked list,Queue and file handling in Python. Users can add, delete, search, and sort songs in the playlist, and also manage a list of recently played tracks.

# achievements:- Users can dynamically add and remove songs to/from a playlist, sort songs alphabetically, and search for specific tracks. The system also maintains a persistent playlist file and keeps track of recently played songs for easy access.

 
 
 
 
 
class Node:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None
import os

class Playlist:
    def __init__(self, name):
        self.name = name
        self.head = None
        self.top = None

    def tofile(self, song):
        with open("playlist.txt", "a") as f:
            f.write(song + "\n")

    def add_node(self):
        song = input("\nEnter Song name: ").replace(" ", "_")
        new_node = Node(song)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
        self.tofile(song)

    def add_node_file(self, song):
        new_node = Node(song)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def delete_file(self, song):
        found = False
        with open("playlist.txt", "r") as f:
            lines = f.readlines()
        with open("temp.txt", "w") as f:
            for line in lines:
                if line.strip() != song:
                    f.write(line)
                else:
                    found = True
        os.remove("playlist.txt")
        os.rename("temp.txt", "playlist.txt")
        if found:
            print("Song has been deleted.")
        else:
            print("There is no song with the name you entered.")

    def delete_node(self):
        if not self.head:
            print("Playlist is empty.")
            return
        current = self.head
        if not current.next:
            self.head = None
        else:
            while current.next:
                current = current.next
            current.prev.next = None
        print("Deleted")

    def printlist(self):
        if not self.head:
            print("Playlist is empty.")
            return
        current = self.head
        print("\nPlaylist Name: " + self.name)
        while current:
            print(current.song)
            current = current.next

    def count_nodes(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        print("\nTotal songs: ", count)

    def search_song(self):
        song = input("\nEnter song to be searched: ").replace(" ", "_")
        current = self.head
        found = False
        while current:
            if current.song == song:
                print("\nSong Found")
                found = True
                break
            current = current.next
        if not found:
            print("\nSong Not Found")

    def play_song(self):
        self.printlist()
        song = input("\nChoose song you wish to play: ").replace(" ", "_")
        current = self.head
        found = False
        while current:
            if current.song == song:
                print(f"\nNow Playing...... {song}")
                self.push(song)
                found = True
                break
            current = current.next
        if not found:
            print("\nSong Not Found")

    def push(self, song):
        new_node = Node(song)
        if not self.top:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node

    def display_recent(self):
        if not self.top:
            print("\nNo recently played tracks.")
            return
        current = self.top
        print("\nRecently played tracks:")
        while current:
            print(current.song)
            current = current.next

    def last_played(self):
        if not self.top:
            print("\nNo last played tracks.")
            return
        print(f"\nLast Played Song: {self.top.song}")

    def sort_playlist(self):
        if not self.head or not self.head.next:
            return
        sorted_ = False
        while not sorted_:
            sorted_ = True
            current = self.head
            while current.next:
                if current.song > current.next.song:
                    current.song, current.next.song = current.next.song, current.song
                    sorted_ = False
                current = current.next

    def addplaylist(self):
        with open("playlist.txt", "r") as f:
            lines = f.readlines()
        for line in lines:
            self.add_node_file(line.strip())
        print("Playlist Added")

    def delete_by_search(self):
        self.printlist()
        song = input("\nChoose song you wish to delete: ").replace(" ", "_")
        current = self.head
        found = False
        while current:
            if current.song == song:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                self.delete_file(song)
                found = True
                break
            current = current.next
        if not found:
            print("\nSong Not Found")

    def delete_by_position(self, pos):
        if pos < 1:
            print("Invalid position")
            return
        current = self.head
        count = 1
        while current and count < pos:
            current = current.next
            count += 1
        if not current:
            print("Position out of range")
            return
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == self.head:
            self.head = current.next
        self.delete_file(current.song)

    def deletemenu(self):
        print("Which type of delete do you want?\n1. By Search\n2. By Position")
        choice = int(input())
        if choice == 1:
            self.delete_by_search()
        elif choice == 2:
            pos = int(input("Enter the position of the song: "))
            self.delete_by_position(pos)

def main():
    print("\t\t\t**WELCOME**")
    print("\n**please use '_' for space.")
    playlist_name = input("\n\nEnter your playlist name: ").replace(" ", "_")
    playlist = Playlist(playlist_name)

    while True:
        print("\n1. Add New Song\n2. Delete Song\n3. Display Entered Playlist\n4. Total Songs\n5. Search Song\n6. Play Song\n7. Recently Played List\n8. Last Played\n9. Sorted playlist\n10. Add 
        From File\n11. Exit")
        choice = int(input("\nEnter your choice: "))

        if choice == 1:
            playlist.add_node()
        elif choice == 2:
            playlist.deletemenu()
        elif choice == 3:
            playlist.printlist()
        elif choice == 4:
            playlist.count_nodes()
        elif choice == 5:
            playlist.search_song()
        elif choice == 6:
            playlist.play_song()
        elif choice == 7:
            playlist.display_recent()
        elif choice == 8:
            playlist.last_played()
        elif choice == 9:
            playlist.sort_playlist()
            playlist.printlist()
        elif choice == 10:
            playlist.addplaylist()
        elif choice == 11:
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
