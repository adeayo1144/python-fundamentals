#/usr/bin/python3
"""a module that checks grammer in a sentence"""
from textblob import TextBlob

def check_grammer(sentence):
    blob = TextBlob(sentence)
    corrected = blob.correct()
    return str(corrected)


if __name__ == "__main__":
    """main function to test the grammer checker"""
    sentence = "This is a smpke sentence with a few erors."
    corrected_sentence = check_grammer(sentence)
    print(f"Original: {sentence}")
    print(f"Corrected: {corrected_sentence}")