
# Funktsioon juhusliku kaardi loomiseks (2-11 punkti)
def loe_kaart():
    return random.randint(2, 11)

# Funktsioon m�ngu tulemuse arvutamiseks
def arvuta_tulemus(mangija_summa, arvuti_summa):
    if mangija_summa > 21:
        return "Kaotus!", "Kaotasid, sest l�ksid �le 21."
    elif arvuti_summa > 21 or mangija_summa > arvuti_summa:
        return "V�it!", "V�itsid, kuna oled 21-le l�hemal."
    elif mangija_summa < arvuti_summa:
        return "Kaotus!", "Kaotasid, arvuti oli l�hemal 21-le."
    else:
        return "Viik!", "M�ng l�ppes viigiga."

# Funktsioon tulemuse salvestamiseks faili
def salvesta_tulemus(nimi, tulemus, punktid):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{nimi}: {tulemus} ({punktid} punkti)\n")

# Funktsioon arvutile m�ngu loomiseks
def m�ngi_arvuti():
    summa = 0
    while summa < 17:
        summa += loe_kaart()
    return summa

# Funktsioon ajaloo kuvamiseks
def n�ita_ajalugu():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            ajalugu = f.read()
        messagebox.showinfo("M�ngu ajalugu", ajalugu if ajalugu else "Ajalugu on t�hi.")
    except FileNotFoundError:
        messagebox.showinfo("M�ngu ajalugu", "Ajalugu on t�hi.")

# GUI loomine
class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("M�ng 21")
        
        self.nimi_var = tk.StringVar()
        self.summa = 0
        
        tk.Label(root, text="Sisesta oma nimi:").pack()
        tk.Entry(root, textvariable=self.nimi_var).pack()
        
        self.kaardid_label = tk.Label(root, text="Kaardid: ")
        self.kaardid_label.pack()
        
        self.summa_label = tk.Label(root, text="Summa: 0")
        self.summa_label.pack()
        
        tk.Button(root, text="Alusta m�ngu", command=self.alusta_m�ngu).pack()
        tk.Button(root, text="V�ta kaart", command=self.v�ta_kaart).pack()
        tk.Button(root, text="Peatu", command=self.peatu).pack()
        tk.Button(root, text="Vaata ajalugu", command=n�ita_ajalugu).pack()
        
    def alusta_m�ngu(self):
        self.summa = loe_kaart() + loe_kaart()
        self.kaardid_label.config(text=f"Kaardid: {self.summa}")
        self.summa_label.config(text=f"Summa: {self.summa}")
    
    def v�ta_kaart(self):
        self.summa += loe_kaart()
        self.summa_label.config(text=f"Summa: {self.summa}")
        if self.summa > 21:
            self.peatu()
    
    def peatu(self):
        arvuti_summa = m�ngi_arvuti()
        tulemus, s�num = arvuta_tulemus(self.summa, arvuti_summa)
        salvesta_tulemus(self.nimi_var.get() or "M�ngija", tulemus, self.summa)
        messagebox.showinfo(tulemus, s�num)
        self.summa = 0
        self.summa_label.config(text="Summa: 0")
        self.kaardid_label.config(text="Kaardid: ")

