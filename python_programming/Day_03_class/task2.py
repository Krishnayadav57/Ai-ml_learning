        # Question no. 1
# book_flight = (flight_cost < max_price)
# flight_cost = 1500
# max_price = 2000
# print(book_flight)


        # Question Number 2 
approved_ids = ["A101", "B205", "C303", "D410"]
employee_id = input("enter employee id : ")

print(employee_id in approved_ids)

print("Z999" not in approved_ids)


    #  Question no. 3
balance = 1000.00
deposite = 250.00
service_fee = 10.50
interest_rate = 1.05

balance += deposite
balance -= service_fee
balance *= interest_rate
print(f"final balance after adding deposite, subtracting service_fee and appling interest_rate :- {balance}")
share = balance
# share = balance //= 100