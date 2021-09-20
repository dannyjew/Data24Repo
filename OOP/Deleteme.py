replay = True

while replay:
    guess_word = input("Please pick a word")

    def hidden_word_function(word_to_hide):
        return "_"*len(word_to_hide)


    hidden_word = hidden_word_function(guess_word)

    def reveals_letter_in_word(letter, original_word, current_hidden_word):
        print("hello")
    player_replay_str = input("Do you want to replay? please type Y/N")
    if player_replay_str == "N":
        replay = False

