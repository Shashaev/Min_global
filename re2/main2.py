from tkinter import Tk, Label
from bot2 import Bot
from random import shuffle, randint, choice
from PIL import ImageTk, Image, ImageDraw
from dataclasses import dataclass
from time import time


def random_create_bots(dat):
    ch = 0
    n = [[x, y] for x in range(len(dat.pole)) for y in range(len(dat.pole[0]))]
    shuffle(n)
    len_n = len(n)
    while ch < len_n and ch != dat.count_bots:
        bot = Bot(n[ch], dat.pole)
        dat.list_bots.append(bot)
        ch += 1

    return ch


def create_bots(dat):
    ch = 0
    for x in range(0, len(dat.pole), dat.MOVE_SIZE_X):
        for y in range(0, len(dat.pole[x]), dat.MOVE_SIZE_Y):
            bot = Bot([x, y], dat.pole)
            dat.list_bots.append(bot)
            ch += 1
            if dat.count_bots == ch:
                break

        if dat.count_bots == ch:
            break

    return ch


def painting(pole):
    len_y = len(pole[0])
    for x in range(len(pole)):
        for y in range(len_y):
            z = pole[x][y]
            if z:
                # fill = (z, z // 10, z // 100)
                # fill = (z * 10, z, z // 5)
                if z <= 503:
                    fill = colors[z]
                else:
                    fill = (z * 10, z * 10, z)
                draw_img.rectangle((x * SIZE_PIXELS, y * SIZE_PIXELS, (x+1) * SIZE_PIXELS, (y+1) * SIZE_PIXELS), fill)


def motion(list_bots):
    x = -1
    y = -1
    for bot in list_bots:
        z = bot.run_motion(x, y)
        if z:
            x, y = z


def start_loop(dat, count_motions=1):
    # print('Motions: ', count_motions)

    start_time = round(time() * 1000)
    draw_img.rectangle((0, 0, WIDTH, HEIGHT), fill='black', outline='black')

    if dat.end_motions or count_motions == dat.end_motions:
        return

    motion(dat.list_bots)
    painting(dat.pole)
    img_to_label.paste(img)

    delay = max(1, 100 - (round(time() * 1000) - start_time) - dat.count_bots // 150)
    tk.after(delay, lambda: start_loop(dat, count_motions + 1))


@dataclass()
class Data:
    count_bots = 150000
    MOVE_SIZE_X = 1
    MOVE_SIZE_Y = 1
    size = 1
    Bot.default_method = Bot.interesting_right_down_or_left_up
    RANDOM_GENERATION = 0
    RANDOM_COUNT_BOTS = 0
    RANDOM_MOVE_SIZE = 0
    RANDOM_SIZE = 0
    RANDOM_FUNCTION = 0
    end_motions = False

    list_bots = []
    pole = []
    list_function = (Bot.right_down, Bot.simple_right_down_left_up, Bot.right_down_left_up,
                     Bot.interesting_right_down_left_up, Bot.interesting_right_down,
                     Bot.interesting_right_down_or_left_up, Bot.right_or_down_or_left_or_up,
                     Bot.interesting_right_or_down_or_left_or_up, Bot.interesting_right_or_down_or_left_or_up2,
                     Bot.interesting_right_or_down_or_left_or_up4,
                     )


def main(dat):
    # shuffle(colors)

    dat.end_motions = not dat.end_motions

    dat.list_bots = []
    dat.pole = [[0 for _ in range(0, HEIGHT, SIZE_PIXELS)] for _ in range(0, WIDTH, SIZE_PIXELS)]

    if dat.RANDOM_FUNCTION:
        Bot.default_method = choice(dat.list_function)

    if dat.RANDOM_MOVE_SIZE:
        dat.MOVE_SIZE_X = randint(1, 5)
        dat.MOVE_SIZE_Y = randint(1, 5)

    if dat.RANDOM_COUNT_BOTS:
        dat.count_bots = randint(1, len(dat.pole) * len(dat.pole[0]) // dat.MOVE_SIZE_X // dat.MOVE_SIZE_Y)

    if dat.RANDOM_GENERATION:
        count = random_create_bots(dat)
    else:
        count = create_bots(dat)

    if not dat.end_motions:
        print('count_bots = ', count)
        print('MOVE_SIZE_X = ', dat.MOVE_SIZE_X)
        print('MOVE_SIZE_Y = ', dat.MOVE_SIZE_Y)
        print('size = ', SIZE_PIXELS)
        print('Bot.default_method = ', f'Bot.{Bot.default_method.__name__}')
        tk.after(250, lambda: start_loop(dat))
    else:
        tk.after(250, lambda: main(dat))


if __name__ == '__main__':
    SIZE_PIXELS = Data.size

    if Data.RANDOM_SIZE:
        SIZE_PIXELS = randint(1, 11)

    WIDTH = 750
    WIDTH += SIZE_PIXELS - WIDTH % SIZE_PIXELS
    HEIGHT = 450
    HEIGHT += SIZE_PIXELS - HEIGHT % SIZE_PIXELS

    tk = Tk()
    img = Image.new('RGB', (WIDTH, HEIGHT), 'green')
    draw_img = ImageDraw.ImageDraw(img)
    img_to_label = ImageTk.PhotoImage(img)

    label = Label(tk, image=img_to_label)
    label.bind('<1>', lambda event: main(Data))
    label.grid()

    with open('colors') as f:
        colors = [tuple(int(j) for j in i.split()) for i in f.readlines()]

    main(Data)

    tk.mainloop()
