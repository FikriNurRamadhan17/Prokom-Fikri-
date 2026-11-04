# Exercise 8.10
def send_messages(messages, sent_messages):
    """Cetak tiap pesan lalu pindahkan ke sent_messages."""
    while messages:
        current = messages.pop()
        print(f"Mengirim: {current}")
        sent_messages.append(current)


texts = ['Halo!', 'Sudah makan belum?', 'Jangan lupa tugas Python.']
sent_messages = []

send_messages(texts, sent_messages)

print("\nList texts:", texts)
print("List sent_messages:", sent_messages)
