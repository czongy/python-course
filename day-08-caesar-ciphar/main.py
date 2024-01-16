import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
to_continue = True

def encode(msg, sft):
    enc_msg = ""
    for x in msg:
        if x.isspace():
            enc_msg += " "
        else:
            x_index = alphabet.index(x)
            enc_msg += alphabet[x_index + sft]
    return enc_msg

def decrypt(msg, sft):
    dec_msg = ""
    for x in msg:
        if x.isspace():
            dec_msg += " "
        else:
            x_index = alphabet.index(x)
            dec_msg += alphabet[x_index - sft]
    return dec_msg

def caesar():
    action = input("\nType 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message (only alphabet): \n").lower()
    shift = input("Type the shift numebr: \n")

    if action == "encode" and shift.isnumeric() and not any(i.isdigit() for i in message):
        sft = int(shift) % 26
        result = encode(message, sft)
    elif action == "decode" and shift.isnumeric() and not any(i.isdigit() for i in message):
        sft = int(shift) % 26
        result = decrypt(message, sft)
    else:
        print("Invalid input. Please try again.")
        caesar()

    print(f"Here's the {action}d result:\n{result}")

print(art.logo)
while to_continue:
    caesar()
    check = input("\nType 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if check == "no":
        to_continue = False