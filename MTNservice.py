#M.T.N Sevive
'''
balance = 1000
borrow_airtime_limit = 400
borrow_data_limit = 500
dept = 0

ussd_code = input("USSD Code:...")
if ussd_code == "*555#":
	while True:
    		print("1. check balance: ")
    		print("2. Buy data: ")
    		print("3, Buy airtime: ")
    		print("4. Borrow service: ")
    		break
	choice = int(input("input choice: "))
	
	if choice == 1:
		print("your balance is :{balance}")
	break
'''
'''
sum_number = 0

for nums in range(1,101):
	if nums % 2 == 0:
		sum_number += nums
print(sum_number)
'''

balance = 1000
borrow_airtime_limit = 400
borrow_data_limit = 500
debt = 0

ussd_code = input("USSD Code: ")
if ussd_code == "*555#":
    while True:
        print(" M.T.N USSD Menu ")
        print("1. Check balance")
        print("2. Buy data")
        print("3. Buy airtime")
        print("4. Borrow service")
        print("5. Exit")

        choice = int(input("Enter choice: "))

        if choice == 1:
            print(f"Your balance is: ₦{balance}")

        elif choice == 2:
            amount = int(input("Enter data cost: ₦"))
            if amount <= balance:
                balance -= amount
                print(f"Data purchased successfully. Remaining balance: ₦{balance}")
            else:
                print("Insufficient balance.")

        elif choice == 3:
            amount = int(input("Enter airtime amount: ₦"))
            if amount <= balance:
                balance -= amount
                print(f"Airtime purchased successfully. Remaining balance: ₦{balance}")
            else:
                print("Insufficient balance.")

        elif choice == 4:
            print("1. Borrow airtime")
            print("2. Borrow data")
            borrow_choice = int(input("Enter choice: "))
            if borrow_choice == 1:
                if debt < borrow_airtime_limit:
                    debt += borrow_airtime_limit
                    balance += borrow_airtime_limit
                    print(f"You borrowed ₦{borrow_airtime_limit}. New balance: ₦{balance}")
                else:
                    print("Borrow limit reached.")
            elif borrow_choice == 2:
                if debt < borrow_data_limit:
                    debt += borrow_data_limit
                    balance += borrow_data_limit
                    print(f"You borrowed ₦{borrow_data_limit} for data. New balance: ₦{balance}")
                else:
                    print("Borrow limit reached.")

        elif choice == 5:
            print("Thank you for using our service.")
            break

        else:
            print("Invalid choice. Please try again.")

