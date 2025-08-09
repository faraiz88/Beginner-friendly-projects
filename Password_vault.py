import json
import os
from cryptography.fernet import Fernet

FILENAME = "vault.json"
KEYFILE = "vault.key"

# ----------------- Encryption Helpers -----------------
def load_key():
    """Load encryption key or create one if it doesn't exist."""
    if not os.path.exists(KEYFILE):
        key = Fernet.generate_key()
        with open(KEYFILE, "wb") as key_file:
            key_file.write(key)
    else:
        with open(KEYFILE, "rb") as key_file:
            key = key_file.read()
    return key

key = load_key()
fernet = Fernet(key)

# ----------------- File Setup -----------------
def credentials():
    """Ensure the vault file exists."""
    if not os.path.exists(FILENAME):
        with open(FILENAME, "w") as f:
            json.dump([], f, indent=4)

def saved_cred():
    """Read saved credentials from file."""
    with open(FILENAME, "r") as f:
        return json.load(f)

credentials()
allcred = saved_cred()

# ----------------- Menu -----------------
def display_options():
    print("\n--- Password Vault ---")
    print("1. Add a website, username, and password")
    print("2. View all saved credentials")
    print("3. Exit")

while True:
    display_options()
    a = input("Enter your choice: ")

    if a == "1":
        website = input("Enter your website: ")
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Encrypt the password before saving
        encrypted_password = fernet.encrypt(password.encode()).decode()

        data = {
            "Website": website,
            "Username": username,
            "Password": encrypted_password
        }
        allcred.append(data)

        with open(FILENAME, "w") as f:
            json.dump(allcred, f, indent=4)
        print("✅ Credentials saved successfully.")

    elif a == "2":
        if not allcred:
            print("No credentials saved to display!")
        else:
            for d in allcred:
                decrypted_password = fernet.decrypt(d["Password"].encode()).decode()
                print(f"Website: {d['Website']}, Username: {d['Username']}, Password: {decrypted_password}")

    elif a == "3":
        print("Exiting...")
        break

    else:
        print("❌ Invalid choice. Please try again.")
