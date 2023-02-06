import tkinter as tk
import os

os.system("pip3 install rsa")
import rsa  # NOQA: E402

public_key, private_key = rsa.newkeys(2048)
COLOR = "#d28536"


def encrypt(message, enc_message):
    enc = rsa.encrypt(message.encode(), public_key)

    new_enc = enc.replace(b"\n", b"").replace(b"\r", b"")
    enc_message.set(new_enc)
    return enc


def decrypt(enc, dec_message):
    dec = rsa.decrypt(enc, private_key)
    dec_message.set(dec.decode())


def func(message, enc_message, dec_message):
    enc = encrypt(message, enc_message)
    decrypt(enc, dec_message)


def main():
    win = tk.Tk()
    win.title("RSA encryption")
    win.geometry("650x350")
    win.config(bg=COLOR)
    text = tk.StringVar()
    enc_message = tk.StringVar()
    dec_message = tk.StringVar()

    original_text_title_label = tk.Label(text="original text:", font=("Ariel", "11", "bold"), bg=COLOR)
    original_text_title_label.pack(side="top", padx=10, pady=10, fill="x")
    original_text_label = tk.Label(textvariable=text, font=("Ariel", "11", "italic"), bg=COLOR)
    original_text_label.pack(side="top", padx=10, fill="x")

    enc_title_label = tk.Label(text="encrypted text (RSA):", font=("Ariel", "11", "bold"), bg=COLOR)
    enc_title_label.pack(side="top", padx=10, pady=10, fill="x")
    enc_label = tk.Label(textvariable=enc_message, font=("Ariel", "11", "italic"), bg=COLOR)
    enc_label.pack(side="top", padx=10, fill="x")

    dec_title_label = tk.Label(text="decrypted text:", font=("Ariel", "11", "bold"), bg=COLOR)
    dec_title_label.pack(side="top", padx=10, pady=10, fill="x")
    dec_label = tk.Label(textvariable=dec_message, font=("Ariel", "11", "italic"), bg=COLOR)
    dec_label.pack(side="top", padx=10, fill="x")

    button = tk.Button(text="Encrypt", command=lambda: func(text.get(), enc_message, dec_message), bd=4, bg="#a57699")
    button.pack(side="bottom", fill="x", padx=10, pady=10)
    entry = tk.Entry(textvariable=text)
    entry.bind("<Return>", lambda event: func(text.get(), enc_message, dec_message))
    entry.pack(side="bottom", fill="x", padx=10)

    win.mainloop()


if __name__ == "__main__":
    main()
