import tkinter
from bot import Bot
from random import shuffle


def random_create_bots(count=2):
    ch = 0
    n = [[x, y, x + SIZE_PIXELS, y + SIZE_PIXELS] for x in range(0, WIDTH, SIZE_PIXELS) for y in range(0, HEIGHT, SIZE_PIXELS)]
    shuffle(n)
    len_n = len(n)
    while ch < len_n and ch != count:
        position = n[ch]
        bot = Bot(c, position, len(list_bots))
        list_bots.append(bot)
        ch += 1

    return ch


def create_bots(count=2):
    ch = 0
    for x in range(0, WIDTH, SIZE_PIXELS * 2):
        for y in range(0, HEIGHT, SIZE_PIXELS * 2):
            bot = Bot(c, [x, y, x + SIZE_PIXELS, y + SIZE_PIXELS], len(list_bots))
            list_bots.append(bot)
            ch += 1
            if count == ch:
                break

        if count == ch:
            break

    return ch


def motion(els):
    for el in els:
        el.run_motion()


def main(count_motions=0, end_motion=10):
    print('Motions: ', count_motions)

    motion(list_bots)

    if end_motion and count_motions == end_motion:
        return

    tk.after(300, lambda: main(count_motions + 1, end_motion))


if __name__ == '__main__':
    SIZE_PIXELS = 10
    WIDTH = 500
    WIDTH += SIZE_PIXELS - WIDTH % SIZE_PIXELS
    HEIGHT = 300
    HEIGHT += SIZE_PIXELS - HEIGHT % SIZE_PIXELS

    count_bots = 100
    count_motions = False

    list_bots = []

    tk = tkinter.Tk('Min_global')
    c = tkinter.Canvas(tk, background='green', width=WIDTH, height=HEIGHT)
    print(create_bots(count_bots))
    c.grid()

    main(end_motion=count_motions)

    tk.mainloop()
