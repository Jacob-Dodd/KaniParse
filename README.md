
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/github_username/repo_name">
    <img src="images/crab.jpeg" alt="Logo" width="80" height="80">
  </a>

<h2 align="center">KaniParse</h2>

  <p align="center">
    A VERY basic terminal based NLP assisted Anki tool for language learners
    <br />
    <a href="https://github.com/github_username/repo_name"><strong>Explore the docs »</strong></a>
    <br />
    <br />
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

A simple command-line tool I developed to automate the creation of vocab cards for space-repetition learning. At this stage it's capable of scanning entire Japanese ebooks and using NLP, tokenizes every proper Japanese word, while also deinflecting all the verbs it finds. These tokens are then sorted into a list by frequency. This list is then fed into JMDict, a large machine-readable multilingual Japanese dictionary, to get English definitions and grammar notes for every word. Finally these words are then converted into cards in an Anki Deck using Genanki, so they can be utilised for space-repetition practice. This project is still in its VERY early stages and I'm learning as I go, but I have plans to add support for more languages down the line to facilitate other language learning ventures.


<br />


### Built With:


[![Python][Pythonimg]][Python-url]

<br />




<!-- GETTING STARTED -->
## Getting Started

Follow instructions below to get started

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

  ```sh
  pip install -r requirements.txt
  ```

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Jacob-Dodd/KaniParse.git
   ```
2. Install packages
   ```sh
   pip install -r requirements.txt
   ```
3. download and install the ja_core_news_md and jamdict datasets
   ```sh
   python -m spacy download ja_core_news_md

   pip install --upgrade jamdict jamdict-data
   ```

<br />



<!-- USAGE EXAMPLES -->
## Usage

Simply place the target ebooks(.epub files) in the projects root directory and run
```sh
python3 main.py
```
and follow  the menu prompts
<br />
<br />
Note Search Jamdict takes words.txt as input which is generated by Generate Wordlist or can be provided manually. Create Anki deck accepts the output of Search JAMdict which must follow an explicit format otherwise the regular expressions in Create Anki deck will fail


<br />



<!-- LICENSE -->
## License

Distributed under the MIT License.


<br />



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [spaCy](https://spacy.io/)
* [ebooklib](https://github.com/aerkalov/ebooklib)
* [Jamdict](https://github.com/neocl/jamdict)
* [Genanki](https://github.com/kerrickstaley/genanki)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: images/pic.png
[Pythonimg]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://python.org/

