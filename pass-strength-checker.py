import string

def Pass_strength_checker(password):
    score = 0
    letters = string.ascii_letters
    digits = string.digits
    symbols = string.punctuation

    for item in password:
        if item in letters:
            score +=1
            if item.isupper():
                score +=1
        elif item in digits:
            score +=1
        elif item in symbols:
            score +=3
        else:
            score +=1
    strength = ""
    if score <=4:
        strength = "Very weak"
    elif score <=8:
        strength = "Weak"
    elif score <=12:
        strength = "Solid"
    elif score <= 16:
        strength = "Strong"
    elif score > 16:
        strength = "Very Strong"
    return print(f"This password is {strength}!")

Pass_strength_checker("sadsagf#dddA")
