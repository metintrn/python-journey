from ceasar_art import art
print(art)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l',
            'm','n','o','p','q','r','s','t','u','v','w','x','y','z']

def caesar(original_text, shift_amount, direction):
    output_text = ""

    if direction == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
            continue   # 🔥 KRİTİK SATIR

        shift_position = alphabet.index(letter) + shift_amount
        shift_position %= len(alphabet)
        output_text += alphabet[shift_position]

    print(f"Your {direction}d text is: {output_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye 👋")
