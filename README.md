The provided code implements a **Tambola** (also known as Housie or Bingo) game in Python. It consists of two main classes: `Tambola` for generating tickets and managing players, and `Play_Tambola` for simulating the gameplay.

---

### **Overview of Tambola**
Tambola is a popular number-calling game where players have tickets with a 3x9 grid. Each ticket has 15 numbers (5 numbers per row) distributed across 9 columns, with specific rules for number placement. Numbers from 1 to 90 are called randomly, and players mark them on their tickets. The game has multiple winning conditions, such as:
- **Jaldi 5**: First player to mark 5 numbers on any ticket.
- **Upper Row**: First player to mark all numbers in the first row of any ticket.
- **Middle Row**: First player to mark all numbers in the second row of any ticket.
- **Lower Row**: First player to mark all numbers in the third row of any ticket.
- **Housie**: First player to mark all 15 numbers on any ticket.

---

### **Code Structure**
The code is organized into two classes:
1. **Tambola**: Handles ticket generation and player management.
2. **Play_Tambola**: Simulates gameplay by generating random numbers and checking for winners.

The code also includes an example usage section that demonstrates how to generate tickets, assign them to players, and play the game.

---

### **Class: Tambola**

#### **Purpose**
The `Tambola` class is responsible for:
- Generating valid Tambola tickets (3x9 grids with 15 numbers).
- Assigning tickets to players.
- Managing player data, including ticket details and game statistics.

#### **Key Attributes**
- `no_of_tickets`: Default number of tickets (6 for a serial).
- `tickets_per_player`: List specifying how many tickets each player gets (e.g., `[2, 3, 4]` means Player 0 gets 2 tickets, Player 1 gets 3, etc.).
- `player_tickets`: Stores the tickets assigned to each player.
- `total_numbers`: Dictionary mapping columns (0-8) to available numbers (e.g., column 0: 1-9, column 1: 10-19, ..., column 8: 80-90).
- `column_ranges`: Tracks how many numbers are left in each column for ticket generation.
- `total_rows`: Tracks the number of rows (3 per ticket) during ticket generation.
- `players_summary`: Stores game statistics for each player, including ticket details, numbers marked, and row/ticket status.

#### **Key Methods**

1. **reset_generate_tickets()**
   - Initializes the ticket generation process.
   - Creates an empty 3x9 grid for 6 tickets (`ticket_array`).
   - Sets up `total_numbers` with numbers 1-90, distributed across 9 columns (e.g., column 0: 1-9, column 8: 80-90).
   - Initializes `column_ranges` to track available numbers per column.
   - Sets `total_rows` to 18 (6 tickets × 3 rows).

2. **get_row_indices()**
   - Generates indices for a row (i.e., which 5 columns will have numbers).
   - Ensures that columns with enough remaining numbers are prioritized.
   - Uses `column_ranges` to enforce constraints (e.g., a column can't be used if it has no numbers left).
   - Returns a list of 5 column indices (e.g., `[0, 2, 4, 6, 8]`).

3. **get_3rd_row(first_row, second_row)**
   - Generates indices for the third row of a ticket, ensuring it complements the first two rows.
   - Avoids columns already used in both `first_row` and `second_row` (common columns).
   - Handles edge cases where all 5 columns in the first two rows are the same, ensuring the third row still has 5 numbers.
   - Returns a list of 5 column indices.

4. **get_row_choices()**
   - Generates indices for all three rows of a ticket by calling `get_row_indices()` for the first two rows and `get_3rd_row()` for the third.
   - Returns a list of three lists, each containing 5 column indices.

5. **get_random_ticket(ticket_no)**
   - Fills a ticket (3 rows) with random numbers based on the row indices from `get_row_choices()`.
   - For each selected column, picks a random number from `total_numbers` for that column and removes it to avoid duplicates.
   - Updates `ticket_array` with the numbers.

6. **genarate_serial_tickets()**
   - Generates a "serial" of 6 tickets, ensuring all numbers from 1 to 90 are used exactly once across the serial.
   - Calls `reset_generate_tickets()` to initialize and `get_random_ticket()` for each ticket.
   - Prints each ticket using the `tabulate` library in a formatted grid.

7. **genarate_tickets_per_player(tickets_per_player)**
   - Generates tickets for multiple players based on the `tickets_per_player` list.
   - For each player, generates a new set of tickets (up to 6) and stores them in `player_tickets`.
   - Each player's tickets are independent (no guarantee of unique numbers across players).

8. **get_tickets()**
   - Prints all tickets for each player, formatted as 3x9 grids using `tabulate`.
   - Shows the number of tickets per player and separates each player's tickets with a divider.

9. **start_game()**
   - Initializes the game by creating `players_summary` for each player.
   - For each player, calculates:
     - Number of tickets.
     - Number of numbers in each row (`numbers_in_row`).
     - Total numbers per ticket (`numbers_in_ticket`, always 15).
     - Numbers marked per ticket (`numbers_marked_in_ticket`, initially 0).
     - The ticket grids themselves.
   - Returns `players_summary`.

---

### **Class: Play_Tambola**

#### **Purpose**
The `Play_Tambola` class simulates the gameplay by:
- Generating random numbers from 1 to 90.
- Marking numbers on players' tickets.
- Checking for winning conditions (Jaldi 5, rows, or Housie).
- Announcing winners.

#### **Key Attributes**
- `total_numbers`: List of numbers 1-90, used for random number generation.
- `players_summary`: Player data from the `Tambola` class, including tickets and game statistics.
- Boolean flags for tracking game progress:
  - `jaldi_game`: True if Jaldi 5 has been won.
  - `upper_row_game`, `middle_row_game`, `lower_row_game`: True if the respective row has been won.
  - `housie_game`: True if Housie has been won.

#### **Key Methods**

1. **generate_random_number()**
   - Picks a random number from `total_numbers` and removes it.
   - Prints the generated number.
   - For each player:
     - Checks if the number exists in their tickets.
     - If found, marks it with `'X'` in the ticket grid.
     - Updates `numbers_in_row`, `numbers_in_ticket`, and `numbers_marked_in_ticket`.
     - Checks for winning conditions:
       - If a row has 0 numbers left, announces a row win (upper, middle, or lower).
       - If 5 numbers are marked in a ticket, announces Jaldi 5.
       - If all 15 numbers in a ticket are marked, announces Housie and ends the game.

2. **auto_play()**
   - Simulates the game by calling `generate_random_number()` up to 90 times or until Housie is won.
   - Automatically handles number generation and winner announcements.

---

### **Example Usage**
The code includes an example that demonstrates how to use the classes:

1. **Ticket Generation**:
   ```python
   tambola_game = Tambola()
   tambola_game.reset_generate_tickets()
   tambola_game.genarate_tickets_per_player([2, 3, 4])
   tambola_game.get_tickets()
   ```
   - Creates a `Tambola` instance.
   - Generates tickets for three players: Player 0 (2 tickets), Player 1 (3 tickets), Player 2 (4 tickets).
   - Prints the tickets in a formatted grid.

2. **Game Initialization**:
   ```python
   players_summary = tambola_game.start_game()
   ```
   - Initializes `players_summary` with ticket details and game statistics.

3. **Gameplay**:
   ```python
   play_tambola = Play_Tambola(players_summary)
   play_tambola.auto_play()
   ```
   - Creates a `Play_Tambola` instance with `players_summary`.
   - Runs the game, generating random numbers and checking for winners.
   - Prints each number and any winning conditions (e.g., Jaldi 5, row wins, Housie).

4. **Post-Game**:
   ```python
   tambola_game.get_tickets()
   ```
   - Prints the updated tickets, showing marked numbers (`'X'`).

5. **Single Number Generation**:
   ```python
   play_tambola.generate_random_number()
   play_tambola.players_summary
   ```
   - Generates one more random number and updates the game state.
   - Displays the updated `players_summary`.

---

### **How Tickets Are Generated**
Tambola tickets follow strict rules:
- Each ticket is a 3x9 grid with 15 numbers (5 per row).
- Numbers in each column are within a specific range (e.g., column 0: 1-9, column 8: 80-90).
- Each column has at least one number across the 6 tickets in a serial.
- Numbers are unique within a serial (for `genarate_serial_tickets()`).

The `Tambola` class ensures these rules by:
- Using `column_ranges` to track available numbers per column.
- Generating row indices to place 5 numbers per row, ensuring no column is overused.
- Randomly selecting numbers from `total_numbers` and removing them to avoid duplicates.

For example, a ticket might look like:
```
┏━━━┳━━━━┳━━━━┳━━━━┳━━━━┳━━━━┳━━━━┳━━━━┳━━━━┓
┃ 2 ┃ 18 ┃ 23 ┃    ┃ 49 ┃    ┃    ┃ 74 ┃    ┃
┣━━━╋━━━━╋━━━━╋━━━━╋━━━━╋━━━━╋━━━━╋━━━━╋━━━━┫
┃ 4 ┃    ┃ 27 ┃ 36 ┃ 43 ┃    ┃    ┃    ┃ 90 ┃
┣━━━╋━━━━╋━━━━╋━━━━╋━━━━╋━━━━╋━━━━╋━━━━╋━━━━┫
┃   ┃ 13 ┃    ┃    ┃    ┃ 59 ┃ 61 ┃ 76 ┃ 84 ┃
┗━━━┻━━━━┻━━━━┻━━━━┻━━━━┻━━━━┻━━━━┻━━━━┻━━━━┛
```
- Each row has 5 numbers.
- Numbers in each column are within the correct range (e.g., column 0: 2, 4; column 1: 18, 13).

---

### **Gameplay Simulation**
The `Play_Tambola` class simulates the game by:
- Generating random numbers (e.g., "random number generated 70").
- Marking the number on all players' tickets where it appears (e.g., "player: 0 has generated no. at (2, 7), in ticket_no. 1").
- Checking for wins:
  - Jaldi 5: When a ticket has 5 marked numbers.
  - Row wins: When all 5 numbers in a row are marked.
  - Housie: When all 15 numbers in a ticket are marked.
- Announcing winners with a formatted message (e.g., "player 1 won Tambola game.").

For example, after a few numbers are called, a ticket might look like:
```
┏━━━┳━━━┳━━━┳━━━━┳━━━━┳━━━┳━━━┳━━━┳━━━┓
┃ X ┃ X ┃   ┃    ┃ X  ┃ X ┃ X ┃   ┃   ┃
┣━━━╋━━━╋━━━╋━━━━╋━━━━╋━━━╋━━━╋━━━╋━━━┫
┃   ┃   ┃ X ┃ 30 ┃ 48 ┃   ┃ X ┃ X ┃   ┃
┣━━━╋━━━╋━━━╋━━━━╋━━━━╋━━━╋━━━╋━━━╋━━━┫
┃   ┃ X ┃   ┃ X  ┃    ┃ X ┃   ┃ X ┃ X ┃
┗━━━┻━━━┻━━━┻━━━━┻━━━━┻━━━┻━━━┻━━━┻━━━┛
```
- `'X'` indicates a marked number.

---

### **Key Features**
1. **Ticket Generation**:
   - Ensures valid Tambola tickets with correct number distribution.
   - Supports both serial tickets (unique 1-90) and per-player tickets (independent sets).
2. **Game Simulation**:
   - Automates number calling and marking.
   - Tracks multiple winning conditions.
3. **Player Management**:
   - Supports multiple players with different numbers of tickets.
   - Maintains detailed statistics (e.g., numbers marked, rows completed).
4. **Formatted Output**:
   - Uses `tabulate` to display tickets as clean grids.
   - Provides clear announcements for game events (e.g., wins).

---

### **Example Output**
Here’s a summarized example of what the code does:

1. **Ticket Generation**:
   - Player 0 gets 2 tickets, Player 1 gets 3, Player 2 gets 4.
   - Each ticket is printed as a 3x9 grid with 15 numbers.

2. **Gameplay**:
   - Numbers are called (e.g., "random number generated 70").
   - Matches are marked (e.g., "player: 0 has generated no. at (2, 7), in ticket_no. 1").
   - Wins are announced:
     - "player 1 won jaldi game."
     - "player 1 won lower row... at 2"
     - "player 0 won upper row... at 3"
     - "player 2 won middle row... at 7"
     - "player 1 won Tambola game."

3. **Final State**:
   - Tickets are printed with marked numbers (`'X'`).
   - `players_summary` shows the updated game state (tickets, marked numbers, etc.).

---

## 🤝 Contact

For questions, collaborations, or feedback:

📧 Mailapalli Purushotham

✉️ Email: [purus15987@gmail.com](mailto:purus15987@gmail.com)

🔗 [LinkedIn](https://www.linkedin.com/in/purushotham-mailapalli-0207471b3)

---

## 📄 License

This repository is available for **educational and non-commercial research** purposes only.
