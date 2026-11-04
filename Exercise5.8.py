# Exercise 5.8
usernames = ['fikri', 'budi', 'admin', 'sari', 'andi']
for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {username.title()}, thank you for logging in again.")