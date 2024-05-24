# Osztályok Létrehozása
#   xx Hozz létre egy Szoba absztrakt osztályt, amely alapvető attribútumokat definiál (ár, szobaszám). (5 pont)
#   xx Hozz létre az Szoba osztályból EgyagyasSzoba és KetagyasSzoba származtatott osztályokat, amelyek különböző attributumai vannak, és az áruk
#       is különböző.(5 pont)
#   xx Hozz létre egy Szalloda osztályt, ami ezekből a Szobákból áll, és van saját attributuma is (név pl.) (10 pont)
#   xx Hozz létre egy Foglalás osztályt, amelybe a Szálloda szobáinak foglalását tároljuk (elég itt, ha egy foglalás csak egy napra szól) (10 pont)
#
# Foglalások Kezelése
#   xx Implementálj egy metódust, ami lehetővé teszi szobák foglalását dátum alapján, visszaadja annak árát. (15 pont)
#   xx Implementálj egy metódust, ami lehetővé teszi a foglalás lemondását. (5 pont)
#   xx Implementálj egy metódust, ami listázza az összes foglalást. (5 pont)
#
# Felhasználói Interfész és adatvalidáció
#   xx Készíts egy egyszerű felhasználói interfészt, ahol a felhasználó kiválaszthatja a kívánt műveletet (pl. foglalás, lemondás, listázás). (20 pont)
#   !!! check avail. !!! A foglalás létrehozásakor ellenőrizd, hogy a dátum érvényes (jövőbeni) és a szoba elérhető-e akkor. (10 pont)
#   xx Biztosítsd, hogy a lemondások csak létező foglalásokra lehetségesek. (5 pont)
# #   xx Töltsd fel az futtatás után a rendszert 1 szállodával, 3 szobával és 5 foglalással, mielőtt a felhasználói adatbekérés megjelenik. (10 pont)

from datetime import datetime


#Classes

class Room:

    def __init__(self, roomnumber, price):
        self.roomnumber = roomnumber
        self.price = price

class OneBedRoom(Room):
     def __init__(self, roomnumber, extra):
        super().__init__(roomnumber, 20000)
        self.extra = extra

class TwoBedRoom(Room):
    def __init__(self, roomnumber, extra):
        super().__init__(roomnumber, 40000)
        self.extra = extra

class Reservation:
    def __init__(self, room,date):
        self.room = room
        self.date = date

class Hotel:
    def __init__(self, hotelname):
        self.hotelname = hotelname
        self.rooms  = []
        self.reservations = []

    #Reservations

    def add_Room(self, Room):
        self.rooms.append(Room)


    def reserve_Room(self, roomnumber, date):
        for res in self.reservations:
            if res.room.roomnumber == roomnumber and res.date == date:
                print("A szoba már foglalt")
                return
        for room in self.rooms:
            if room.roomnumber == roomnumber:
                self.reservations.append(Reservation(room,date))
                return room.price
        print("Szoba nem található")

    def remove_Room(self, roomnumber, date):
        for res in self.reservations:
            if res.room.roomnumber == roomnumber and res.date == date:
                self.reservations.remove(res)
                return True
        return False

    def list_reservations(self):
        for res in self.reservations:
            print(f"Room:  {res.room.roomnumber}, Date: {res.date}")


#Create Classes

hotel = Hotel("Szep Hotel")

hotel.add_Room(OneBedRoom("010", "Hair Dryer"))
hotel.add_Room(OneBedRoom("011", "Bath"))
hotel.add_Room(TwoBedRoom("012", "Kitchen"))


hotel.reserve_Room("010",datetime(2024,12,30))
hotel.reserve_Room("011",datetime(2024,12,30))
hotel.reserve_Room("012",datetime(2024,12,30))
hotel.reserve_Room("012",datetime(2024,12,31))
hotel.reserve_Room("010",datetime(2024,12,31))

while True:

    print("\nVálassz:")
    print("1 Foglalás")
    print("2 Foglalás lemondása")
    print("3 Foglalások listázása")
    print("4 Szobák listázása")
    print("5 Kilépés")
    case = input("Kiválasztás: ")

    if case == "1":

        date = input("\n Add meg a dátumot (YYYY-MM-DD): ")
        roomnumber = input("Add meg a szobaszámot: ")

        try:
            date = datetime.strptime(date, "%Y-%m-%d")
            if date < datetime.today():
                print("A dátum már nem foglalható")
            else:
                price = hotel.reserve_Room(roomnumber,date)
                if price:
                    print(f"\nSikeres foglalás! A szoba ára : {price} Ft")
                else:
                    print("\n Hibás szobaszámot adott meg.")
        except ValueError:
            print("Hibás dátum formátum")

    elif case == "2":

        roomnumber = input("\n Add meg a szoba számát! ")
        date = input("Add meg a foglalás dátumát! ")

        try:
            date = datetime.strptime(date, "%Y-%m-%d")

            if hotel.remove_Room(roomnumber,date):
                print("\nA foglalás lemondva")
            else:
                print("\nNincs ilyen foglalás")
        except ValueError:
            print("Hibás dátum formátum")

    elif case == "3":
        hotel.list_reservations()

    elif case == "4":
        print(f"Regisztrált szobák száma:  {len(hotel.rooms)}")
        print("Egyágyas szobák: ")
        for room in hotel.rooms:
            if isinstance(room, OneBedRoom):
                print(f"\tSzobaszam: {room.roomnumber}, Ár: {room.price}, Extra: {room.extra}")

        print(("Kétágyas szobák: "))
        for room in hotel.rooms:
            if isinstance(room, TwoBedRoom):
                print(f"\tSzobaszam: {room.roomnumber}, Ár: {room.price}, Extra: {room.extra}")

    elif case == "5":
        break
    else:
        print(("\nHibás választás!"))