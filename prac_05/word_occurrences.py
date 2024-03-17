def count_word_occurrences(text):
    word_counts = {}
    words = text.split()
    for word in words:
        word_counts[word] = word_counts.get(word, 0) + 1
    return word_counts


def print_word_counts(word_counts):
    max_word_length = max(len(word) for word in word_counts)
    for word, count in sorted(word_counts.items()):
        print(f"{word:{max_word_length}} : {count}")


def main():
    text = input("Enter a string: ")
    word_counts = count_word_occurrences(text)
    print("Word counts:")
    print_word_counts(word_counts)


main()
