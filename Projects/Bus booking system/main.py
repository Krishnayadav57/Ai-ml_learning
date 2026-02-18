'''Bus booking syste 
Admin login
user login
logout
admin menu --> (Add bus, view buses, view all booking)
user menu --> (booking bus, cancel ticket, view all buses, view his all boking)
'''

import os

if not os.path.exists('admins.txt'):
    with open("admins.txt", "w") as f:
        pass

if not os.path.exists('users.txt'):
    with open("users.txt", "w") as f:
        pass

if not os.path.exists('buses.txt'):
    with open("buses.txt", "w") as f:
        pass

if not os.path.exists('bookings.txt'):
    with open("bookings.txt", "w") as f:
        pass

## Register system for user

def register_user():
    print("\n-----User Registering-----")
    username = input("Enter the username :- ").strip()
    password = input("Enter the password :- ").strip()

    if not username or not password:
            print("Username and password not be empty!!")
            return False
    
    with open("users.txt", "r") as f:
        users = []
        for line in f.readlines():
            user = line.split(",")[0]
            users.append(user)
            print(user)
            print(users)
        if username in users:
            print("--Username already exists!!--")
            return False
        
    with open("users.txt", "a") as f:
        f.write(f"{username},{password}\n")
        
    print("-----Registration successful-----")
    return True


###Login System
def admin_login():
    print("-----Admin Login Portal-----")
    username = input(("Ener username :- "))
    password = input(("Ener password :- "))
    with open("admins.txt", "r") as f:
        for line in f:
            u,p = line.strip().split(',')
            if u == username and p == password:
                print("\n---login successful---\n")
                return username
    print("Please enter valid username and password!!!")
    return False


def users_login():
    print("-----Users Login Portal-----")
    username = input(("Ener username :- "))
    password = input(("Ener password :- "))
    with open("users.txt", "r") as f:
        for line in f:
            u,p = line.strip().split(',')
            if u == username and p == password:
                print("\n---login successful---\n")
                return username
    print("Please enter valid username and password!!!")
    return False
    

### Admin menu features
def add_buses():
    bus_no = input("Enter bus number :- ").strip()
    start = input("Enter starting point  :- ").strip()
    destination = input("Enter bus destination :- ").strip()
    seats = input("Enter total seats :- ").strip()

    with open("buses.txt", "a") as f:
        f.write(f"{bus_no},{start},{destination},{seats}\n")
        print("\n---Bus Added successfully---\n")


def load_buses():
    ## Load all bus from buses.txt
    buses = []
    with open("buses.txt", "r") as f:
        for line in f:
            lines = line.strip().split(",")
            if len(lines) ==4:
                buses.append({
                    "bus_no": lines[0],
                    "start": lines[1],
                    "destination": lines[2],
                    "total_seats": lines[3],
                })
    return buses
            


## view all buses
def view_buses():
    buses = load_buses()
    if not buses:
        print("Bus not available\n")
        return
    print("\n========= BUS AVAILABLE =========\n")
    for bus in buses:
        print("---------------------------------------")
        print(f"Bus Number      :- {bus['bus_no']}")
        print(f"Bus Destination :- {bus['start']} To {bus['destination']}")
        print(f"Total Seats     :- {bus['total_seats']}")
        print("---------------------------------------\n")

def load_booking():
    booking = []
    with open("bookings.txt", "r") as f:
        for line in f:
            parts = line.strip().split(',')
            if len(parts) == 4:
                booking.append({
                    "ticket_id": parts[0],
                    "bus_no": parts[1],
                    "name": parts[2],
                    "seat": int(parts[3])
                })
    return booking

def view_all_booking():
    load = load_booking()
    if len(load) == 0:
        print("No Booking is available!!!")
        return
    print("\n========= All Booking ========")
    for line in load:
        print("----------------------------")
        print(f"Ticket ID      :- {line['ticket_id']}")
        print(f"Bus number     :- {line['bus_no']}")
        print(f"passenger Name :- {line['name']}")
        print(f"Seat number    :- {line['seat']}")
        print("----------------------------\n")

def admin_menu():
    while True:
        print("============== ADMIN MENU ==============")
        print("1. Add bus")
        print("2. View buses")
        print("3. View All Booking")
        print("4. Logout")

        choice = input("Enter your choice :- ")

        if choice == '1':
            add_buses()
        elif choice == '2':
            view_buses()
        elif choice == '3':
            view_all_booking()
        elif choice == '4':
            print("\nAdmin Logout successfully\n")
            break
        else:
            print("Invalid choice!!!")

    
def book_ticket(username):
    buses = load_buses()
    booking = load_booking()
    
    bus_no = input("Enter bus number to book :- ")

    selected_bus = None

    for bus in buses:
        if bus['bus_no'] == bus_no:
            selected_bus = bus
            break
        else:
            print("\nBus not found!!!")
            return
        
    booked_seat = []

    for b in booking:
        if b["bus_no"] == bus_no:
            booked_seat.append(b["seat"])
    if len(booked_seat) == selected_bus['total_seats']:
        print("All seat are fulled")
        return
        



