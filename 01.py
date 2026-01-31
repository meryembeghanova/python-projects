import time
import random
import sys
import os

# ANSI color list for rainbow effect
colors = [
    "\033[91m", "\033[93m", "\033[92m",
    "\033[96m", "\033[94m", "\033[95m"
]
reset = "\033[0m"

def rainbow_text(text, delay=0.03):
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(color + char + reset)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def loading_bar():
    rainbow_text("\n[ Starting Magic Engine... ]")
    for i in range(1, 31):
        bar = "#" * i + "-" * (30 - i)
        sys.stdout.write(f"\r\033[96mLoading: [{bar}] {i*3}%\033[0m")
        sys.stdout.flush()
        time.sleep(0.05)
    print("\n")

ASCII_ARTS = [
r"""
   /\_/\  
  ( o.o ) 
   > ^ < 
""",
r"""
  |\_/|
  | @ @   Woof!
  |   <>  
  |  _/  
""",
r"""
  _____
 /     \
| () () |
 \  ^  /
  |||||
  |||||
""",
r"""
     .-.
   .'   `.
   :g g   :
   : o    `.
  :         ``.
 :             `.
 :  :         .   `.
  `..`.__.-'`.____.'
"""
]

QUOTES = [
    "The best way to predict the future is to create it.",
    "Stay focused and never stop learning.",
    "Every great idea starts with a single line of code.",
    "Believe you can, and you’re halfway there.",
    "Magic happens when creativity meets logic."
]

def generate_ascii_art():
    art = random.choice(ASCII_ARTS)
    rainbow_text(art, delay=0.001)

def show_quote():
    quote = random.choice(QUOTES)
    rainbow_text(f"✨ Quote of the Moment ✨\n{quote}\n", delay=0.04)

def main_menu():
    os.system("cls" if os.name == "nt" else "clear")
    rainbow_text("WELCOME TO THE MAGIC PYTHON ART MACHINE\n", delay=0.02)

    while True:
        rainbow_text("Choose an option:\n1. Generate ASCII Art\n2. Show Inspirational Quote\n3. Surprise Me\n4. Exit\n")
        choice = input("-> ")

        if choice == "1":
            generate_ascii_art()

        elif choice == "2":
            show_quote()

        elif choice == "3":
            loading_bar()
            generate_ascii_art()
            show_quote()

        elif choice == "4":
            rainbow_text("\nGoodbye, creator! ✨")
            break

        else:
            print("Invalid choice. Try again!\n")

if __name__ == "__main__":
    loading_bar()
    main_menu() 




