
# Funktsioon juhusliku kaardi loomiseks (2-11 punkti)
def loe_kaart():
    return random.randint(2, 11)

# Funktsioon mängu tulemuse arvutamiseks
def arvuta_tulemus(mangija_summa, arvuti_summa):
    if mangija_summa > 21:
        return "Kaotus!", "Kaotasid, sest läksid üle 21."
    elif arvuti_summa > 21 or mangija_summa > arvuti_summa:
        return "Võit!", "Võitsid, kuna oled 21-le lähemal."
    elif mangija_summa < arvuti_summa:
        return "Kaotus!", "Kaotasid, arvuti oli lähemal 21-le."
    else:
        return "Viik!", "Mäng lõppes viigiga."

# Funktsioon tulemuse salvestamiseks faili
def salvesta_tulemus(nimi, tulemus, punktid):
    with open(HISTORY_FILE, "a", encoding="utf-8") as f:
        f.write(f"{nimi}: {tulemus} ({punktid} punkti)\n")

# Funktsioon arvutile mängu loomiseks
def mängi_arvuti():
    summa = 0
    while summa < 17:
        summa += loe_kaart()
    return summa

# Funktsioon ajaloo kuvamiseks
def näita_ajalugu():
    try:
        with open(HISTORY_FILE, "r", encoding="utf-8") as f:
            ajalugu = f.read()
        messagebox.showinfo("Mängu ajalugu", ajalugu if ajalugu else "Ajalugu on tühi.")
    except FileNotFoundError:
        messagebox.showinfo("Mängu ajalugu", "Ajalugu on tühi.")

# GUI loomine
class BlackjackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Mäng 21")
        
        self.nimi_var = tk.StringVar()
        self.summa = 0
        
        tk.Label(root, text="Sisesta oma nimi:").pack()
        tk.Entry(root, textvariable=self.nimi_var).pack()
        
        self.kaardid_label = tk.Label(root, text="Kaardid: ")
        self.kaardid_label.pack()
        
        self.summa_label = tk.Label(root, text="Summa: 0")
        self.summa_label.pack()
        
        tk.Button(root, text="Alusta mängu", command=self.alusta_mängu).pack()
        tk.Button(root, text="Võta kaart", command=self.võta_kaart).pack()
        tk.Button(root, text="Peatu", command=self.peatu).pack()
        tk.Button(root, text="Vaata ajalugu", command=näita_ajalugu).pack()
        
    def alusta_mängu(self):
        self.summa = loe_kaart() + loe_kaart()
        self.kaardid_label.config(text=f"Kaardid: {self.summa}")
        self.summa_label.config(text=f"Summa: {self.summa}")
    
    def võta_kaart(self):
        self.summa += loe_kaart()
        self.summa_label.config(text=f"Summa: {self.summa}")
        if self.summa > 21:
            self.peatu()
    
    def peatu(self):
        arvuti_summa = mängi_arvuti()
        tulemus, sõnum = arvuta_tulemus(self.summa, arvuti_summa)
        salvesta_tulemus(self.nimi_var.get() or "Mängija", tulemus, self.summa)
        messagebox.showinfo(tulemus, sõnum)
        self.summa = 0
        self.summa_label.config(text="Summa: 0")
        self.kaardid_label.config(text="Kaardid: ")

