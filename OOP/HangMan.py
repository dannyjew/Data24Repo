#    original_word -> hello
#    current_word -> __ll_
#    letter_to_reveal -> e


def character_reveal(letter_to_reveal: str, original_word: str, current_word: str):
    word = ""
    position = 0
    for letter in original_word:
        if letter == letter_to_reveal:
            word += letter
        else:
            if current_word[position] != "_":
                word += letter
            else:
                word += "_"
        position += 1
    return word


print(character_reveal("o", "hello", "_ell_"))