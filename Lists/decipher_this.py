secret_message = input()

for message in secret_message:
    whats_the_word = ""
    secret_message = ""
    letters = []
    letters_str = ""
    whole_message = ""
    for msg in range(len(message)):
        current_later = message[msg]
        