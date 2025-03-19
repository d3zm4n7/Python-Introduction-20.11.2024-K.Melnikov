import random
from tkinter import messagebox

# История игры
HISTORY_FILE = "tulemused.txt"

VALUES = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['♠', '♥', '♦', '♣']
CARD_POINTS = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

deck = []  # Колода карт

def create_deck():
    global deck
    deck = [f"{value}{suit}" for value in VALUES for suit in SUITS]
    random.shuffle(deck)

# Функция для взятия карты из колоды
def random_card():
    if not deck:
        create_deck()  # Если колода пуста — перетасовать её заново
    card = deck.pop()
    value, suit = card[:-1], card[-1]
    points = CARD_POINTS[value]
    color = "black" if suit in ['♠', '♣'] else "red"
    return card, points, color, value

def adjust_ace_score(score, ace_count):
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1
    return score

def salvesta_tulemus(nimi, tulemus, punktid):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{nimi}: {tulemus} ({punktid} punkti)\n")

def näita_ajalugu():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            ajalugu = f.read().strip() or "History is empty."
        messagebox.showinfo("Game history", ajalugu)
    except FileNotFoundError:
        messagebox.showinfo("Game history", "History is empty.")

def võta_kaart():
    global player_score, player_ace_count
    card, points, color, value = random_card()
    if value == 'A':
        player_ace_count += 1
    player_score += points
    player_score = adjust_ace_score(player_score, player_ace_count)

    label = Label(player_frame, text=card, font=("Arial", 18), width=5, height=2, bg="white", fg=color)
    label.pack(side="left", padx=5)
    player_cards.append(label)
    if player_score > 21:
        messagebox.showinfo("Loss!", "You went over 21. You lost!")
        salvesta_tulemus(player_name_var.get() or "Mängija", "Loss", player_score)
        reset_game()

def peatu():
    global player_score, dealer_score, dealer_hidden_label, dealer_hidden_card
    dealer_hidden_label.config(text=dealer_hidden_card)

    if player_score == 21:
        messagebox.showinfo("BLACKJACK!", "BLACKJACK!")
        salvesta_tulemus(player_name_var.get() or "Mängija", "BLACKJACK", player_score)
        reset_game()
        return
    elif dealer_score == 21:
        messagebox.showinfo("BLACKJACK!", "Dealer has a BLACKJACK!")
        salvesta_tulemus(player_name_var.get() or "Mängija", "Loss", player_score)
        reset_game()
        return

    elif dealer_score > 21 or player_score > dealer_score:
        messagebox.showinfo("WIN!", "You won!")
        salvesta_tulemus(player_name_var.get() or "Mängija", "Victory", player_score)
    elif player_score < dealer_score:
        messagebox.showinfo("LOSS!", "You lost! Diller had more points.")
        salvesta_tulemus(player_name_var.get() or "Mängija", "Loss", player_score)
    else:
        messagebox.showinfo("DRAW!", "The game ended in a draw.")
        salvesta_tulemus(player_name_var.get() or "Mängija", "Draw", player_score)
    reset_game()

def reset_game():
    dealer_frame.pack_forget()
    player_frame.pack_forget()




