## Project Overview
This project aims to recreate the classic Unix command line tool `wc` (word count). The Unix `wc` tool is a powerful utility used for counting the number of lines, words, characters, and bytes in text files. This project follows the Unix philosophy of writing simple parts connected by clean interfaces, resulting in a tool that does one thing but does it well.

## Features
- Count the number of bytes in a file (`-c` option).
- Count the number of lines in a file (`-l` option).
- Count the number of words in a file (`-w` option).
- Count the number of characters in a file (`-m` option), with support for multibyte characters depending on the locale.
- Default behavior without options to count lines, words, and bytes.
- Ability to read from standard input if no filename is specified, enabling integration with other command line tools.

## Getting Started

### Prerequisites
- Any standard IDE or text editor for Python development (e.g., Visual Studio Code, PyCharm).
- Python 3.x installed on your system.

### Setting Up Your Environment
1. Clone the repository to your local machine.
2. Save a text file (e.g., `test.txt`) in the project directory to test the functionalities of the tool.

### Usage
Run the tool from the command line using the Python interpreter. Here are some example commands:

- Count bytes: `python ccwc.py -c test.txt`
- Count lines: `python ccwc.py -l test.txt`
- Count words: `python ccwc.py -w test.txt`
- Count characters: `python ccwc.py -m test.txt`
- Default count (lines, words, bytes): `python ccwc.py test.txt`
- Read from stdin: `cat test.txt | python ccwc.py -l`

## Development Steps
The development of this tool was divided into several steps, each focusing on adding a specific feature:

1. **Step One**: Implement byte count functionality.
2. **Step Two**: Add support for counting lines.
3. **Step Three**: Introduce word count capability.
4. **Step Four**: Implement character count, considering multibyte characters.
5. **Step Five**: Combine byte, line, and word count for default option.
6. **Final Step**: Enable reading from standard input.

