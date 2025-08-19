'''can use better cleaning techniques which i will do in the upcoming versions'''


from cleantext import clean
import spacy

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

def clean_transcript(text):
    # Step 1: Basic cleaning using clean-text
    cleaned = clean(
        text,
        fix_unicode=True,
        to_ascii=True,
        lower=False,           # Keep original casing
        no_urls=True,
        no_emails=True,
        no_phone_numbers=True,
        no_numbers=False,      # Keep numbers if they’re important
        no_digits=False,
        no_currency_symbols=True,
        no_punct=False         # Keep punctuation for sentence detection
    )

    # Step 2: Remove filler words and repeated words using spaCy
    doc = nlp(cleaned)
    filtered_sentences = []
    filler_words = {"um", "uh", "like", "you know", "i mean", "sort of", "kind of"}

    for sent in doc.sents:
        tokens = [token.text for token in sent if token.text.lower() not in filler_words]
        filtered_sentences.append(" ".join(tokens))

    # Step 3: Remove extra whitespace
    final_cleaned = " ".join(filtered_sentences)
    return final_cleaned.strip()

if __name__ == "__main__":
    raw_transcript = """
    um so like today we’re here to discuss the Q3 marketing plan uh I mean we have uh some
    updates from the sales team you know they’ve been doing sort of really good with the
    outreach and like um our social media engagement is uh increasing I think...
    """
    cleaned_transcript = clean_transcript(raw_transcript)
    print("\n--- Cleaned Transcript ---\n")
    print(cleaned_transcript)

