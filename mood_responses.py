# question 1 task 1 (pt 2)

def mood_response(mood):

    responses = {
        'happy' : "Awesome! Keep on smiling",
        'sad' : "Oh no! Turn that frown upside down",
        'anxious' : "Deep breaths! It's all going to be okay",
        'bored' : "I suggest looking into new hobbies to occupy your time",
        'excited' : "Fantastic! I hope whatever you are looking forward to is as great as you are hoping it will be.",
    }

    return responses.get(mood, "I hope the rest of your day is fantastic")