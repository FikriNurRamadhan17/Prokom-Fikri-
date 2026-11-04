# Exercise 5.10
current_users = ['Fikri', 'Budi', 'Sari', 'Andi', 'Dimas']
new_users = ['fikri', 'Kelvin', 'SARI', 'Haykal', 'Rina']

current_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_lower:
        print(f"{new_user}: username sudah dipakai, masukkan yang lain.")
    else:
        print(f"{new_user}: username tersedia.")