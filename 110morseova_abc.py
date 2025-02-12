import os

class Morse_Code_Converter:
    # Dictionary for Morse code translation
    MORSE_CODE = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
        'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-',
        'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
        '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        ',': '--..--', '.': '.-.-.-', '?': '..--..', '!': '-.-.--',
        ';': '-.-.-', ' ': '/'}
    
    # Reverse dictionary for decoding Morse code back to text
    MORSE_TO_TEXT = {value: key for key, value in MORSE_CODE.items()}
    
    def __init__(self, input_file="input.txt", output_file="output.txt"):
    # Input and output file names.
        self.input_file = input_file
        self.output_file = output_file
    
    def text_to_morse(self, text):
    # Text to Morse Code
        return ' '.join(self.MORSE_CODE[char] for char in text if char in self.MORSE_CODE)
    
    def morse_to_text(self, morse):
     # Morse Code back to text
        return ''.join(self.MORSE_TO_TEXT[code] for code in morse.split() if code in self.MORSE_TO_TEXT)
    
    def process_files(self):
     # Checking if input file exists - if yes, load it
        if not os.path.exists(self.input_file):
            print(f"File {self.input_file} does not exist.")
            return
        
        with open(self.input_file, "r", encoding="utf-8") as file:
            text = file.read().upper()
        
        #Transcripts the text
        morse_text = self.text_to_morse(text)
        decoded_text = self.morse_to_text(morse_text)
        
        #Re-writes output file and saves it
        with open(self.output_file, "w", encoding="utf-8") as file:
            file.write("Original text: " + text + "\n")
            file.write("Morse code: " + morse_text + "\n")
            file.write("Decoded text: " + decoded_text + "\n")
        
        print("Completed!")

if __name__ == "__main__":
    converter = Morse_Code_Converter()
    converter.process_files()
