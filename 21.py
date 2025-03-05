import tkinter as tk
import random
from tkinter import Frame, Label, Button, messagebox

# Создание окна
window = tk.Tk()
window.geometry("500x700")
window.resizable(False, False)
window.title("BLACKJACK")
window.configure(bg="green")

# Значения карт
VALUES = ['6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
SUITS = ['♠', '♥', '♦', '♣']
CARD_POINTS = {'6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10, 'A': 11}

def random_card():
    value = random.choice(VALUES)
    suit = random.choice(SUITS)
    color = "black" if suit in ['♠', '♣'] else "red"
    return f"{value}{suit}", CARD_POINTS[value], color

# Фрейм для карт дилера
dealer_frame = Frame(window, bg="lightgreen")
dealer_frame.pack(pady=20)
Label(dealer_frame, text="Дилер", bg="lightgreen", font=("Arial", 14)).pack()

dealer_hidden_card = "?"
dealer_hidden_color = "black"
dealer_real_card, dealer_real_points, dealer_real_color = random_card()

dealer_card1 = Label(dealer_frame, text=dealer_hidden_card, font=("Arial", 18), width=5, height=2, bg="white", fg=dealer_hidden_color)
dealer_card1.pack(side="left", padx=10)
dealer_card2 = Label(dealer_frame, text=dealer_real_card, font=("Arial", 18), width=5, height=2, bg="white", fg=dealer_real_color)
dealer_card2.pack(side="left", padx=10)

# Фрейм для карт игрока
player_frame = Frame(window, bg="lightgreen")
player_frame.pack(pady=20)
Label(player_frame, text="Игрок", bg="lightgreen", font=("Arial", 14)).pack()

player_cards = []
player_score = 0
dealer_score = dealer_real_points

def start_game():
    global player_score
    player_score = 0
    for label in player_cards:
        label.destroy()
    player_cards.clear()
    
    for _ in range(2):
        card, points, color = random_card()
        player_score += points
        label = Label(player_frame, text=card, font=("Arial", 18), width=5, height=2, bg="white", fg=color)
        label.pack(side="left", padx=5)
        player_cards.append(label)

def võta_kaart():
    global player_score
    card, points, color = random_card()
    player_score += points
    label = Label(player_frame, text=card, font=("Arial", 18), width=5, height=2, bg="white", fg=color)
    label.pack(side="left", padx=5)
    player_cards.append(label)
    if player_score > 21:
        paljasta_dilleri_kaart()
        messagebox.showinfo("Kaotus!", "Läksid üle 21. Kaotasid!")
        reset_game()

def paljasta_dilleri_kaart():
    global dealer_hidden_card, dealer_hidden_color, dealer_card1
    dealer_card1.config(text=dealer_real_card, fg=dealer_real_color)

def peatu():
    global player_score, dealer_score
    paljasta_dilleri_kaart()
    while dealer_score < 17:
        card, points, color = random_card()
        dealer_score += points
    if dealer_score > 21 or player_score > dealer_score:
        messagebox.showinfo("Võit!", "Sa võitsid!")
    elif player_score < dealer_score:
        messagebox.showinfo("Kaotus!", "Kaotasid! Dilleril oli rohkem punkte.")
    else:
        messagebox.showinfo("Viik!", "Mäng lõppes viigiga.")
    reset_game()

def reset_game():
    global player_score, dealer_score, dealer_real_card, dealer_real_points, dealer_real_color
    player_score = 0
    dealer_real_card, dealer_real_points, dealer_real_color = random_card()
    dealer_score = dealer_real_points
    for label in player_cards:
        label.destroy()
    player_cards.clear()
    dealer_card1.config(text="?", fg="black")
    dealer_card2.config(text=dealer_real_card, fg=dealer_real_color)
    start_game()

Button(window, text="Alusta mängu", font=("Arial", 14), command=start_game).pack(pady=10)
Button(window, text="Võta kaart", font=("Arial", 14), command=võta_kaart).pack(pady=10)
Button(window, text="Peatu", font=("Arial", 14), command=peatu).pack(pady=10)

start_game()
window.mainloop()
