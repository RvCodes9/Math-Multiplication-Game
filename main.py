from colorama import Fore, Style
import random

score = 0
healt = 3

# Random numbers
num1 = random.randint(1,9)
num2 = random.randint(1,9)

print(f'\n{Fore.YELLOW}:: Math - Multiplication - Game :: {Style.RESET_ALL}')

while True:

    print(f'\n{Fore.CYAN}{num1} X {num2}{Style.RESET_ALL}')

    input_number = int(input(f'\n{Fore.MAGENTA}--> {Style.RESET_ALL}'))

    if input_number == (num1 * num2):
        score += 1
        print(f'\n{Fore.GREEN}< True >{Style.RESET_ALL}{Fore.BLACK} | {Style.RESET_ALL}{Fore.YELLOW}Score : {score}{Style.RESET_ALL}{Fore.BLACK} | {Style.RESET_ALL}Healt : {healt}')
        
        # New Random numbers
        num1 = random.randint(1,9)
        num2 = random.randint(1,9)

    else:

        if healt > 0:
            healt -= 1

        elif healt == 0:
            print(f'\n{Fore.RED}Game Over{Style.RESET_ALL}')
            break

        print(f'\n{Fore.RED}< False >{Style.RESET_ALL}{Fore.BLACK} | {Style.RESET_ALL}{Fore.YELLOW}Score : {score}{Style.RESET_ALL}{Fore.BLACK} | {Style.RESET_ALL}Healt : {healt}')