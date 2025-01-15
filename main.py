def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        char_counts = char_analyze(file_contents)       
        print(f"Word Count: {word_count}")
        print(char_counts)

def count_words(string):
    words = string.split()
    return len(words)

def char_analyze(string):
    counts = {}
    lowered = string.lower()
    for char in lowered:
        if char not in counts:
            counts[char] = 1
        else:
            counts[char] += 1
    return counts

main()