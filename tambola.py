import random

class Tambola:
    def __init__(self):
        self.no_of_tickets = 6
        self.tickets_per_player = [6]  # Default: one player with 6 tickets
        self.player_tickets = []

    def start_game(self):
        self.players_summary = {i: {'no_of_tickets': no_of_tickets} for i, no_of_tickets in enumerate(self.tickets_per_player)}
        for i, tickets in enumerate(self.player_tickets):
            row_numbers = [sum(1 for item in row if isinstance(item, int)) for row in tickets]
            ticket_numbers = [sum(num for num in row_numbers[t_no*3:(t_no+1)*3]) for t_no in range(self.tickets_per_player[i])]
            self.players_summary[i]['numbers_in_row'] = row_numbers
            self.players_summary[i]['numbers_in_ticket'] = ticket_numbers
            self.players_summary[i]['numbers_marked_in_ticket'] = [0 for _ in range(self.tickets_per_player[i])]
            self.players_summary[i]['tickets'] = tickets
        return self.players_summary

    def reset_generate_tickets(self):
        self.ticket_array = [[None for _ in range(9)] for _ in range(3*6)]
        self.total_numbers = {i: [j for j in range(i*10, 10*(i+1))] for i in range(9)}
        self.total_numbers[0].remove(0)
        self.total_numbers[8].append(90)
        self.column_ranges = {i: len(self.total_numbers[i]) for i in range(9)}
        self.total_rows = 18

    def get_3rd_row(self, first_row, second_row):
        third_row = [i for i in range(9)]
        common_columns = set(first_row) & set(second_row)
        fixed_row_choices = []
        remaining_rows = self.total_rows
        self.total_rows -= 1
        for i in range(9):
            if self.column_ranges[i] == remaining_rows:
                fixed_row_choices.append(i)
                self.column_ranges[i] -= 1
                third_row.remove(i)
            elif self.column_ranges[i] <= 0 or i in common_columns:
                third_row.remove(i)
        if len(third_row) == 4 or len(common_columns) == 5:
            extra_choice = random.sample(list(common_columns), 1)
            third_row = third_row + extra_choice
        third_row = random.sample(third_row, 5 - len(fixed_row_choices))
        for i in third_row:
            self.column_ranges[i] -= 1
        return third_row + fixed_row_choices

    def get_row_indices(self):
        total_row_indices = [i for i in range(9)]
        fixed_row_choices = []
        remaining_rows = self.total_rows
        self.total_rows -= 1
        for i in range(9):
            if self.column_ranges[i] == remaining_rows:
                fixed_row_choices.append(i)
                self.column_ranges[i] -= 1
                total_row_indices.remove(i)
            elif self.column_ranges[i] <= 0:
                total_row_indices.remove(i)
        row_indices = random.sample(total_row_indices, 5 - len(fixed_row_choices))
        for i in row_indices:
            self.column_ranges[i] -= 1
        return row_indices + fixed_row_choices

    def get_row_choices(self):
        first_row = self.get_row_indices()
        second_row = self.get_row_indices()
        third_row = self.get_3rd_row(first_row, second_row)
        return [first_row, second_row, third_row]

    def get_random_ticket(self, ticket_no):
        row_choices = self.get_row_choices()
        for i, row_choice in enumerate(row_choices):
            for column in row_choice:
                number = random.choice(self.total_numbers[column])
                self.ticket_array[i + (ticket_no * 3)][column] = number
                self.total_numbers[column].remove(number)

    def genarate_serial_tickets(self):
        self.reset_generate_tickets()
        output = []
        for ticket_no in range(6):
            self.get_random_ticket(ticket_no)
            random_ticket = self.ticket_array[ticket_no*3:3*(ticket_no+1)]
            ticket_str = self.format_ticket(random_ticket)
            output.append(f"Ticket {ticket_no + 1}:\n{ticket_str}")
        return "\n\n".join(output)

    def genarate_tickets_per_player(self, tickets_per_player):
        self.tickets_per_player = tickets_per_player
        self.player_tickets = []
        output = []
        for player_id, tickets in enumerate(self.tickets_per_player):
            self.reset_generate_tickets()
            if tickets > 6:
                continue
            self.ticket_array = [[None for _ in range(9)] for _ in range(3*6)]
            for ticket_no in range(tickets):
                self.get_random_ticket(ticket_no)
            self.player_tickets.append(self.ticket_array[:tickets*3])
            player_tickets = []
            for ticket_no in range(tickets):
                random_ticket = self.player_tickets[player_id][ticket_no*3:3*(ticket_no+1)]
                ticket_str = self.format_ticket(random_ticket)
                player_tickets.append(f"Player {player_id} - Ticket {ticket_no + 1}:\n{ticket_str}")
            output.append("\n".join(player_tickets))
        return "\n\n".join(output)

    def format_ticket(self, ticket):
        lines = []
        lines.append("+" + "---+" * 9)
        for row in ticket:
            row_str = "|"
            for cell in row:
                if isinstance(cell, int):
                    row_str += f" {cell:2} |"
                elif cell == 'X':
                    row_str += "  X |"
                else:
                    row_str += "    |"
            lines.append(row_str)
            lines.append("+" + "---+" * 9)
        return "\n".join(lines)

    def get_tickets(self):
        output = []
        for i, tickets in enumerate(self.player_tickets):
            player_tickets = [f"Player {i} tickets are {self.tickets_per_player[i]}"]
            for ticket_no in range(self.tickets_per_player[i]):
                random_ticket = tickets[ticket_no*3:3*(ticket_no+1)]
                ticket_str = self.format_ticket(random_ticket)
                player_tickets.append(ticket_str)
            output.append("\n".join(player_tickets))
        return "\n\n____________________________________________________________\n\n".join(output)

class Play_Tambola:
    def __init__(self, players_summary):
        self.total_numbers = [i for i in range(1, 91)]
        self.players_summary = players_summary
        self.jaldi_game = False
        self.upper_row_game = False
        self.middle_row_game = False
        self.lower_row_game = False
        self.housie_game = False
        self.output = []

    def generate_random_number(self):
        if not self.total_numbers:
            return "No more numbers to generate."
        random_number = random.choice(self.total_numbers)
        self.output.append(f"Random number generated: {random_number}")
        self.total_numbers.remove(random_number)

        for player_id, player_data in self.players_summary.items():
            flattened_tickets = [i for row in player_data['tickets'] for i in row]
            if random_number in flattened_tickets:
                t_index = flattened_tickets.index(random_number)
                row = t_index // 9
                col = t_index % 9
                t_no = int(row / 3)
                self.output.append(f"Player {player_id} has number {random_number} at (row {row + 1}, col {col + 1}), in ticket {t_no + 1}")
                self.players_summary[player_id]['tickets'][row][col] = 'X'
                self.players_summary[player_id]['numbers_in_row'][row] -= 1
                self.players_summary[player_id]['numbers_marked_in_ticket'][t_no] += 1
                self.players_summary[player_id]['numbers_in_ticket'][t_no] -= 1

                if self.players_summary[player_id]['numbers_in_row'][row] == 0:
                    if not self.upper_row_game and row % 3 == 0:
                        self.output.append(f"PLAYER {player_id} WON UPPER ROW at row {row + 1}!")
                        self.upper_row_game = True
                    elif not self.middle_row_game and row % 3 == 1:
                        self.output.append(f"PLAYER {player_id} WON MIDDLE ROW at row {row + 1}!")
                        self.middle_row_game = True
                    elif not self.lower_row_game and row % 3 == 2:
                        self.output.append(f"PLAYER {player_id} WON LOWER ROW at row {row + 1}!")
                        self.lower_row_game = True
                if self.players_summary[player_id]['numbers_marked_in_ticket'][t_no] == 5 and not self.jaldi_game:
                    self.output.append(f"PLAYER {player_id} WON JALDI 5!")
                    self.jaldi_game = True
                if self.players_summary[player_id]['numbers_in_ticket'][t_no] == 0 and not self.housie_game:
                    self.output.append(f"PLAYER {player_id} WON TAMBOLA (HOUSIE)!")
                    self.housie_game = True
                    return "\n".join(self.output)
        return "\n".join(self.output)

    def auto_play(self):
        self.output = []
        for _ in range(90):
            if self.housie_game:
                break
            result = self.generate_random_number()
            if isinstance(result, str):
                self.output.append(result)
        return "\n".join(self.output)

# Example usage for testing in Python environment
if __name__ == "__main__":
    tambola = Tambola()
    tambola.genarate_tickets_per_player([2, 3])
    # print(tambola.get_tickets())
    players_summary = tambola.start_game()
    play_tambola = Play_Tambola(players_summary)
    # print(play_tambola.auto_play())