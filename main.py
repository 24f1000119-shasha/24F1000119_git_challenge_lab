from sum import add
from difference import subtract
from product import multiply

def welcome():
    print("Welcome to the Simple Calculator!")

if __name__ == "__main__":
    welcome()
    sum_result = add(15, 5)
    print(f"15 + 5 = {sum_result}")

    diff_result = subtract(15, 5)
    print(f"15 - 5 = {diff_result}")

    prod_result = multiply(15, 5)
    print(f"15 * 5 = {prod_result}")