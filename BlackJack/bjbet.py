import tkinter as tk
from tkinter import messagebox
import random
import os

class BlackjackGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Blackjack")
        
        self.balance = 1000
        self.bet = 0
        self.player_name = "Player"
        self.player_hand = []
        self.split_hand = []
        self.dealer_hand = []  # Добавляем руку дилера
        self.active_hand = "player"  # Активная рука по умолчанию
        
        self.setup_ui()

    def setup_ui(self):
        self.label_balance = tk.Label(self.master, text=f"Balance: {self.balance} chips", font=("Arial", 14))
        self.label_balance.pack(pady=10)

        self.entry_name = tk.Entry(self.master, font=("Arial", 14))
        self.entry_name.pack(pady=5)
        self.entry_name.insert(0, "Enter your name")

        self.entry_bet = tk.Entry(self.master, font=("Arial", 14))
        self.entry_bet.pack(pady=5)
        self.entry_bet.insert(0, "Enter your bet")

        self.button_place_bet = tk.Button(self.master, text="Place Bet", command=self.place_bet)
        self.button_place_bet.pack(pady=5)

        self.button_start_game = tk.Button(self.master, text="Start Game", command=self.start_game, state=tk.DISABLED)
        self.button_start_game.pack(pady=5)

        self.button_split = tk.Button(self.master, text="Split", command=self.split_hand_action, state=tk.DISABLED)
        self.button_split.pack(pady=5)

        self.button_hit = tk.Button(self.master, text="Take Card", command=self.take_card, state=tk.NORMAL)
        self.button_hit.pack(pady=5)

        self.button_stand = tk.Button(self.master, text="Check", command=self.check_result, state=tk.NORMAL)
        self.button_stand.pack(pady=5)

        self.button_new_game = tk.Button(self.master, text="New Game", command=self.start_game, state=tk.NORMAL)
        self.button_new_game.pack(pady=5)

        self.button_show_history = tk.Button(self.master, text="Show Leaderboard", command=self.show_leaderboard)
        self.button_show_history.pack(pady=5)

        self.label_result = tk.Label(self.master, text="", font=("Arial", 14))
        self.label_result.pack(pady=10)

        self.label_dealer = tk.Label(self.master, text="", font=("Arial", 14))  # Новое поле для карт дилера
        self.label_dealer.pack(pady=5)

        self.label_advice = tk.Label(self.master, text="", font=("Arial", 12), fg="blue")
        self.label_advice.pack(pady=5)

        # Выбор активной руки при Split
        self.split_checkbox = tk.IntVar()
        self.checkbox_split = tk.Checkbutton(self.master, text="Play Split Hand", variable=self.split_checkbox)
        self.checkbox_split.pack(pady=5)

    def place_bet(self):
        self.player_name = self.entry_name.get() or "Player"
        try:
            bet_amount = int(self.entry_bet.get())
            if bet_amount > self.balance:
                messagebox.showwarning("Invalid Bet", "You cannot bet more than your current balance.")
            elif bet_amount <= 0:
                messagebox.showwarning("Invalid Bet", "Your bet must be greater than zero.")
            else:
                self.bet = bet_amount
                self.balance -= self.bet
                self.label_balance.config(text=f"Balance: {self.balance} chips")
                self.button_start_game.config(state=tk.NORMAL)
                self.label_result.config(text=f"Bet Placed: {self.bet} chips")
        except ValueError:
            messagebox.showwarning("Invalid Input", "Please enter a valid number for your bet.")
    
    def save_score(self):
        try:
            with open("leaderboard.txt", "a") as file:
                file.write(f"{self.player_name}: {self.balance}\n")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save score: {e}")

    def start_game(self):
        self.player_hand = [random.randint(2, 11), random.randint(2, 11)]
        self.split_hand = []  # Сбрасываем split руку при начале новой игры
        self.dealer_hand = [random.randint(2, 11), random.randint(2, 11)]  # Добавляем карты дилера

        self.label_result.config(text=f"Your cards: {self.player_hand}")
        self.label_dealer.config(text=f"Dealer's cards: [{self.dealer_hand[0]}, ?]")
        self.give_advice()

        if self.player_hand[0] == self.player_hand[1]:
            self.button_split.config(state=tk.NORMAL)
        else:
            self.button_split.config(state=tk.DISABLED)

        if self.balance > 0:
            self.save_score()

    def split_hand_action(self):
        self.split_hand = [self.player_hand.pop()]
        self.label_result.config(text=f"Your hands:\n- Hand 1: {self.player_hand}\n- Hand 2: {self.split_hand}")
        self.balance -= self.bet
        self.label_balance.config(text=f"Balance: {self.balance} chips")
        self.label_result.config(text=f"Split completed! Both hands are active.")
        self.give_advice()

    def take_card(self):
        active_hand = self.split_hand if self.split_checkbox.get() else self.player_hand
        active_hand.append(random.randint(2, 11))
        self.label_result.config(text=f"Your cards: {self.player_hand}\nSplit hand: {self.split_hand}")
        self.give_advice()  # Возвращаем подсказки после взятия карты

        if sum(active_hand) > 21:
            messagebox.showinfo("Bust", f"{self.player_name} busted with {sum(active_hand)} points!")
            self.check_result()

    def give_advice(self):
        active_hand = self.split_hand if self.split_checkbox.get() else self.player_hand
        total = sum(active_hand)
        if total < 12:
            advice = "Advice: Take a card (Hit)"
        elif total in [12, 13, 14, 15, 16]:
            advice = "Advice: Take a card (Hit), unless dealer has 4-6"
        elif total in [17, 18]:
            advice = "Advice: Stand (Stay)"
        elif total >= 19:
            advice = "Advice: Stand (Stay) — strong hand!"
        else:
            advice = "Advice: Follow standard strategy."

        self.label_advice.config(text=advice)

    def check_result(self):
        dealer_total = sum(self.dealer_hand)
        player_total = sum(self.player_hand)
        split_total = sum(self.split_hand) if self.split_hand else 0

        self.label_dealer.config(text=f"Dealer's cards: {self.dealer_hand}")  # Показать полные карты дилера

        result_msg = ""

        if player_total > 21:
            result_msg += "You lost — busted!"
        elif dealer_total > 21 or player_total > dealer_total:
            result_msg += "You win!"
            self.balance += self.bet * 2
        elif player_total == dealer_total:
            result_msg += "Push — tie!"
            self.balance += self.bet
        else:
            result_msg += "Dealer wins!"

        if split_total:
            result_msg += f"\nSplit hand score: {split_total}"
            if split_total > 21:
                result_msg += "\nSplit hand busted!"
            elif split_total > dealer_total or dealer_total > 21:
                result_msg += "\nSplit hand wins!"
                self.balance += self.bet * 2
            elif split_total == dealer_total:
                result_msg += "\nSplit hand push!"
                self.balance += self.bet
            else:
                result_msg += "\nSplit hand loses!"

        self.label_result.config(text=result_msg)
        self.label_balance.config(text=f"Balance: {self.balance} chips")

    def show_leaderboard(self):
        if not os.path.exists("leaderboard.txt"):
            messagebox.showinfo("Leaderboard", "No leaderboard data available.")
            return

        with open("leaderboard.txt", "r") as file:
            scores = file.readlines()
        scores = [line.strip() for line in scores]
        scores.sort(key=lambda x: int(x.split(": ")[1]), reverse=True)
        top_scores = "\n".join(scores[:5])
        messagebox.showinfo("Leaderboard - Top 5 Players", top_scores)

if __name__ == "__main__":
    root = tk.Tk()
    game = BlackjackGame(root)
    root.mainloop()
