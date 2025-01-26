
# Multi-Sentence Spell Checker

A simple Python-based program that checks and corrects spelling errors in user-provided text. It highlights corrected words, making it easy to identify changes.

## Features
- Accepts paragraphs or multiple sentences as input.
- Uses the **TextBlob** library for spell checking and correction.
- Highlights corrected words in green for better visualization.
- Provides a user-friendly, interactive experience.

## Demo
### Input:
```text
I hav a dreem to becum a coder.
```

### Output:
```text
Original Text:
I hav a dreem to becum a coder.

Corrected Text:
I have a dream to become a coder.

Highlighted Corrections:
I have a dream to become a coder.
```

---

## How It Works
1. The user enters text into the program.
2. The program uses the **TextBlob** library to:
   - Detect spelling mistakes.
   - Correct them automatically.
3. Corrected words are highlighted in green to show changes.

## Requirements

- Python 3.6 or higher
- Libraries:
  - [TextBlob](https://textblob.readthedocs.io/en/dev/)

Install the library using:
```bash
pip install textblob
```
## Limitations
- The program highlights corrected words but may not work perfectly with:
  - Very complex or technical text.
  - Non-English sentences (depends on TextBlob's language support).

## Contributing

Contributions are welcome! Feel free to:
- Open an issue for bugs or feature requests.
- Fork the repository and submit a pull request.
  
