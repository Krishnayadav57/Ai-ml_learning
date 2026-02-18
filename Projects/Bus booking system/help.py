import os

# ================================
# Ensure required files exist
# ================================
for file in ["admin.txt", "users.txt", "buses.txt", "bookings.txt"]:
    if not os.path.exists(file):
        open(file, "w").close()

# Add default admin if empty
if os.stat("admin.txt").st_size == 0:
    with open("admin.txt", "w") as f:
        f.write("admin,1234\n")

# Add one default user if empty
if os.stat("users.txt").st_size == 0:
    with open("users.txt", "w") as f:
        f.write("user,1111\n")


# ================================
# Helper Functions
# ================================
def load_buses():
    """Load all buses from buses.txt"""
    buses = []
    with open("buses.txt", "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 4:
                buses.append({
                    "bus_no": parts[0],
                    "start": parts[1],
                    "destination": parts[2],
                    "total_seats": int(parts[3])
                })
    return buses


def load_bookings():
    """Load all bookings from bookings.txt"""
    bookings = []
    with open("bookings.txt", "r") as f:
        for line in f:
            parts = line.strip().split(",")
            if len(parts) == 4:
                bookings.append({
                    "ticket_id": parts[0],
                    "bus_no": parts[1],
                    "name": parts[2],
                    "seat": int(parts[3])
                })
    return bookings


# ================================
# LOGIN SYSTEM
# ================================
def admin_login():
    print("\n----- ADMIN LOGIN -----")
    username = input("Enter admin username: ")
    password = input("Enter admin password: ")

    with open("admin.txt", "r") as f:
        for line in f:
            u, p = line.strip().split(",")
            if u == username and p == password:
                print("\nAdmin login successful!\n")
                return True

    print("Invalid admin credentials!\n")
    return False


def user_login():
    print("\n----- USER LOGIN -----")
    username = input("Enter username: ")
    password = input("Enter password: ")

    with open("users.txt", "r") as f:
        for line in f:
            u, p = line.strip().split(",")
            if u == username and p == password:
                print("\nUser login successful!\n")
                return username

    print("Invalid user credentials!\n")
    return None


# ================================
# ADMIN FEATURES
# ================================
def add_bus():
    bus_no = input("Enter bus number: ")
    start = input("Enter starting point: ")
    destination = input("Enter destination: ")
    seats = input("Enter total seats: ")

    with open("buses.txt", "a") as f:
        f.write(f"{bus_no},{start},{destination},{seats}\n")

    print("\nBus added successfully !\n")


def view_buses():
    buses = load_buses()

    if not buses:
        print("No buses available.\n")
        return

    print("\n===== AVAILABLE BUSES =====")
    for bus in buses:
        print("----------------------------------")
        print(f"Bus Number   : {bus['bus_no']}")
        print(f"Route        : {bus['start']} → {bus['destination']}")
        print(f"Total Seats  : {bus['total_seats']}")
    print("----------------------------------\n")


def view_all_bookings():
    bookings = load_bookings()

    if not bookings:
        print("\nNo bookings found.\n")
        return

    print("\n===== ALL BOOKINGS =====")
    for b in bookings:
        print("----------------------------------")
        print(f"Ticket ID : {b['ticket_id']}")
        print(f"Bus No    : {b['bus_no']}")
        print(f"User      : {b['name']}")
        print(f"Seat No   : {b['seat']}")
    print("----------------------------------\n")


def admin_menu():
    while True:
        print("===== ADMIN MENU =====")
        print("1. Add Bus")
        print("2. View Buses")
        print("3. View All Bookings")
        print("4. Logout")

        choice = input("\nEnter choice: ")

        if choice == "1":
            add_bus()
        elif choice == "2":
            view_buses()
        elif choice == "3":
            view_all_bookings()
        elif choice == "4":
            print("Admin logged out!\n")
            break
        else:
            print("Invalid choice!\n")


# ================================
# USER FEATURES
# ================================
def book_ticket(username):
    buses = load_buses()
    bookings = load_bookings()

    bus_no = input("Enter bus number to book: ")

    selected_bus = None
    for bus in buses:
        if bus["bus_no"] == bus_no:
            selected_bus = bus
            break

    if not selected_bus:
        print("Bus not found!\n")
        return

    booked_seats = [b["seat"] for b in bookings if b["bus_no"] == bus_no]

    if len(booked_seats) >= selected_bus["total_seats"]:
        print("All seats are booked!\n")
        return

    seat_no = 1
    while seat_no in booked_seats:
        seat_no += 1

    ticket_id = "T" + str(len(bookings) + 1)

    with open("bookings.txt", "a") as f:
        f.write(f"{ticket_id},{bus_no},{username},{seat_no}\n")

    print("\nTicket Booked Successfully!")
    print(f"Ticket ID : {ticket_id}")
    print(f"Bus No    : {bus_no}")
    print(f"Seat No   : {seat_no}")
    print(f"User      : {username}\n")


def cancel_ticket(username):
    ticket_id = input("Enter ticket ID to cancel: ")

    bookings = load_bookings()
    new_list = []
    found = False

    for b in bookings:
        if b["ticket_id"] == ticket_id and b["name"] == username:
            found = True
        else:
            new_list.append(b)

    if not found:
        print("Ticket not found or not belongs to you!\n")
        return

    with open("bookings.txt", "w") as f:
        for b in new_list:
            f.write(f"{b['ticket_id']},{b['bus_no']},{b['name']},{b['seat']}\n")

    print("Ticket cancelled successfully!\n")


def view_my_bookings(username):
    bookings = load_bookings()

    print(f"\n===== BOOKINGS FOR {username} =====")
    found = False
    for b in bookings:
        if b["name"] == username:
            found = True
            print("----------------------------------")
            print(f"Ticket ID : {b['ticket_id']}")
            print(f"Bus No    : {b['bus_no']}")
            print(f"Seat No   : {b['seat']}")

    if not found:
        print("No bookings found!\n")
    else:
        print("----------------------------------\n")


def user_menu(username):
    while True:
        print(f"===== USER MENU ({username}) =====")
        print("1. Book Ticket")
        print("2. Cancel Ticket")
        print("3. View My Bookings")
        print("4. Logout")

        choice = input("\nEnter choice: ")

        if choice == "1":
            book_ticket(username)
        elif choice == "2":
            cancel_ticket(username)
        elif choice == "3":
            view_my_bookings(username)
        elif choice == "4":
            print("User logged out!\n")
            break
        else:
            print("Invalid choice!\n")


# ================================
# LOGIN MENU
# ================================
def login_menu():
    while True:
        print("===== LOGIN PORTAL =====")
        print("1. Admin Login")
        print("2. User Login")
        print("3. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            if admin_login():
                admin_menu()

        elif choice == "2":
            username = user_login()
            if username:
                user_menu(username)

        elif choice == "3":
            print("Thank you for using the system!")
            exit()

        else:
            print("Invalid choice!\n")


# ================================
# START PROGRAM
# ================================
login_menu()