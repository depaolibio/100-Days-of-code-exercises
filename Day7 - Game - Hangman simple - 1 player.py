import random

#functions needed
def find_all_occurrences_loop(text, char):
    positions = []
    start_index = 0
    while True:
        index = text.find(char, start_index)
        if index == -1:  # Character not found
            break
        positions.append(index)
        start_index = index + 1  # Start searching from the next position
    return positions

def exchange_characters(list1, list2, positions):
    """
    Exchanges characters at specified positions between two lists.

    Args:
      list1: The first list.
      list2: The second list.
      positions: A list of integers representing the indices at which to exchange characters.
                 All lists must have identical length and positions must be valid indices.

    Returns:
      None. The lists are modified in-place.
    """
    if len(list1) != len(list2):
        raise ValueError("Lists must have identical length.")

    for pos in positions:
        if not (0 <= pos < len(list1)):
            raise IndexError(f"Position {pos} is out of bounds for lists of length {len(list1)}.")

        # Swap the elements at the current position
        list1[pos], list2[pos] = list2[pos], list1[pos]

#code starts after functions
list_of_words = ["apple", "pear", "pie", "henrique", "mogno", "mississipi", "aardvark", "baboon", "camel"]
chosen_word = random.choice(list_of_words)
word_list = list(chosen_word)
replacement_symbol = "_"
word_list_empty_1 = [replacement_symbol for _ in word_list]
word_list_empty_2 = ''.join([replacement_symbol for _ in word_list])

#checkpoint1 selecting the word into a list
#print(chosen_word)
print("Welcome to HangMan Game")
mistakes = 5
print(f"Your word has {len(chosen_word)} letters.")
print(word_list_empty_2)

while mistakes != 0:
    ask = input("Type a letter to move on: ").lower()

    if ask in word_list:
        indices = find_all_occurrences_loop(chosen_word, ask)
        #print(f"The character '{ask}' appears at indices: {indices}")
        exchange_characters(word_list_empty_1, word_list, indices)

        target_char = '_'
        total_count = 0
        for word in word_list_empty_1:
            total_count += word.count(target_char)
        if total_count == 0:
                print(f"Congratulations, your word is {chosen_word}, you won!")
                exit()

    else:
        print("This character is not found in the present word")
        mistakes -=1
    print(f"You have {mistakes} mistakes left before being hang!")
    print(''.join(word_list_empty_1))

print(f"Too many wrong attempts... GAME OVER, sorry. The word was {chosen_word}.")
