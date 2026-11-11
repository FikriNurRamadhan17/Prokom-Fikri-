# Exercise 10-14
from pathlib import Path
import json


def get_stored_username(path):
    """Ambil nama tersimpan kalau ada."""
    if path.exists():
        return json.loads(path.read_text())
    return None


def get_new_username(path):
    """Minta nama baru lalu simpan."""
    username = input("Siapa namamu? ")
    path.write_text(json.dumps(username))
    return username


def greet_user():
    """Sapa pengguna, pastikan dulu itu orang yang benar."""
    path = Path('username10_14.json')
    username = get_stored_username(path)

    if username:
        jawaban = input(f"Apakah kamu {username}? (y/n) ")
        if jawaban.lower() == 'y':
            print(f"Selamat datang kembali, {username}!")
        else:
            username = get_new_username(path)
            print(f"Oke, nanti aku ingat kamu, {username}!")
    else:
        username = get_new_username(path)
        print(f"Nanti aku ingat kamu, {username}!")


greet_user()