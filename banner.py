import pyfiglet
from termcolor import colored
import random
import sys
import os

# Available fonts (limited subset for better Termux compatibility)
FONTS = [
    'standard'
]

COLORS = ['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_error(message):
    """Display error message in red"""
    print(colored(f"\nError: {message}", 'red'))

def generate_banner(text, font='standard', color='cyan'):
    """Generate colored banner with error handling"""
    try:
        if font not in FONTS:
            font = 'standard'
        return pyfiglet.figlet_format(text, font=font)
    except Exception as e:
        show_error(f"Font '{font}' not available. Using standard font.")
        return pyfiglet.figlet_format(text, font='standard')

def display_banner(banner, color):
    """Display banner with colored output"""
    try:
        print(colored(banner, color)) if color in COLORS else print(banner)
    except:
        print(banner)  # Fallback if coloring fails

def main():
    clear_screen()
    print(colored("\n✨ Termux Banner Tool ✨ Insta ID: official_aman07__ ✨\n✨ Created by Aman-mk ✨ version 1.0  ✨", 'yellow'))
    
    while True:
        try:
            text = input("\n Enter your text ->>>: ")
            if text.lower() == 'exit':
                break

            print("\n Available fonts:", ", ".join(FONTS))
            font = input(" Type standard -->>: ") or 'standard'
            
            print("\n Available colors:", ", ".join(COLORS))
            color = input(" Choose color -->>: ") or 'cyan'

            clear_screen()
            print(colored("\n Your Awesome Banner:\n", 'yellow'))
            
            banner = generate_banner(text, font)
            display_banner(banner, color)
            
            print("\nexit: CTRL + z \n"+ ">"*70)
            
        except KeyboardInterrupt:
            print(colored("\nOperation cancelled by user.", 'red'))
            break
        except Exception as e:
            show_error(str(e))

if __name__ == "__main__":
    # Check if pyfiglet is installed
    try:
        import pyfiglet
        import termcolor
        main()
    except ImportError:
        print(colored("\nRequired packages not found. Installing...", 'yellow'))
        os.system('pip install pyfiglet termcolor')
        print(colored("\nPlease run the script again.", 'green'))
        sys.exit()
