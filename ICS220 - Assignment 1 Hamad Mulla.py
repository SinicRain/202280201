class Guest:
    def __init__(self, guestID, name, email, phoneNumber, address, password):
        self.guestID = guestID
        self.name = name
        self.email = email
        self.phoneNumber = phoneNumber
        self.address = address
        self.password = password

    def login(self, email, password):
        return self.email == email and self.password == password

    def searchRooms(self, rooms):
        available_rooms = [room for room in rooms if room.availability]
        return available_rooms

    def makeReservation(self, roomID, checkInDate, checkOutDate, rooms):
        for room in rooms:
            if room.roomID == roomID and room.availability:
                room.availability = False
                return Reservation(101, self.guestID, roomID, checkInDate, checkOutDate, "Confirmed", room.pricePerNight)
        return None

    def cancelReservation(self, reservation, rooms):
        for room in rooms:
            if room.roomID == reservation.roomID:
                room.availability = True
                reservation.status = "Cancelled"

    def __str__(self):
        return f"Guest: {self.name}, Email: {self.email}"


class Staff:
    def __init__(self, staffID, name, email, role, password):
        self.staffID = staffID
        self.name = name
        self.email = email
        self.role = role
        self.password = password

    def login(self, email, password):
        return self.email == email and self.password == password

    def updateRoomDetails(self, room, newRoomType, newPricePerNight):
        room.roomType = newRoomType
        room.pricePerNight = newPricePerNight

    def viewReservations(self, reservations):
        for reservation in reservations:
            print(reservation)

    def __str__(self):
        return f"Staff: {self.name}, Role: {self.role}"


class Room:
    def __init__(self, roomID, roomType, roomNumber, availability, pricePerNight):
        self.roomID = roomID
        self.roomType = roomType
        self.roomNumber = roomNumber
        self.availability = availability
        self.pricePerNight = pricePerNight

    def __str__(self):
        return f"Room {self.roomNumber}: {self.roomType}, Available: {self.availability}, Price: {self.pricePerNight}"


class Reservation:
    def __init__(self, reservationID, guestID, roomID, checkInDate, checkOutDate, status, totalCost):
        self.reservationID = reservationID
        self.guestID = guestID
        self.roomID = roomID
        self.checkInDate = checkInDate
        self.checkOutDate = checkOutDate
        self.status = status
        self.totalCost = totalCost

    def __str__(self):
        return (f"Reservation {self.reservationID}: Guest {self.guestID}, Room {self.roomID}, "
                f"Check-in: {self.checkInDate}, Check-out: {self.checkOutDate}, Status: {self.status}, "
                f"Total Cost: {self.totalCost}")


class Payment:
    def __init__(self, paymentID, reservationID, paymentDate, paymentAmount, paymentMethod):
        self.paymentID = paymentID
        self.reservationID = reservationID
        self.paymentDate = paymentDate
        self.paymentAmount = paymentAmount
        self.paymentMethod = paymentMethod

    def __str__(self):
        return f"Payment {self.paymentID}: Reservation {self.reservationID}, Amount {self.paymentAmount}, Method: {self.paymentMethod}"


# Example usage:
# Create some rooms
room1 = Room(1, "Single", "101", True, 100)
room2 = Room(2, "Double", "102", True, 150)

# Create a guest
guest1 = Guest(1, "John Doe", "john@example.com", "1234567890", "123 Main St", "password123")

# Guest searches for available rooms
rooms = [room1, room2]
available_rooms = guest1.searchRooms(rooms)
for room in available_rooms:
    print(room)

# Guest makes a reservation
reservation = guest1.makeReservation(1, "2024-10-01", "2024-10-05", rooms)
if reservation:
    print("Reservation made:")
    print(reservation)

# Staff updates room details
staff1 = Staff(1, "Alice", "alice@example.com", "Manager", "adminpass")
staff1.updateRoomDetails(room1, "Luxury Single", 200)
print(room1)

# Guest cancels the reservation
guest1.cancelReservation(reservation, rooms)
print(f"After cancellation: {reservation}")
