tickets = [ticket.strip() for ticket in input().split(', ')]
def check_ticket(ticket):

    if len(ticket) != 20:
        return "invalid ticket"

    winning_symbols = ['@', '#', '$', '^']
    side_a, side_b = ticket[:10], ticket[10:]
    for match_symbol in winning_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            winning_symbols_repetition = match_symbol * uninterrupted_match_length
            if winning_symbols_repetition in side_a and winning_symbols_repetition in side_b:
                if uninterrupted_match_length == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol} Jackpot!'
                return f'ticket "{ticket}" - {uninterrupted_match_length}{match_symbol}'
    return f'ticket "{ticket}" - no match'


for ticket in tickets:
    print(check_ticket(ticket))