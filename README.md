# RSA Encryption using tkinter

This code provides a basic GUI interface for performing RSA encryption on input text. The program uses the `rsa` module to generate public and private keys and then provides options to encrypt and decrypt text using the generated keys.

![image](https://user-images.githubusercontent.com/87757968/213925246-77e782e3-a87c-4f4f-a458-8fb0e30e77a9.png)


## Prerequisites

-   Python 3.x
-   tkinter module
-   rsa module

To install the required modules, run the following command:

`pip3 install rsa` 

Note: As `tkinter` is a standard Python library, there is no need to install it separately. It should already be available in your Python installation.

## Usage

-   Run the program `rsa_gui.py` using the command `python3 rsa_gui.py`.
-   Enter the text that needs to be encrypted in the input box and click the `Encrypt` button.
-   The encrypted text will be displayed in the `encrypted text (RSA)` field.
-   To decrypt the encrypted text, the `Decrypt` function is called using the private key.
-   The decrypted text will be displayed in the `decrypted text` field.

## Disclaimer

This program is provided as a basic illustration of RSA encryption and is not recommended for use in any secure system.
