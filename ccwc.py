import sys

def count_bytes(stream):
    data = stream.read()
    return len(data.encode('utf-8'))

def count_lines(stream):
    return sum(1 for line in stream)

def count_words(stream):
    stream.seek(0)  # Reset stream position to the beginning
    content = stream.read()
    words = content.split()
    return len(words)

def process_input(option, stream):
    if option == '-c':
        return count_bytes(stream)
    elif option == '-l':
        return count_lines(stream)
    elif option == '-w':
        return count_words(stream)
    elif option == '-m':
        # This is the same as count_bytes in UTF-8
        return count_bytes(stream)
    else:  # Default case
        line_count = count_lines(stream)
        word_count = count_words(stream)
        byte_count = count_bytes(stream)
        return f"{line_count} {word_count} {byte_count}"

def main():
    if len(sys.argv) > 3:
        print("Usage: ccwc [-c|-l|-w|-m] [filename]")
        sys.exit(1)

    option = sys.argv[1] if len(sys.argv) > 1 and sys.argv[1].startswith('-') else 'default'
    filename = None
    if len(sys.argv) == 3:
        filename = sys.argv[2]
    elif len(sys.argv) == 2 and not sys.argv[1].startswith('-'):
        filename = sys.argv[1]

    if filename:
        with open(filename, 'r', encoding='utf-8', errors='ignore') as file:
            result = process_input(option, file)
    else:
        result = process_input(option, sys.stdin)

    print(result)

if __name__ == "__main__":
    main()

