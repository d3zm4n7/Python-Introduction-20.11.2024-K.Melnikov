import tkinter as tk
from tkinter import ttk, messagebox, filedialog, OptionMenu
import smtplib
from email.message import EmailMessage
import mimetypes
import os
import json



auto_attachments = ["photo.jpg", "photo2.jpg"]  # или любой другой файл в папке со скриптом
SIGNATURE = "\n\nBest regards,\nKerja 😎\nhttps://kirillmelnikov24.thkit.ee/wp/"
SETTINGS_FILE = "settings.json"

def add_attachments():
    files = filedialog.askopenfilenames(title="Vali failid")
    if files:
        attached_files.extend(files)
        update_attachment_list()

def update_attachment_list():
    attachment_listbox.delete(0, tk.END)
    for file in attached_files:
        attachment_listbox.insert(tk.END, os.path.basename(file))

def clear_attachments():
    attached_files.clear()
    update_attachment_list()
    save_settings()

def send_email_multi(sender, password, recipients_string, subject, body):
    recipient_list = [email.strip() for email in recipients_string.split(',') if email.strip()]
    if not recipient_list:
        messagebox.showerror("Viga", "Palun sisesta vähemalt üks korrektne e-maili aadress.")
        return

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ", ".join(recipient_list)
    msg.set_content(body)

# Добавляем либо auto_attachments, либо attached_files (но не оба)
    files_to_attach = attached_files if attached_files else auto_attachments

    for file_path in files_to_attach:
        if os.path.exists(file_path):
            mime_type, _ = mimetypes.guess_type(file_path)
            mime_type = mime_type or 'application/octet-stream'
            main_type, sub_type = mime_type.split('/', 1) 
            with open(file_path, 'rb') as f:
                msg.add_attachment(f.read(),
                                   maintype=main_type,
                                   subtype=sub_type,
                                   filename=os.path.basename(file_path))

    # 📎 Вложения вручную
    for file_path in attached_files:
        if os.path.exists(file_path):
            mime_type, _ = mimetypes.guess_type(file_path)
            mime_type = mime_type or 'application/octet-stream'
            main_type, sub_type = mime_type.split('/', 1)
            with open(file_path, 'rb') as f:
                msg.add_attachment(f.read(),
                                   maintype=main_type,
                                   subtype=sub_type,
                                   filename=os.path.basename(file_path))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.login(sender, password)
            smtp.send_message(msg)
            messagebox.showinfo("Edukas", "E-kiri saadetud koos manustega!")
    except Exception as e:
        messagebox.showerror("Viga", f"Midagi läks valesti:\n{e}")

def send_multi_direct():
    sender = sender_entry.get()
    password = password_entry.get()
    recipients = recipient_entry.get()
    subject = subject_entry.get()
    body = body_text.get("1.0", tk.END).strip()

    if not sender or not password or not recipients or not subject or not body:
        messagebox.showerror("Viga", "Täida kõik väljad.")
        return

    if include_signature.get():
        body += SIGNATURE

    send_email_multi(sender, password, recipients, subject, body)

def save_draft():
    with open("draft.txt", "w", encoding="utf-8") as f:
        f.write(body_text.get("1.0", tk.END).strip())

def fill_example():
    sender_entry.delete(0, tk.END)
    sender_entry.insert(0, "dezxplay@gmail.com")

    password_entry.delete(0, tk.END)
    password_entry.insert(0, "mszztnoatpptjvvw")

    recipient_entry.delete(0, tk.END)
    recipient_entry.insert(0, "t002@bk.ru, marina.oleinik@tthk.ee")

    subject_entry.delete(0, tk.END)
    subject_entry.insert(0, "Test email from Tkinter")

    body_text.delete("1.0", tk.END)
    body_text.insert("1.0", "Tere!\n\nSee on test-sõnum saatmiseks mitmele kasutajale koos manustega.")

def clear_fields():
    sender_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)
    recipient_entry.delete(0, tk.END)
    subject_entry.delete(0, tk.END)
    body_text.delete("1.0", tk.END)
    attached_files.clear()
    update_attachment_list()

def apply_theme(theme_name):
    def set_all_styles(bg_root, bg_frame, fg, entry_bg="#ffffff", text_bg="#ffffff"):
        root.configure(bg=bg_root)

        style.theme_use("clam")

        # 👇 Создаём уникальный стиль для каждой темы
        frame_style_name = f"{theme_name}.TFrame"
        labelframe_style = f"{theme_name}.TLabelframe"
        main_frame.configure(style=frame_style_name)
        style.configure(frame_style_name, background=bg_frame)

        style.configure("TLabel", background=bg_frame, foreground=fg)
        style.configure("TEntry", fieldbackground=entry_bg, foreground=fg)
        style.configure("TButton", background=entry_bg, foreground=fg)
        style.configure("TCheckbutton", background=bg_frame, foreground=fg)
        style.configure("TLabelframe", background=bg_frame, foreground=fg)
        style.configure(labelframe_style, background=bg_frame, foreground=fg)
        style.configure(f"{labelframe_style}.Label", background=bg_frame, foreground=fg)
        body_text.configure(bg=text_bg, fg=fg, insertbackground=fg)
        attachment_listbox.configure(bg=text_bg, fg=fg)
        attachments_frame.configure(style=labelframe_style)

        # Меняем OptionMenu цвета
        theme_menu.config(bg=bg_frame, fg=fg, activebackground=bg_frame, activeforeground=fg, highlightthickness=0, borderwidth=0)
        theme_menu["menu"].config(bg=bg_frame, fg=fg, activebackground=bg_frame, activeforeground=fg)

    if theme_name == "Standard":
        set_all_styles(bg_root="#f2f2f2", bg_frame="#ffffff", fg="#000000")

    elif theme_name == "Tume":
        set_all_styles(bg_root="#0e0e0e", bg_frame="#121212", fg="#e0e0e0", entry_bg="#1e1e1e", text_bg="#1e1e1e")

    elif theme_name == "Roosa":
        set_all_styles(bg_root="#fddde6", bg_frame="#ffe6f0", fg="#800040", entry_bg="#ffffff", text_bg="#fff0f5")

    elif theme_name == "Sinine":
        set_all_styles(bg_root="#d6ebff", bg_frame="#e6f2ff", fg="#003366", entry_bg="#ffffff")

    elif theme_name == "Roheline":
        set_all_styles(bg_root="#dcedc8", bg_frame="#e8f5e9", fg="#1b5e20", entry_bg="#ffffff")

    elif theme_name == "Monokroomne":
        set_all_styles(bg_root="#c0c0c0", bg_frame="#dcdcdc", fg="#2e2e2e", entry_bg="#f0f0f0", text_bg="#f0f0f0")



def save_settings():
    settings = {
        "theme": current_theme.get(),
        "attachments": attached_files,
        "sender": sender_entry.get(),
        "recipients": recipient_entry.get(),
        "subject": subject_entry.get(),
        "body": body_text.get("1.0", tk.END).strip()
    }
    with open(SETTINGS_FILE, "w", encoding="utf-8") as f:
        json.dump(settings, f, indent=4)

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}

# --- GUI ---
root = tk.Tk()
root.title("Gmailiga kirja saatmine")
root.geometry("540x560")

style = ttk.Style()
style.configure("TLabel", font=("Arial", 11))
style.configure("TButton", font=("Arial", 11))
style.configure("TEntry", font=("Arial", 11))

include_signature = tk.BooleanVar(value=True)
main_frame = ttk.Frame(root, padding=10)
main_frame.grid(row=0, column=0, sticky="nsew")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

# 📬 Ввод
ttk.Label(main_frame, text="Sinu Gmail:").grid(row=0, column=0, sticky="w")
sender_entry = ttk.Entry(main_frame, width=50)
sender_entry.insert(0, "dezxplay@gmail.com")
sender_entry.grid(row=0, column=1, padx=5, pady=2)

ttk.Label(main_frame, text="App Password:").grid(row=1, column=0, sticky="w")
password_entry = ttk.Entry(main_frame, width=50, show="*")
password_entry.insert(0, "mszztnoatpptjvvw")
password_entry.grid(row=1, column=1, padx=5, pady=2)

ttk.Label(main_frame, text="Saaja email(id):").grid(row=2, column=0, sticky="w")
recipient_entry = ttk.Entry(main_frame, width=50)
recipient_entry.insert(0, "dezxplay@gmail.com")
recipient_entry.grid(row=2, column=1, padx=5, pady=2)

ttk.Label(main_frame, text="Teema:").grid(row=3, column=0, sticky="w")
subject_entry = ttk.Entry(main_frame, width=50)
subject_entry.insert(0, "Hello World!")
subject_entry.grid(row=3, column=1, padx=5, pady=2)

ttk.Label(main_frame, text="Sõnum:").grid(row=4, column=0, sticky="nw")
body_text = tk.Text(main_frame, height=6, width=50)
body_text.grid(row=4, column=1, padx=5, pady=5)

# 📥 Загрузка черновика
try:
    with open("draft.txt", "r", encoding="utf-8") as f:
        body_text.insert("1.0", f.read())
except FileNotFoundError:
    pass

# 📎 Вложения
attachments_frame = ttk.LabelFrame(main_frame, text="Manused", padding=10)
attachments_frame.grid(row=5, column=0, columnspan=2, pady=10, sticky="ew")

ttk.Button(attachments_frame, text="📎Lisa manused", command=add_attachments).grid(row=0, column=0, sticky="w")
attachment_listbox = tk.Listbox(attachments_frame, height=4, width=60)
attachment_listbox.grid(row=1, column=0, pady=5)

ttk.Button(attachments_frame, text="Eemalda kõik manused", command=clear_attachments).grid(row=0, column=1, padx=5)

# 📤 Кнопка отправки
ttk.Checkbutton(main_frame, text="Lisa allkiri", variable=include_signature).grid(row=8, column=0, columnspan=1, sticky="w", padx=5)
ttk.Button(main_frame, text="Saada kiri", command=send_multi_direct).grid(row=8, column=1, columnspan=2, pady=15)

theme_options = ["Standard", "Tume", "Roosa", "Sinine", "Roheline", "Monokroomne"]
# Загружаем настройки
loaded_settings = load_settings()

# Тема
initial_theme = loaded_settings.get("theme", "Standard")
current_theme = tk.StringVar(value=initial_theme)

# Вложения
attached_files = loaded_settings.get("attachments", [])
update_attachment_list()

# Восстановим текстовые поля
sender_entry.delete(0, tk.END)
sender_entry.insert(0, loaded_settings.get("sender", ""))

recipient_entry.delete(0, tk.END)
recipient_entry.insert(0, loaded_settings.get("recipients", ""))

subject_entry.delete(0, tk.END)
subject_entry.insert(0, loaded_settings.get("subject", ""))

body_text.delete("1.0", tk.END)
body_text.insert("1.0", loaded_settings.get("body", ""))
include_signature.set(loaded_settings.get("signature", True))
 

ttk.Label(main_frame, text="Vali teema:").grid(row=9, column=0, sticky="e", padx=5)
theme_menu = OptionMenu(main_frame, current_theme, "Standard", "Tume", "Roosa", "Sinine", "Roheline", "Monokroomne", command=lambda t: apply_theme(t))
theme_menu.grid(row=9, column=1, sticky="w", padx=5)

ttk.Button(main_frame, text="Täida näidis", command=fill_example).grid(row=7, column=0, pady=(5, 10))
ttk.Button(main_frame, text="Tühjenda vorm", command=clear_fields).grid(row=7, column=1, pady=(5, 10))


update_attachment_list()


# 💾 Сохраняем черновик при выходе
root.protocol("WM_DELETE_WINDOW", lambda: [save_draft(), save_settings(), root.destroy()])
apply_theme(current_theme.get())
root.mainloop()
