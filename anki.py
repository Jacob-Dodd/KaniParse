import genanki
import re

# Define a model for the Anki cards
model = genanki.Model(
  1607392319,
  'Japanese Vocabulary',
  fields=[
    {'name': 'Japanese'},
    {'name': 'English'},
    {'name': 'Notes'},
  ],
  templates=[
    {
      'name': 'Card 1',
      'qfmt': '{{Japanese}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{English}}<br>{{Notes}}',
    },
  ],
  css='''
    .card {
      font-family: arial;
      font-size: 20px;
      text-align: center;
      color: black;
      background-color: white;
    }
  '''
)

# Define a deck for the Anki cards
deck = genanki.Deck(
  2059400310,
  'Japanese Vocabulary'
)

def createCards():
    
    # Read the txt file line by line
    with open('vocabulary.txt', 'r') as f:
        for line in f:
            # Parse the fields from each line using a regular expression
            japanese, english, notes = re.findall(r'\[id#\d+\]\s+(.+?)\s+:\s+(.+?)\s+\((.+?)\)', line.strip())[0]

            # Split the English meanings by the number at the start of each line
            english_meanings = re.split(r'^\d+\.', english)

            # Create a card for each English meaning
            for meaning in english_meanings:
                card = genanki.Note(
                    model=model,
                    fields=[japanese, meaning, notes]
                )
                # Add the card to the deck
                deck.add_note(card)

    # Generate the Anki package
    genanki.Package(deck).write_to_file('japanese_vocabulary.apkg')
