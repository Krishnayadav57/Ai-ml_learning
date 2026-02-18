with open("admins.txt", "r") as f:
    for line in f:
        u,p = line.strip().split(",")
        print(u)
        # if u == username and p == password:
        #     print("\nAdmin login successful!\n")
        #     return True