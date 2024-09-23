# question 2 task 1

import text_utils as tu

def main():
    string_to_manipulate = input("Enter the string you would like to manipulate: ")

    reversed_input = tu.reverse_string(string_to_manipulate)
    print(f"Your reversed string: {reversed_input}")

    capiatlized_input = tu.capitalize_string(string_to_manipulate)
    print(f"Your string capitalized: {capiatlized_input}")


if __name__ == "__main__":
    main()