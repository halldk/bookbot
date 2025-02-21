import sys
from stats import get_word_count, get_char_stats, generate_report

def get_book_text(filepath:str):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    f_path = args[1]
    text = get_book_text(f_path)
    num_words = get_word_count(text)
    # print(f'{num_words} words found in the document')
    num_chars = get_char_stats(text)
    # print(num_chars)
    report = generate_report(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {f_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in report:
        for key, value in item.items():
            if key.isalpha():
                print(f"{key}: {value}")
    print("============= END ===============")


if __name__ == "__main__":
    main()