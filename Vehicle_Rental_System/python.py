import os
import random
import string
from datetime import datetime
import matplotlib.pyplot as plt
from prettytable import PrettyTable

now = datetime.now()


# Function to check if StaffCredentials.txt is empty
def check_initial_credentials():
    if os.path.exists('StaffCredentials.txt') and os.stat('StaffCredentials.txt').st_size == 0:
        return True
    return False


# Function to initialize staff credentials
def initialize_credentials():
    print("Initial  setup: Create a username and password for Admin login.")
    username = input("Enter a username: ")
    password = input("Enter a password: ")

    with open('StaffCredentials.txt', 'w') as file:
        file.write(f"{username},{password},admin\n")  # Assuming admin permissions for initial setup

    print("Initial staff credentials set up successfully.\n")


# Function to authenticate staff login
def staff_login():
    if check_initial_credentials():
        initialize_credentials()

    username = input("Enter username: ")
    password = input("Enter password: ")

    with open('StaffCredentials.txt', 'r') as file:
        credentials = file.readlines()
        for credential in credentials:
            parts = credential.strip().split(',')
            if len(parts) == 3:
                stored_username, stored_password, permissions = parts
                if username == stored_username and password == stored_password:
                    return permissions.strip()
        else:
            print("Invalid username or password.")
            return None


# Go back to main menu
def back():
    input('\nPress ENTER to return to main menu...')
    menu()


# Modify files
def modify(filename, data):
    with open(filename, 'w+') as file:
        for line in data:
            file.write(line)


# Staff Management
def Add_Staff():
    staff_id = input('Enter Staff ID: ')
    with open('Staff.txt', 'r') as file:
        staff = file.readlines()
        for member in staff:
            if staff_id == member.split(',')[0]:
                print('Staff member already exists.')
                return
    first_name = input('Enter First Name: ')
    last_name = input('Enter Last Name: ')
    dob = input('Enter new Date of Birth (dd/mm/yyyy): ')
    role = input('Enter Role: ')
    phone = input('Enter Phone Number: ')
    address = input('Enter new Address: ')
    email = input('Enter Email: ')
    username = input('Enter username: ')
    password = input('Enter password: ')
    with open('Staff.txt', 'a') as file:
        file.write(f'{staff_id},{first_name},{last_name},{dob},{role},{phone},{address},{email}\n')
    with open('StaffCredentials.txt', 'a') as cred_file:
        cred_file.write(f'{username},{password},{role}\n')

    print('Staff member added successfully.')


# Update staff details
def Update_Staff():
    staff_id = input('\nEnter Staff ID to update: ')
    with open('Staff.txt', 'r') as file:
        staff_members = file.readlines()
    for index, staff in enumerate(staff_members):
        staff_data = staff.strip().split(',')
        if staff_id == staff_data[0]:
            print("\nCurrent details:", staff_data)
            first_name = input('Enter new First Name (leave blank to keep current): ') or staff_data[1]
            last_name = input('Enter new Last Name (leave blank to keep current): ') or staff_data[2]
            dob = input('Enter new Date of Birth (dd/mm/yyyy, leave blank to keep current): ') or staff_data[3]
            role = input('Enter Role: (leave blank to keep current): ') or staff_data[4]
            phno = input('Enter new Phone number (leave blank to keep current): ') or staff_data[5]
            address = input('Enter new Address (leave blank to keep current): ') or staff_data[6]
            email = input('Enter new Email ID (leave blank to keep current): ') or staff_data[7]
            username = input('Enter username (leave blank to keep current): ')
            password = input('Enter password (leave blank to keep current): ')
            staff_members[index] = f'{staff_id},{first_name},{last_name},{dob},{role},{phno},{address},{email}\n'
            modify('Staff.txt', staff_members)
            with open('StaffCredentials.txt', 'a') as cred_file:
                cred_file.write(f'{username},{password},{role}\n')
            print("\nStaff member updated successfully.")
            return
    else:
        print("\nStaff member not found.")
    back()


def Delete_Staff():
    staff_id = input('Enter Staff ID: ')
    with open('Staff.txt', 'r') as file:
        staff = file.readlines()
        for member in staff:
            if staff_id == member.split(',')[0]:
                staff.remove(member)
                modify('Staff.txt', staff)
                print('Staff member deleted successfully.')
                return
    print('Staff member does not exist.')


def Display_Staff():
    table = PrettyTable(
        ['Staff ID', 'First Name', 'Last Name', 'Data of Birth', 'Role', 'Phone Number', 'Address', 'Email'])
    with open('Staff.txt', 'r') as file:
        staff = file.readlines()
        for member in staff:
            member = member.split(',')
            member = [x.replace('\n', "") for x in member]
            table.add_row(member)
    print(table)


# Customer Management
def Add_Customer():
    customer_id = input('Enter Customer ID: ')
    with open('Customers.txt', 'r') as file:
        customers = file.readlines()
        for customer in customers:
            if customer_id == customer.split(',')[0]:
                print('Customer already exists.')
                return
    first_name = input('Enter First Name: ')
    last_name = input('Enter Last Name: ')
    dob = input('Enter Date of Birth (dd/mm/yyyy): ')
    address = input('Enter Address: ')
    phone_number = input('Enter Phone Number: ')
    email = input('Enter Email: ')
    license_number = input('Enter License Number: ')
    with open('Customers.txt', 'a') as file:
        file.write(f'{customer_id},{first_name},{last_name},{dob},{address},{phone_number},{email},{license_number}\n')
    print('Customer added successfully.')


# Update customer details
def Update_Customer():
    customer_id = input('\nEnter Customer ID to update: ')
    with open('Customers.txt', 'r') as file:
        customers = file.readlines()
    for index, customer in enumerate(customers):
        customer_data = customer.strip().split(',')
        if customer_id == customer_data[0]:
            print("\nCurrent details:", customer_data)
            first_name = input('Enter new First Name (leave blank to keep current): ') or customer_data[1]
            last_name = input('Enter new Last Name (leave blank to keep current): ') or customer_data[2]
            dob = input('Enter new Date of Birth (dd/mm/yyyy, leave blank to keep current): ') or customer_data[3]
            address = input('Enter new Address (leave blank to keep current): ') or customer_data[4]
            phone_number = input('Enter new Phone number (leave blank to keep current): ') or customer_data[5]
            email = input('Enter new Email ID (leave blank to keep current): ') or customer_data[6]
            license_number = input('Enter new License Number (leave blank to keep current): ') or customer_data[7]
            customers[
                index] = f'{customer_id},{first_name},{last_name},{dob},{address},{phone_number},{email},{license_number}\n'
            with open('Customers.txt', 'w') as file:
                file.writelines(customers)
            print("\nCustomer updated successfully.")
            return
    else:
        print("\nCustomer not found.")


def Delete_Customer():
    customer_id = input('Enter Customer ID: ')
    with open('Customers.txt', 'r') as file:
        customers = file.readlines()
        for customer in customers:
            if customer_id == customer.split(',')[0]:
                customers.remove(customer)
                modify('Customers.txt', customers)
                print('Customer deleted successfully.')
                return
    print('Customer does not exist.')


# Displaying Customers data
def Display_Customers():
    table = PrettyTable(['Customer ID', 'First Name', 'Last Name', 'Date of Birth', 'Address', 'Phone Number', 'Email',
                         'License Number'])
    with open('Customers.txt', 'r') as file:
        customers = file.readlines()
        for customer in customers:
            customer = customer.split(',')
            customer = [x.replace('\n', "") for x in customer]
            table.add_row(customer)
    print(table)


# Add and delete vehicles
def Add_Vehicle():
    while True:
        vehicle_id = input('\nEnter Vehicle ID: ')  # V001
        exists = False

        # Check if the vehicle ID already exists in the file
        with open('Vehicle.txt', 'r') as file:
            vehicles = file.readlines()
            for vehicle in vehicles:
                vehicle_data = vehicle.strip().split(',')
                if vehicle_id == vehicle_data[0]:
                    print('\nVehicle already exists in database.')
                    exists = True
                    break

        # If vehicle ID does not exist, proceed to add the vehicle details
        if not exists:
            name = input('Enter Vehicle Name: ')
            while True:
                typ = input('Enter vehicle type (O/P): ')
                if typ in ['O', 'P']:
                    break
                else:
                    print('\nInvalid choice. Please enter O for Ordinary or P for Premium.')

            # Only prompt for mileage if the vehicle type is Premium (P)
            mileage = input("Enter Vehicle's mileage (km): ") if typ == 'P' else '0'
            daily_rent = input("Enter daily rent rate: ")
            status = input("Enter status (A/R): ")

            # Append new vehicle details to the file
            with open('Vehicle.txt', 'a') as file:
                file.write(f'\n{vehicle_id},{name},{typ},{mileage},{daily_rent},{status}')

            print('\nVehicle added successfully!')

        while True:
            con = input('\nDo you want to add another vehicle? (Y/N): ').upper()
            if con == 'Y':
                break  # Break out of the inner loop to add another vehicle
            elif con == 'N':
                return  # Return from the function to stop adding vehicles
            else:
                print("\nInvalid choice. Please enter Y for Yes or N for No.")


# Update vehicle details
def Update_Vehicle():
    vehicle_id = input('\nEnter Vehicle ID to update: ')
    with open('Vehicle.txt', 'r') as file:
        vehicles = file.readlines()
    for index, vehicle in enumerate(vehicles):
        vehicle_data = vehicle.strip().split(',')
        if vehicle_id == vehicle_data[0]:
            print("\nCurrent details:", vehicle_data)
            name = input('Enter new Vehicle Name (leave blank to keep current): ') or vehicle_data[1]
            while True:
                typ = input('Enter new vehicle type (O/P, leave blank to keep current): ') or vehicle_data[2]
                if typ in ['O', 'P']:
                    break
                else:
                    print('\nInvalid choice.\n')
            mileage = input("Enter new Vehicle's mileage (km, leave blank to keep current): ") or vehicle_data[3]
            daily_rent = input("Enter new daily rent rate (leave blank to keep current): ") or vehicle_data[4]
            status = input("Enter new status (A/R, leave blank to keep current): ") or vehicle_data[5]
            vehicles[index] = f'{vehicle_id},{name},{typ},{mileage},{daily_rent},{status}\n'
            modify('Vehicle.txt', vehicles)
            print("\nVehicle updated successfully.")
            return
    else:
        print("\nVehicle not found.")
    back()


def Delete_Vehicle():
    vehicle_id = input('\nEnter Vehicle ID: ')
    with open('Vehicle.txt', 'r') as file:
        vehicles = file.readlines()
        for vehicle in vehicles:
            vehicle_data = vehicle.split(',')
            if vehicle_id == vehicle_data[0]:
                with open('deletedVehicles.txt', 'a') as del_file:
                    del_file.write(vehicle)
                vehicles.remove(vehicle)
                modify('Vehicle.txt', vehicles)
                print("\nVehicle deleted.")
                break
        else:
            print("\nVehicle does not exist.")
    while True:
        con = input('\nDo you want to delete another vehicle? (Y/N): ')
        if con == 'Y':
            Delete_Vehicle()
        elif con == 'N':
            return
        else:
            print("\nInvalid choice.")

# Display cars available for rent
def Display_Vehicle():
    table = PrettyTable(['Registration number', 'Model name', 'Type (Ordinary/Premium)', 'mileage (km)', 'Daily rent (₹)', 'Status'])
    with open('Vehicle.txt', 'r') as file:
        cars = file.readlines()
        for car in cars:
            car = car.strip().split(',')
            if len(car) >= 6:  # Ensure car data has at least 6 elements
                car = [x.replace('\n', "") for x in car]
                table.add_row([car[0], car[1], car[2], car[3], car[4], car[5]])
    print(table)

# Graphical representation of vehicles
def Graph1():
    ordinary = 0
    premium = 0
    with open('Vehicle.txt', 'r') as file:
        for line in file.readlines():
            if line.split(',')[2] == 'O':
                ordinary += 1
            elif line.split(',')[2] == 'P':
                premium += 1
    labels = 'Ordinary', 'Premium'
    sizes = [ordinary, premium]
    explode = (0, 0.1)
    plt.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title('Ordinary vs. Premium Cars')
    plt.show()


def Graph2():
    with open('Vehicle.txt', 'r') as file:
        labels = []
        sizes = []
        for line in file.readlines():
            labels.append(line.split(',')[1])
            sizes.append(float(line.split(',')[4]))
    plt.bar(labels, sizes, align='center', alpha=0.5)
    plt.ylabel('Daily Rent (₹)')
    plt.title('Cars and their daily rents')
    plt.xticks(rotation=90)
    plt.show()


# Rent a car
def rentVehicle(vehicle_id):
    now = datetime.now()

    with open('Vehicle.txt', 'r') as file:
        vehicles = file.readlines()

        for index, vehicle in enumerate(vehicles):
            vehicle_data = vehicle.strip().split(',')

            if vehicle_id == vehicle_data[0] and vehicle_data[5] == 'A':  # Check if vehicle is available
                renter_id = input('Enter Customer ID: ')

                # Get customer details
                with open('Customers.txt', 'r') as c_file:
                    customers = c_file.readlines()
                    for customer in customers:
                        customer_data = customer.strip().split(',')
                        if renter_id == customer_data[0]:
                            renter_name = f'{customer_data[1]} {customer_data[2]}'
                            break
                    else:
                        print("\nCustomer not found.")
                        return

                odo_start = str(odometer(1, 0))  # Assuming odometer() function is defined elsewhere
                accessories = 0
                rec_id = receiptID()  # Assuming receiptID() function is defined elsewhere

                if vehicle_data[2] == 'P':
                    print('\nAccessories available for ₹20:')
                    print('1. HD Dash Cam\n2. GPS Navigation\n3. Engine Heater')
                    if input('\nAdd accessories? (Y/N): ').upper() == 'Y':
                        accessories = 20

                rent_info = f'{rec_id},{vehicle_id},{renter_id},{renter_name},{now.strftime("%d/%m/%Y %H:%M")},{odo_start},{accessories}\n'
                rentDetails('rentVehicle.txt', rent_info)
                print(f'\nVehicle {vehicle_id} rented successfully to {renter_name}.')

                vehicle_data[5] = 'R'  # Mark vehicle as rented
                vehicles[index] = ','.join(vehicle_data) + '\n'  # Update the vehicles list
                modify('Vehicle.txt', vehicles)

                return

        else:
            print('\nVehicle not available for rent or does not exist.')


# View Rented Vehicles
def viewRentedVehicles():
    print("\n======== View Rented Vehicles ========")
    found_rentals = False

    # Create a PrettyTable instance
    table = PrettyTable(['Receipt ID', 'Vehicle ID', 'Customer ID', 'Rental Date', 'Duration', 'Odometer start', 'Odometer end', 'Status'])

    with open('rentVehicle.txt', 'r') as file:
        rentals = file.readlines()
        for rental in rentals:
            rental_data = rental.strip().split(',')
            if len(rental_data) >= 7:  # Ensure there's enough data in the rental record
                receipt_id = rental_data[0]
                vehicle_id = rental_data[1]
                customer_id = rental_data[2]
                rental_date = rental_data[3]
                if len(rental_data) == 6:  # Handle case where optional fields are missing
                    duration = "N/A"
                    odometer_start = "N/A"
                    odometer_end = rental_data[5]
                    status = "Returned"
                else:
                    duration = rental_data[4]
                    odometer_start = rental_data[5]
                    odometer_end = rental_data[6]
                    status = "Not returned"

                table.add_row([receipt_id, vehicle_id, customer_id, rental_date, duration, odometer_start, odometer_end, status])
                found_rentals = True

    if found_rentals:
        print(table)
    else:
        print("No vehicles are currently rented.")

# Function to modify files
def modify(filename, data):
    with open(filename, 'w') as file:
        for line in data:
            file.write(line)


# Return a car
def rentComplete(receipt_id):
    with open('rentVehicle.txt', 'r') as file:
        rentals = file.readlines()

    found = False
    for index, rental in enumerate(rentals):
        rental_data = rental.strip().split(',')
        if receipt_id == rental_data[0]:
            found = True
            vehicle_id = rental_data[1]
            with open('Vehicle.txt', 'r') as v_file:
                vehicles = v_file.readlines()
            for v_index, vehicle in enumerate(vehicles):
                vehicle_data = vehicle.strip().split(',')
                if vehicle_id == vehicle_data[0] and vehicle_data[5].strip() == 'R':
                    odo_end = str(odometer(2, float(rental_data[5])))
                    days_rented = (now - datetime.strptime(rental_data[4], '%d/%m/%Y %H:%M')).days + 1
                    kms_driven = float(odo_end) - float(rental_data[5])
                    type_fee = 11 if vehicle_data[2] == 'P' else 15
                    total_cost = (days_rented * float(vehicle_data[4])) + (days_rented * float(rental_data[6])) + (
                            kms_driven * type_fee)
                    transaction = f'{receipt_id},{rental_data[1]},{rental_data[2]},{rental_data[3]},{rental_data[4]},{now.strftime("%d/%m/%Y %H:%M")},{rental_data[5]},{odo_end},{total_cost}\n'
                    rentDetails('rentComplete.txt', transaction)
                    print(f'\nVehicle returned. Total charge: ₹{total_cost:.2f}')
                    vehicles[v_index] = ','.join(vehicle_data[:5]) + ',A\n'
                    modify('Vehicle.txt', vehicles)
                    rentals[index] = ','.join(rental_data[:5]) + ',A\n'
                    modify('rentVehicle.txt', rentals)
                    return
            break

    if not found:
        print('\nReceipt not found.')

    back()


# Add rent details to files
def rentDetails(filename, data):
    with open(filename, 'a') as file:
        file.write(data)
        print('\nTransaction recorded successfully.')


# Generate Receipt ID
def receiptID():
    while True:
        code = ''.join([random.choice(string.ascii_letters + string.digits) for _ in range(10)])
        with open('rentVehicle.txt', 'r') as file:
            if code not in file.read():
                return code


# Check Odometer reading
def odometer(way, initial):
    while True:
        try:
            reading = float(input('Enter odometer reading: '))
            if way == 2 and reading < initial:
                raise ValueError
            return reading
        except ValueError:
            print('\nInvalid input. Please enter a valid odometer reading.')


def generate_invoice(receipt_id):
    with open('rentComplete.txt', 'r') as file:
        transactions = file.readlines()

    found = False
    for transaction in transactions:
        transaction_data = transaction.strip().split(',')
        if receipt_id == transaction_data[0]:
            vehicle_id = transaction_data[1]
            renter_name = transaction_data[3]
            rent_date = transaction_data[4]
            return_date = transaction_data[5]
            total_cost = transaction_data[8]

            # Retrieve vehicle details
            with open('Vehicle.txt', 'r') as v_file:
                vehicles = v_file.readlines()
            for vehicle in vehicles:
                vehicle_data = vehicle.strip().split(',')
                if vehicle_id == vehicle_data[0]:
                    vehicle_name = vehicle_data[1]
                    vehicle_type = "Premium" if vehicle_data[2] == 'P' else "Ordinary"
                    daily_rent = vehicle_data[4]
                    break

            # Print invoice details
            print(f"\n========== Invoice Report ==========")
            print(f"Receipt ID: {receipt_id}")
            print(f"Customer Name: {renter_name}")
            print(f"Vehicle ID: {vehicle_id}")
            print(f"Vehicle Name: {vehicle_name}")
            print(f"Vehicle Type: {vehicle_type}")
            print(f"Rent Date: {rent_date}")
            print(f"Return Date: {return_date}")
            print(f"Daily Rent Rate: ₹{daily_rent}")
            print(f"Total Cost: ₹{total_cost}")
            print("====================================")

            found = True
            break

    if not found:
        print(f"\nReceipt ID {receipt_id} not found.")


# Bookings Management
def Add_Booking():
    booking_id = input('Enter Booking ID: ')
    with open('Bookings.txt', 'r') as file:
        bookings = file.readlines()
        for booking in bookings:
            if booking_id == booking.split(',')[0]:
                print('Booking already exists.')
                return
    customer_id = input('Enter Customer ID: ')
    vehicle_id = input('Enter Vehicle ID: ')
    staff_id = input('Enter Staff ID for Booking: ')
    start_date = input('Enter Start Date (dd/mm/yyyy): ')
    end_date = input('Enter End Date (dd/mm/yyyy): ')
    start_odo = input('Enter Start Odometer Reading: ')
    end_odo = input('Enter End Odometer Reading: ')
    total_cost = input('Enter Total Cost: ')
    with open('Bookings.txt', 'a') as file:
        file.write(
            f'{booking_id},{customer_id},{vehicle_id},{staff_id},{start_date},{end_date},{start_odo},{end_odo},{total_cost}\n')
    print('Booking added successfully.')

# Update booking details

def Update_Booking():
    booking_id = input('\nEnter Booking ID to update: ')
    with open('Bookings.txt', 'r') as file:
        bookings = file.readlines()
    for index, booking in enumerate(bookings):
        booking_data = booking.strip().split(',')
        if booking_id == booking_data[0]:
            print("\nCurrent details:", booking_data)
            customer_id = input('Enter new Customer ID (leave blank to keep current): ') or booking_data[1]
            vehicle_id = input('Enter new Vehicle ID (leave blank to keep current): ') or booking_data[2]
            staff_id = input('Enter new Staff ID (leave blank to keep current): ') or booking_data[3]
            rent_date = input('Enter new Rent Date  (leave blank to keep current (dd/mm/yyyy)): ') or booking_data[4]
            return_date = input('Enter new Return Date (leave blank to keep current (dd/mm/yyyy)): ') or booking_data[5]
            start_odo = input('Enter Start Odometer Reading (leave blank to keep current): ') or booking_data[6]
            end_odo = input('Enter End Odometer Reading (leave blank to keep current): ') or booking_data[7]
            total_cost = input('Enter Total Cost: ') or booking_data[8]
            bookings[index] = f'{booking_id},{customer_id},{vehicle_id},{staff_id},{rent_date},{return_date},{start_odo},{end_odo},{total_cost}\n'
            modify('Bookings.txt.txt', bookings)
            print("\nBooking updated successfully.")
            return
    else:
        print("\nBooking not found.")
    back()


def Delete_Booking():
    booking_id = input('Enter Booking ID: ')
    with open('Bookings.txt', 'r') as file:
        bookings = file.readlines()
        for booking in bookings:
            if booking_id == booking.split(',')[0]:
                bookings.remove(booking)
                modify('Bookings.txt', bookings)
                print('Booking deleted successfully.')
                return
    print('Booking does not exist.')


def Display_Bookings():
    table = PrettyTable(
        ['Booking ID', 'Customer ID', 'Vehicle ID', 'Staff ID', 'Start Date', 'End Date', 'Start Odometer',
         'End Odometer',
         'Total Cost'])
    with open('Bookings.txt', 'r') as file:
        bookings = file.readlines()
        for booking in bookings:
            booking = booking.split(',')
            booking = [x.replace('\n', "") for x in booking]
            table.add_row(booking)
    print(table)


def generate_revenue_report():
    total_revenue = 0
    with open('rentComplete.txt', 'r') as file:
        transactions = file.readlines()
        for transaction in transactions:
            transaction_data = transaction.strip().split(',')
            total_revenue += float(transaction_data[-1])  # Assuming last field is total cost

    print(f"\nTotal Revenue Earned: ₹{total_revenue:.2f}")


# Main menu function
def menu():
    permissions = staff_login()
    if permissions is None:
        return

    while True:
        print('\n\t\t\t\t Vehicle Rental System ')
        print('1. Staff Details')
        print('2. Customer Details')
        print('3. Vehicle Details')
        print('4. Rent details')
        print('5. Booking Details')
        print('6. Invoice')
        print('7. Exit')

        choice = input('\nEnter your choice: ')

        if choice == '1':
            while True:
                print('\n======== 2.Staff Details: ========')
                print('1. Add staff')
                print('2. Update staff')
                print('3. Delete staff details')
                print('4. Display staff')
                print('5. Back to main menu')

                staff_choice = input('\nEnter your choice: ')

                if staff_choice == '1':
                    Add_Staff()
                elif staff_choice == '2':
                    Update_Staff()
                elif staff_choice == '3':
                    Delete_Staff()
                elif staff_choice == '4':
                    Display_Staff()
                elif staff_choice == '5':
                    break
                else:
                    print("\nInvalid choice. Please try again.")

        if choice == '2':
            while True:
                print('\n======== 1.Customer Details: ========')
                print('1. Add customer')
                print('2. Update customer details')
                print('3. Delete customer')
                print('4. Display customers')
                print('5. Back to main menu')

                customer_choice = input('\nEnter your choice: ')

                if customer_choice == '1':
                    Add_Customer()
                elif customer_choice == '2':
                    Update_Customer()
                elif customer_choice == '3':
                    Delete_Customer()
                elif customer_choice == '4':
                    Display_Customers()
                elif customer_choice == '5':
                    break
                else:
                    print("\nInvalid choice. Please try again.")

        elif choice == '3':
            while True:
                print('\n======== 3. Vehicle Details: ========')
                print('1. Add new vehicle')
                print('2. Update vehicle')
                print('3. Delete vehicle details')
                print('4. Display vehicles')
                print('5. Graphical representation of vehicles')
                print('6. Graphical representation of Daily Rent')
                print('7. Back to main menu')

                vehicle_choice = input('\nEnter your choice: ')

                if vehicle_choice == '1':
                    Add_Vehicle()
                elif vehicle_choice == '2':
                    Update_Vehicle()
                elif vehicle_choice == '3':
                    Delete_Vehicle()
                elif vehicle_choice == '4':
                    Display_Vehicle()
                elif vehicle_choice == '5':
                    Graph1()
                elif vehicle_choice == '6':
                    Graph2()
                elif vehicle_choice == '7':
                    break
                else:
                    print("\nInvalid choice. Please try again.")


        elif choice == '4':
            while True:
                print('\n======== 4. Rent details: ========')
                print('1. Rent a vehicle')
                print('2. Return a vehicle')
                print('3. View rented vehicles')
                print('4. Daily Revenue')
                print('5. Back to main menu')
                rent_choice = input('\nEnter your choice: ')
                if rent_choice == '1':
                    vehicle_id = input('\nEnter Vehicle ID: ')
                    rentVehicle(vehicle_id)  # Pass the vehicle_id as an argument
                elif rent_choice == '2':
                    receipt_id = input("Enter receipt ID: ")
                    rentComplete(receipt_id)
                elif rent_choice == '3':
                    viewRentedVehicles()
                elif rent_choice == '4':
                    generate_revenue_report()
                elif rent_choice == '5':
                    break
                else:
                    print("\nInvalid choice. Please try again.")


        elif choice == '5':
            while True:
                print('\n======== 5. Booking Details: ========')
                print('1. Add booking')
                print('2. Update booking')
                print('3. Delete booking details')
                print('4. Display bookings')
                print('5. Back to main menu')

                booking_choice = input('\nEnter your choice: ')

                if booking_choice == '1':
                    Add_Booking()
                elif booking_choice == '2':
                    Update_Booking()
                elif booking_choice == '3':
                    Delete_Booking()
                elif booking_choice == '4':
                    Display_Bookings()
                elif booking_choice == '5':
                    break
                else:
                    print("\nInvalid choice. Please try again.")

        if choice == '6':
                receipt_id = input("\nEnter Receipt ID for invoice report: ")
                generate_invoice(receipt_id)


        elif choice == '7':
            print("Exiting the system.")
            break
        else:
            print("\nInvalid choice. Please try again.")

        input("\nPress Enter to continue...")


# Function to go back to the menu
def back():
    input("\nPress Enter to return to the menu.")
    menu()


# Define the other functions here...

menu()