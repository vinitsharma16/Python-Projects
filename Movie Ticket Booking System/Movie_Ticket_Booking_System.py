# Movie Ticket Booking System

TOTAL_SEATS = 10

seat_status = ["A"] * TOTAL_SEATS        ## Marker "A" is for the sat availability and "B" means seat is booked

def show_seats():
    print("\nSeat Status:")
    for i in range(TOTAL_SEATS):
        print("Seat", i + 1, ":", "Available" if seat_status[i] == "A" else "Booked")
    print()
def is_available(seat_no):
    index = seat_no - 1
    if seat_status[index] == "A":
        return True
    else:
        return False
def book_seat(seat_no):
    index = seat_no - 1


    if not is_available(seat_no):
        print("Seat", seat_no, "is already booked. Looking for the next available seat...")


        next_seat = seat_no + 1
        while next_seat <= TOTAL_SEATS:
            if is_available(next_seat):
                seat_status[next_seat - 1] = "B"
                print("Seat", next_seat, "has been booked for you instead!")
                return
            next_seat = next_seat + 1


        print("Sorry, no seats are available after seat", seat_no)
    else:

        seat_status[index] = "B"
        print("Seat", seat_no, "has been booked successfully!")



def main():
    while True:
        show_seats()
        choice = input("Enter seat number to book (or 0 to exit): ")
        choice = int(choice)

        if choice == 0:
            print("Thank you for using the booking system!")
            break

        if choice < 1 or choice > TOTAL_SEATS:
            print("Invalid seat number. Please choose between 1 and", TOTAL_SEATS)
            continue

        book_seat(choice)


main()