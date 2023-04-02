import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

main_window = ctk.CTk()
main_window.geometry("400x200")
main_window.title("Login")

def login_click():
    print("Fazer login")

def validate_email():
    if "@" in email_entry.get():
        return True
    else:
        print("Endereço de e-mail inválido")
        return False

login_label = ctk.CTkLabel(main_window, text="Fazer login")

email_entry = ctk.CTkEntry(main_window, placeholder_text="E-mail")
email_entry.configure(validate="focusout", validatecommand=validate_email)
email_entry.register(validate_email)

password_entry = ctk.CTkEntry(main_window, placeholder_text="Senha", show="*")

login_button = ctk.CTkButton(main_window, text="Login", command=login_click)

login_label.grid(row=0, column=0, padx=10, pady=10)

email_entry.grid(row=1, column=0, padx=10, pady=10)

password_entry.grid(row=2, column=0, padx=10, pady=10)

login_button.grid(row=3, column=0, padx=10, pady=10)

main_window.mainloop()
