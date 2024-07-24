def count_words(text):
    text = text.strip()
    
    if not text:
        return 0
    
    words = text.split()
    
    
    return len(words)

def main():
   
    
    while True:
        text = input("\nEnter a sentence or paragraph (or 'exit' to quit): ")
        
        if text.lower() == 'exit':
            print("Exiting the program. Goodbye!")
            break
        
        num_words = count_words(text)
        
        # Display the result
        if num_words == 0:
            print("Error: Empty input. Please enter some text.")
        else:
            print(f"Number of words: {num_words}")

if __name__ == "__main__":
    main()
