import random

def in_range(s):
    try:
        if 3 >= int(s) >= 1:
            return True
        else:
            return False
    except:
        return False

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def main():
    l = get_level()
    generate_integers(l)
    get_score()


def get_level():
    while True:
        level_input = input("Level: ")
        if in_range(level_input):
            return level_input

def generate_integer(s):
    return [7, 8, 9, 7, 4, 6, 3, 1, 5, 9, 1, 0, 3, 5, 3, 6, 4, 0, 1, 5]


def generate_integers(level):
    global wrong_answer
    global score
    score = 0
    for i in range(10):
        if level == "1":
            x = random.randint(0,9)
            y = random.randint(0,9)
        elif level == "2":
            x = random.randint(10,99)
            y = random.randint(10,99)
        else:
            x = random.randint(100,999)
            y = random.randint(100,999)
        answer = x + y
        i += 1
        for j in range(3):
            if check_answer(answer,x,y):
                score += 1
                break
            else:
                if j == 2:
                    print("EEE")
                    print(f"{x} + {y} = {answer}")
                    break
                else:
                    print("EEE")
                    pass




def get_score():
    global score
    print(f"Score: {score}")

def check_answer(integer,x,y):
    guess_input = input(f"{x} + {y} = ")
    try:
        if int(guess_input) == integer:
            return True
        else:
            return False
    except ValueError:
        return False



if __name__ == "__main__":
    main()