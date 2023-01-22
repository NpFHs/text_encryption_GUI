import tkinter as tk
import rsa

public_key, private_key = rsa.newkeys(512)


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
    win.geometry("500x300")
    text = tk.StringVar()
    enc_message = tk.StringVar()
    dec_message = tk.StringVar()

    original_text_label = tk.Label(textvariable=text)
    original_text_label.pack(side="top", padx=10, pady=10, fill="x")
    enc_label = tk.Label(textvariable=enc_message)
    enc_label.pack(side="top", padx=10, pady=10, fill="x")
    dec_label = tk.Label(textvariable=dec_message)
    dec_label.pack(side="top", padx=10, pady=10, fill="x")
    button = tk.Button(text="Encrypt", command=lambda: func(text.get(), enc_message, dec_message))
    button.pack(side="bottom", fill="x", padx=10, pady=10)
    entry = tk.Entry(textvariable=text)
    entry.bind("<Return>", lambda event: func(text.get(), enc_message, dec_message))
    entry.pack(side="bottom", fill="x", padx=10)
    win.mainloop()


if __name__ == "__main__":
    main()
