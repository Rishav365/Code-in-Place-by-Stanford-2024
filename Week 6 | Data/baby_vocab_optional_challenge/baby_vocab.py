"""
Baby Vocab

Author: Rishav Dey
Date: 1st June 2024
Version: 1.0

Description:
This Python program analyzes a baby's vocabulary by counting occurrences of each word and generating a histogram. 
It reads words from a file, counts their occurrences, and displays them vertically with bars representing each occurrence 
using 'x'. The program aims to provide insights into a baby's early language development.
"""

def main():
    words = load_words_from_file("words.txt")
   # Counts the appearance of each word
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    # Print the histogram
    for word, count in word_counts.items():
        print_histogram_bar(word, count)

def print_histogram_bar(word, count):
    """
    Prints one bar in the histogram.
    
    Uses formatted strings to do so. The 
        {word : <8}
    adds white space after a string to make
    the string take up 8 total characters of space.
    This makes all of our words on the left of the 
    histogram line up nicely. On the other end,
        {'x' * count}
    takes the 'x' string and duplicates it by 'count'
    number of times. So 'x' * 5 would be 'xxxxx'.
    
    Calling print_histogram_bar("mom", 7) would print:
        mom     : xxxxxxx
    """
    print(f"{word : <8}: {'x' * count}")

def load_words_from_file(filepath):
    """
    Loads words from a file into a list and returns it.
    We assume the file to have one word per line.
    Returns a list of strings. You should not modify this
    function.
    """
    words = []
    with open(filepath, 'r') as file_reader:
        for line in file_reader.readlines():
            cleaned_line = line.strip()
            if cleaned_line != '':
                words.append(cleaned_line)
    
    return words


if __name__ == '__main__':
    main()
