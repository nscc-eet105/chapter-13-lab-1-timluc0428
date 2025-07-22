# Tim Lucas
# Lab 13-1
# # 2025-07-21

def repeat(char, times):
    if times <= 0:
        return ""
    else:
        return char + repeat(char, times -1)

def main():
    char = input("What character would you like to repeat? ")
    times = int(input(f"How many {char}\'s would you like to print? "))

    print(repeat(char, times))

if __name__ == "__main__":
    main()