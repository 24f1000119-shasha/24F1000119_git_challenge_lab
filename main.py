from sum import add

def welcome():
    print("Welcome to the Command-Line Calculator!")

if __name__ == "__main__":
    welcome()
    sum_result = add(20, 10)
    print(f"20 + 10 = {sum_result}")