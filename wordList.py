import ebooklib
from ebooklib import epub
import spacy
import os
import re

def readEbook():

    # Load the Japanese spaCy model
    nlp = spacy.load('ja_core_news_md')

    # Get the path of the .epub file from the user
    file_path = input("Enter the path of the .epub file: ")

    # Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: file not found at path '{file_path}'")
        exit()

    # Use ebooklib to open the epub file
    book = epub.read_epub(file_path)

    # Initialize a list to store the tokenized words
    words = []

    # Iterate through all the items in the book (which should include the text from each chapter)
    for item in book.get_items():
        # If the item is a chapter (identified by the 'text/html' media type)
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            # Decode the bytes object to a string and use the spaCy model to tokenize and deinflect it
            text = item.get_content().decode()
            # Break up the text into smaller chunks (e.g. 100 characters each)
            chunk_size = 100
            chunks = [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]
            for chunk in chunks:
                # Use the spaCy model to tokenize and deinflect each chunk
                doc = nlp(chunk)
                # Add only the non-grammar tokens (i.e. vocabulary) to the list of words
                words.extend([token.lemma_ for token in doc if token.pos_ == 'NOUN' 
                or token.pos_ == 'VERB'
                or token.pos_ == 'ADJ'])

    # Check if the words list is empty
    if not words:
        print("The .epub file does not contain any Japanese nouns, verbs, or adjectives")
    else:
        # Use the Counter class from the collections module to count the frequency of each word
        from collections import Counter
        word_counts = Counter()

        # Check if each word contains Japanese characters and add it to the word_counts dictionary
        for word in words:
            if re.search(r'[\u3040-\u309F]|[\u30A0-\u30FF]|[\u4E00-\u9FFF]', word):
                word_counts[word] += 1

        # Write the list of most frequent words to a file
        with open('words.txt', 'w') as file:
            for word, count in word_counts.most_common():
                #file.write(f"{word}: {count}\n")
                file.write(f"{word}\n")
        print("The list of most frequent words has been saved to the file 'word.txt'")
