"""A script to randomly generate a joke"""
import random


jokes = [
    {
        "joke": "Why don't scientists trust atoms?",
        "punchline": "Because they make up everything!"
    },
    {
        "joke": "What do you call a fake noodle?",
        "punchline": "An impasta."
    },
    {
        "joke": "Why did the scarecrow win an award?",
        "punchline": "Because he was outstanding in his field!"
    },
    {
        "joke": "I'm reading a book on anti-gravity.",
        "punchline": "It's impossible to put down!"
    },
    {
        "joke": "What do you get when you cross a snowman and a vampire?",
        "punchline": "Frostbite."
    }
]

jokes_length = len(jokes)
# Obtain a random integer to be used as an index
random_index = random.randint(0, jokes_length-1)
# Save a random joke to a variable
random_joke = jokes[random_index]
# Display jokes until user stops program
while True:
    print(f"Joke: {random_joke["joke"]}\n\
Punchline: {random_joke["punchline"]}\n")
    another_joke = input("Type 'yes' for another joke: ").lower()
    if another_joke != "yes":
        break
    
print("Restart the program for more random jokes")
