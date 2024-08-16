def calculate_word_count(input_text):
    word_list = input_text.split()
    return len(word_list)


def start_program():
    text_input = input("Please enter a sentence or paragraph: ").strip()

    if not text_input:
        print("Error: You entered an empty string. Please provide valid text.")
        return

    total_words = calculate_word_count(text_input)
    print(f"The number of words in the input is: {total_words}")


if __name__ == "__main__":
    start_program()
