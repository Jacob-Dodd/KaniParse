from jamdict import Jamdict
from tqdm import tqdm
jam = Jamdict()


def searchDict():
    # Read the input file
    with open('words.txt', 'r') as input_file:
        words = input_file.readlines()

    # Create an empty list for the output
    output = []

    # Use tqdm to create a progress bar
    for word in tqdm(words, desc='😩'):
        # Strip the newline character at the end of the word
        word = word.strip()

        result = jam.lookup(word)
        for entry in result.entries:
            output.append(str(entry))
        ##output.append('\n')

    with open('vocabulary.txt', 'w') as output_file:
        output_file.write('\n'.join(output))