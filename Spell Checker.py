from textblob import TextBlob

def highlight_corrected(original, corrected):
    """
    Highlights corrected words in green if they differ from the original.
    """
    original_words = original.split()
    corrected_words = corrected.split()

    highlighted = []
    for orig, corr in zip(original_words, corrected_words):
        if orig != corr:
            # Highlight corrected word in green
            highlighted.append(f"\033[92m{corr}\033[0m")
        else:
            highlighted.append(corr)
    
    # Join the words back into a sentence
    return " ".join(highlighted)

print("Welcome to the Multi-Sentence Spell Checker!")
print("Enter a paragraph or multiple sentences to be corrected.")
print("Type 'exit' to quit the program.")
print("-" * 50)

while True:
    # Get user input
    user_input = input("Enter your text: ").strip()
    
    if user_input.lower() == "exit":
        print("Thank you for using the Spell Checker! Goodbye!")
        break

    if not user_input:
        print("You entered nothing. Please try again!")
        continue

    # Use TextBlob to correct the text
    blob = TextBlob(user_input)
    corrected_text = str(blob.correct())

    # Highlight corrected words
    highlighted_text = highlight_corrected(user_input, corrected_text)

    # Display the results
    print("\nOriginal Text:")
    print(user_input)
    print("\nCorrected Text:")
    print(corrected_text)
    print("\nHighlighted Corrections:")
    print(highlighted_text)
    print("-" * 50)
