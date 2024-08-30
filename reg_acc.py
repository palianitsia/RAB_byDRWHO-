import random
import string
import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import subprocess
import time
from playwright.sync_api import sync_playwright

# Lista di proxy server gratuiti
PROXY_LIST = [
    "http://proxy1.example.com:8080",
    "http://proxy2.example.com:8080",
    "http://proxy3.example.com:8080",
    # Aggiungi altri proxy gratuiti che trovi affidabili
]

# Lista di paesi disponibili per la VPN (esempio)
VPN_COUNTRIES = [
    "United States",
    "Canada",
    "United Kingdom",
    "Germany",
    "Netherlands",
    # Aggiungi altri paesi supportati dalle VPN
]

# Funzione per generare email casuale
def generate_random_email(domain):
    length = random.randint(8, 15)
    email = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return email + domain

# Funzione per generare username casuale
def generate_random_username():
    length = random.randint(4, 8)
    username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
    return username

# Funzione per generare password casuale
def generate_random_password():
    length = random.randint(8, 12)
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
    return password

# Funzione per avviare la VPN e cambiare il paese
def start_vpn_and_change_country(vpn_path, vpn_name):
    # Scegli un paese casuale dalla lista
    country = random.choice(VPN_COUNTRIES)
    
    # Comandi specifici per avviare e cambiare paese per ciascuna VPN
    if vpn_name == "NordVPN":
        subprocess.run([vpn_path, "-c", "-g", country], check=True)  # Comando per NordVPN
    elif vpn_name == "ExpressVPN":
        subprocess.run([vpn_path, "connect", country], check=True)  # Comando per ExpressVPN
    elif vpn_name == "SharkVPN":
        subprocess.run([vpn_path, "-c", country], check=True)  # Comando per SharkVPN

# Funzione principale per eseguire la registrazione
def register_account():
    vpn_path = None
    if use_vpn_var.get():
        vpn_path = filedialog.askopenfilename(title="Seleziona il file eseguibile della VPN")

    num_registrations = 1
    if use_multi_reg_var.get() and multi_reg_entry.get().isdigit():
        num_registrations = int(multi_reg_entry.get())

    for i in range(num_registrations):
        # Seleziona un proxy casuale se le registrazioni multiple sono attive
        proxy = None
        if use_multi_reg_var.get():
            proxy = random.choice(PROXY_LIST)
        
        # Avvia e configura la VPN se richiesto
        if vpn_path:
            start_vpn_and_change_country(vpn_path, vpn_option_var.get())
        
        with sync_playwright() as playwright:
            if proxy:
                browser = playwright.chromium.launch(headless=False, proxy={"server": proxy})
            else:
                browser = playwright.chromium.launch(headless=False)
                
            context = browser.new_context(viewport={"width": 375, "height": 812}, is_mobile=True)
            page = context.new_page()

            # Determina la versione del sito da usare (it o es)
            base_url = "https://it.bidoo.com" if lang_var.get() == "it" else "https://es.bidoo.com"

            invite_link = invite_link_entry.get() if use_invite_var.get() else None
            if invite_link:
                page.goto(invite_link.replace("it.bidoo.com", base_url.split("//")[1]))
            else:
                page.goto(base_url)

            # Clicca sul bottone "Iscriviti"
            page.wait_for_selector('a#register_btn').click()

            # Email
            email = custom_email_entry.get() if use_custom_email_var.get() else generate_random_email(email_domain_var.get())
            page.fill('input#email_signup.email-reg.email.form-control', email)

            # Username
            username = custom_username_entry.get() if use_custom_username_var.get() else generate_random_username()
            page.fill('input.user-reg.user.form-control.username', username)

            # Password
            password = generate_random_password()
            page.fill('input#password_signup.pwd-reg.pwd.form-control.password', password)

            # Accetta Termini
            page.check('label.policy-checkbox.checkbox-inline input')

            # Registrati
            page.click('button#btnRegister.btlogin.btn-join.btn.btn-grey.btn-lg.btn-block.signup-btn')

            # Attendere il caricamento della pagina di destinazione
            while True:
                time.sleep(2)  # Attendere 2 secondi tra i controlli
                current_url = page.url

                # Controlla se la registrazione è stata completata con successo
                if f"{base_url}/home_alt.php?onboard=false&nu=true" in current_url:
                    time.sleep(2)  # Attendere 2 secondi prima di chiudere il browser
                    break

                if use_invite_var.get() and f"{base_url}/home_alt.php?onboard=false&nu=true&fr=" + invite_link_entry.get() in current_url:
                    time.sleep(2)  # Attendere 2 secondi prima di chiudere il browser
                    break

            # Salva i dati nel file acc.txt (aggiungendo senza cancellare)
            with open("acc.txt", "a") as file:
                file.write(f"{email}/{username}/{password}\n")

            context.close()
            browser.close()

        # Mostra il popup di successo
        if i == num_registrations - 1:
            if lang_var.get() == "it":
                messagebox.showinfo("Registrazione Completa", f"{num_registrations} registrazioni effettuate con successo!")
            else:
                messagebox.showinfo("Registro Completo", f"¡{num_registrations} registros completados con éxito!")
        
        # Attendere 5 secondi prima di avviare la prossima registrazione, se applicabile
        if i < num_registrations - 1:
            time.sleep(5)

# Funzione per aggiornare i testi della GUI in base alla lingua selezionata
def update_language():
    if lang_var.get() == "it":
        label_email.config(text="Inserire email personale?")
        label_domain.config(text="Finale Email:")
        label_username.config(text="Inserire username personale?")
        label_invite.config(text="Usare Link di Invito")
        label_multi_reg.config(text="Effettuare registrazioni multiple?")
        label_vpn.config(text="Usare VPN?")
        label_vpn_option.config(text="Seleziona VPN:")
        label_language.config(text="Lingua:")
        register_button.config(text="Registrati")
    else:
        label_email.config(text="¿Ingresar correo electrónico personal?")
        label_domain.config(text="Dominio de Correo:")
        label_username.config(text="¿Ingresar nombre de usuario personal?")
        label_invite.config(text="Usar enlace de invitación")
        label_multi_reg.config(text="¿Realizar registros múltiples?")
        label_vpn.config(text="¿Usar VPN?")
        label_vpn_option.config(text="Selecciona VPN:")
        label_language.config(text="Idioma:")
        register_button.config(text="Registrar")

# Creazione della finestra principale
root = tk.Tk()
root.title("RAB_byDRWHO?!_pwrdbyGPT")

# Checkbox e input per l'email
use_custom_email_var = tk.IntVar()
label_email = tk.Checkbutton(root, text="Inserire email personale?", variable=use_custom_email_var)
label_email.grid(row=0, column=0, sticky='w')
custom_email_entry = tk.Entry(root, width=30)
custom_email_entry.grid(row=0, column=1)

# Selettore per il dominio dell'email
label_domain = tk.Label(root, text="Finale Email:")
label_domain.grid(row=1, column=0, sticky='w')
email_domain_var = tk.StringVar(value="@yopmail.com")
ttk.Combobox(root, textvariable=email_domain_var, values=["@yopmail.com", "@gmail.com"]).grid(row=1, column=1)

# Checkbox e input per l'username
use_custom_username_var = tk.IntVar()
label_username = tk.Checkbutton(root, text="Inserire username personale?", variable=use_custom_username_var)
label_username.grid(row=2, column=0, sticky='w')
custom_username_entry = tk.Entry(root, width=30)
custom_username_entry.grid(row=2, column=1)

# Checkbox e input per il link di invito
use_invite_var = tk.IntVar()
label_invite = tk.Checkbutton(root, text="Usare Link di Invito", variable=use_invite_var)
label_invite.grid(row=3, column=0, sticky='w')
invite_link_entry = tk.Entry(root, width=50)
invite_link_entry.grid(row=3, column=1)

# Checkbox e input per il numero di registrazioni multiple
use_multi_reg_var = tk.IntVar()
label_multi_reg = tk.Checkbutton(root, text="Effettuare registrazioni multiple?", variable=use_multi_reg_var)
label_multi_reg.grid(row=4, column=0, sticky='w')
multi_reg_entry = tk.Entry(root, width=10)
multi_reg_entry.grid(row=4, column=1)

# Checkbox per usare la VPN
use_vpn_var = tk.IntVar()
label_vpn = tk.Checkbutton(root, text="Usare VPN?", variable=use_vpn_var)
label_vpn.grid(row=5, column=0, sticky='w')

# Selettore per la VPN
label_vpn_option = tk.Label(root, text="Seleziona VPN:")
label_vpn_option.grid(row=6, column=0, sticky='w')
vpn_option_var = tk.StringVar(value="NordVPN")
ttk.Combobox(root, textvariable=vpn_option_var, values=["NordVPN", "ExpressVPN", "SharkVPN"]).grid(row=6, column=1)

# Checkbox per selezionare la lingua (IT/ES)
label_language = tk.Label(root, text="Lingua:")
label_language.grid(row=7, column=0, sticky='w')
lang_var = tk.StringVar(value="it")
tk.Radiobutton(root, text="IT", variable=lang_var, value="it", command=update_language).grid(row=7, column=1, sticky='w')
tk.Radiobutton(root, text="ES", variable=lang_var, value="es", command=update_language).grid(row=7, column=2, sticky='w')

# Bottone per avviare la registrazione
register_button = tk.Button(root, text="Registrati", command=register_account)
register_button.grid(row=8, column=0, columnspan=3)

# Avvio della finestra principale
root.mainloop()
