# question 1 task 1

import mood_responses

def main():
    mood = input("How are you feeling today?")
    print(mood_responses.mood_response(mood))

if __name__ == "__main__":
    main()