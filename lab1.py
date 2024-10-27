import time

SET_COLOR = "\x1b[48;5;"
END = "\x1b[0m"
CLEAR = "\033[H"
MOVING = "\x1b"
RED = 1
YELLOW = 221
GREEN = 35
WHITE = 231
BLACK = 0

def draw_line(offset=0, length=1, color=YELLOW):
    line = "  " * length
    print(f"{'  ' * offset}{SET_COLOR}{color}m{line}{END}")

def draw_flag():
    height = 8

    for i in range(height):
        if i < height//2:
            draw_line(length=10, offset=6)
        else:
            draw_line(length=10, offset=6, color=RED)

    print(f"{MOVING}[{height+1}A")

    for i in range(height):
        draw_line(length=6, color=GREEN)

def draw_pattern():
    size = 8
    color = 91
    
    step = 1
    length = 1
    center = size // 2
    offset = size // 2

    for i in range(3):
        for j in range(2, -1, -1):
            if j != 2:
                print(f"{MOVING}[{size + 2}A")

            for line in range(size+1):
                draw_line(offset + (j * size), length, color)

                if line < center:
                    offset -= step
                    length += step * 2

                else:
                    offset += step
                    length -= step * 2

            step = 1
            length = 1
            center = size // 2
            offset = size // 2

        print(f"{MOVING}[{2}A")
    print("\n")

def draw_graph():
    print("y = x + 1")

    for i in range(9, 0, -1):
        print(f"{i}{SET_COLOR}{WHITE}m{(i-1) * '  '}{SET_COLOR}{BLACK}m{'  '}{SET_COLOR}{WHITE}m{(9-i) * '  '}{END}")
    
    print(f"0{SET_COLOR}{WHITE}m{9 * '  '}{END}")
    print("  0 1 2 3 4 5 6 7 8")
            
def draw_diogram():
    with open('sequence.txt') as file:
        numbers = [float(x) for x in file]
    positive_num = 0
    negative_num = 0

    for i in numbers:
        if 0 <= i <= 5:
            positive_num += 1
        if -5 <= i <= 0:
            negative_num += 1
    
    if (positive_num - (positive_num // 10)) < 0.5:
        len_pos = int(positive_num // 10) 
    else:
        len_pos = int(positive_num // 10) + 1

    if (negative_num - (negative_num // 10)) < 0.5: 
        len_neg = int(negative_num // 10)
    else:
        len_neg = int(negative_num // 10) + 1

    print(f"{SET_COLOR}{GREEN}m{len_pos * '  '}{END} - числа от 0 до 5") 
    print(f"{SET_COLOR}{RED}m{len_neg * '  '}{END} - числа от -5 до 0") 

def animation():
    size = 15
    center = size // 2
    offset = size // 2

    step = 1
    length = 1

    colors = [89, 91]

    while True:
        for i in range(7):
            for color in colors:
                for line in range(size):
                    draw_line(offset, length, color)

                    if line < center:
                        offset -= step
                        length += step*2

                    else:
                        offset += step
                        length -= step*2

                print(f"{MOVING}[{size+2}A")
                print(f"{MOVING}[{offset}D")

                time.sleep(1.5)

        length = 1
        offset = size // 2

                
if __name__ == "__main__":
    print("Кормушкина Ксения, 8 вариант\n")
    
    draw_flag()  
    print("\n")

    draw_pattern()
    print("\n")

    draw_graph()
    print("\n")
    
    draw_diogram()
    print("\n")
    
    animation()
