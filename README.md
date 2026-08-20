# Movie_ticket_Booking_System

# Movie Ticket Booking System 🎬🍿

A simple, interactive, console-based Python application for managing movie theater seat reservations. This system allows users to view available seats, choose a specific seat, and automatically assigns the next available seat if their first choice is already taken.

## ✨ Features

* **Real-Time Seat Status:** Displays a clear list of all seats (1 to 10) and their current status (`Available` or `Booked`).
* **Smart Booking (Auto-Fallback):** If a user attempts to book a seat that is already taken, the system automatically searches for and assigns the next available seat in sequential order.
* **Input Validation:** Ensures users only select valid seat numbers within the theater's capacity and gracefully handles out-of-bounds inputs.
* **Interactive Loop:** Continues prompting the user for bookings until they explicitly choose to exit the system.

## 🚀 How It Works

The program uses a basic array (`seat_status`) to track the state of 10 seats. 
* `"A"` represents an **Available** seat.
* `"B"` represents a **Booked** seat.

When a user selects a seat, the system checks the corresponding index. If the seat is `"A"`, it updates it to `"B"`. If it's already `"B"`, a `while` loop checks subsequent indices until it finds an open spot or reaches the end of the row.

## 💻 How to Run

1. Ensure you have [Python](https://www.python.org/downloads/) installed on your system.
2. Clone this repository or download the script file.
3. Open your terminal or command prompt.
4. Navigate to the directory containing the script.
5. Run the following command:

   ```bash
   python Movie_Ticket_Booking_System.py
