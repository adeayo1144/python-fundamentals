def word_frequency(text):
    
    # Split the text into words
    words = text.split()
    
    # Create a dictionary to store word frequencies
    frequency = {}
    
    # Count the frequency of each word
    for word in words:
        frequency[word] = frequency.get(word, 0) + 1
    
    return frequency
text = "hello world hello"
result = word_frequency(text)
print(result)
