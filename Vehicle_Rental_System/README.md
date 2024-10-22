# Vehical Rental Management System

This is a comprehensive command-line application designed to manage a car rental business. The system supports various operations related to customers, staff, vehicles, and bookings. Additionally, it provides functionalities for renting and returning vehicles, and generating various reports and graphs for better business insights.

## Features

### Customer Management
- **Add New Customers:** Input customer details to add them to the system, including their name, contact information, and driving license number. This ensures the business can keep track of who is renting their vehicles.
- **Update Existing Customer Details:** Modify the information of existing customers. This can include updating their contact information or correcting any errors in their initial data entry.
- **Delete Customers:** Remove customers from the system if they are no longer active or if they have requested account deletion.
- **Display All Customers:** View a list of all registered customers. This is useful for quickly accessing customer information and ensuring all data is up-to-date.

### Staff Management
- **Add New Staff Members:** Input staff details to add them to the system. This includes their name, role, and contact information.
- **Update Existing Staff Details:** Modify the information of existing staff members. This ensures that staff records are accurate and current.
- **Delete Staff Members:** Remove staff members from the system. This might be necessary if a staff member leaves the company or if their account needs to be disabled.
- **Display All Staff Members:** View a list of all staff members. This helps in managing staff and ensuring everyone is accounted for.

### Vehicle Management
- **Add New Vehicles:** Input vehicle details to add them to the system. This includes the make, model, year, and rental price of the vehicle.
- **Update Existing Vehicle Details:** Modify the information of existing vehicles. This can include updating the rental price or correcting vehicle details.
- **Delete Vehicles:** Remove vehicles from the system. This is necessary if a vehicle is sold or no longer available for rent.
- **Display Available Vehicles:** View a list of vehicles that are available for rent. This helps in managing the fleet and ensuring that customers can see which vehicles are available.
- **Display Rented Vehicles:** View a list of vehicles that are currently rented out. This helps in tracking which vehicles are in use and their expected return dates.

### Booking Management
- **Add New Bookings:** Input booking details to add them to the system. This includes the customer's name, the vehicle they are renting, and the rental period.
- **Update Existing Booking Details:** Modify the information of existing bookings. This can include changing the rental period or updating the vehicle being rented.
- **Delete Bookings:** Remove bookings from the system. This might be necessary if a booking is canceled or if there was an error in the booking process.
- **Display All Bookings:** View a list of all bookings. This helps in managing current and future rentals.

### Rental Process
- **Rent a Vehicle:** Manage the process of renting out a vehicle to a customer. This includes verifying customer details, ensuring the vehicle is available, and updating the system to reflect the rental.
- **Return a Rented Vehicle:** Manage the process of returning a rented vehicle. This includes checking the vehicle's condition, updating the system to reflect the return, and processing any final payments or refunds.
- **Generate Revenue Report:** Produce a report detailing the revenue generated from rentals. This helps in tracking the business's performance and making informed financial decisions.

### Graphical Reports
- **Display a Pie Chart of Ordinary vs Premium Cars:** Generate a visual representation of the proportion of ordinary to premium cars in the fleet. This helps in understanding the distribution of vehicle types.
- **Display a Bar Chart of Cars and Their Daily Rents:** Generate a visual representation of cars and their corresponding daily rental rates. This helps in analyzing rental prices and making pricing decisions.

## Getting Started

### Prerequisites

Ensure you have Python installed on your system. This project also requires the following Python packages:
- `prettytable`
- `matplotlib`

## Running the Application
To start the application, run the following command in your terminal:

- `python testing.py`

## Initial Setup
- *Upon the first run, you will be prompted to create initial staff credentials. This is necessary to ensure that only authorized personnel can access the system. You will need to provide a username and password for the admin account.*

## Staff Login
- *The application requires staff login to access the menu. Enter the username and password created during the initial setup to log in. This ensures that only authorized staff members can access sensitive information and perform operations.*

## File Structure
- **The system uses several text files to store data persistently:**

- `StaffCredentials.txt:`  Stores staff login credentials (username, password, role).
- `Vehicle.txt:` Stores details of all vehicles, including make, model, year, rental price, and availability status.
- `Customers.txt:` Stores details of all customers, including their name, contact information, and driving license number.
- `Staff.txt:` Stores details of all staff members, including their name, role, and contact information.
- `Bookings.txt:` Stores details of all bookings, including customer name, vehicle rented, rental period, and status.
- `rentVehicle.txt:` Stores details of ongoing rental transactions, including customer name, vehicle rented, rental start date, and expected return date.
- `rentComplte.txt:` Stores details of completed rental transactions, including customer name, vehicle rented, rental start and end dates, and total cost.
- `deletedVehicles.txt:` Logs details of vehicles that have been deleted from the system, including make, model, year, and date of deletion.
- `rentComplete.txt`: Stores completed rental transactions.

# Usage
## Menu Options
### Once logged in, the following options are available:

- **Add customer:** Input customer details to add them to the system. This includes their name, contact information, and driving license number.
- **Update customer**  details: Modify the information of an existing customer. This ensures that customer records are accurate and current.
- **Delete customer:** Remove a customer from the system. This might be necessary if a customer is no longer active or requests account deletion.
- **Display customers:** View all registered customers. This is useful for quickly accessing customer information and ensuring all data is up-to-date.
- **Add staff:** Input staff details to add them to the system. This includes their name, role, and contact information.
- **Delete staff:** Remove a staff member from the system. This might be necessary if a staff member leaves the company or if their account needs to be disabled.
- **Update staff details:** Modify the information of an existing staff member. This ensures that staff records are accurate and current.
- **Display staff:** View all staff members. This helps in managing staff and ensuring everyone is accounted for.
- **Add new vehicle:** Input vehicle details to add them to the system. This includes the make, model, year, and rental price of the vehicle.
- **Delete vehicle:** Remove a vehicle from the system. This is necessary if a vehicle is sold or no longer available for rent.
- **Update vehicle details:** Modify the information of an existing vehicle. This can include updating the rental price or correcting vehicle details.
- **View available vehicles:** Display all vehicles that are currently available for rent. This helps in managing the fleet and ensuring that customers can see which vehicles are available.
- **Rent a vehicle:** Manage the process of renting a vehicle to a customer. This includes verifying customer details, ensuring the vehicle is available, and updating the system to reflect the rental.
- **Return a vehicle:** Manage the process of a customer returning a rented vehicle. This includes checking the vehicle's condition, updating the system to reflect the return, and processing any final payments or refunds.
- **View rented vehicles:** Display all vehicles that are currently rented out. This helps in tracking which vehicles are in use and their expected return dates.
- **Add booking:** Input booking details to add them to the system. This includes the customer's name, the vehicle they are renting, and the rental period.
- **Delete booking:** Remove a booking from the system. This might be necessary if a booking is canceled or if there was an error in the booking process.
- **Update booking details:** Modify the information of an existing booking. This can include changing the rental period or updating the vehicle being rented.
- **Display bookings:** View all bookings. This helps in managing current and future rentals.
- **Display Ordinary vs Premium Cars:** Generate and display a pie chart comparing the number of ordinary and premium cars. This helps in understanding the distribution of vehicle types in the fleet.
- **Display Cars and their daily rents:** Generate and display a bar chart showing cars and their daily rental rates. This helps in analyzing rental prices and making pricing decisions.
- **Exit:** Exit the application. This safely closes the application and ensures all data is saved.
