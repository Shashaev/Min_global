import tkinter
from random import randint


class Bot:
    def __init__(self, can: tkinter.Canvas, position: list, index_bot: int, fill='red'):
        self.fill = fill
        self.index_bot = index_bot
        self.can = can
        self.size_bot = position[2] - position[0]
        self.width = self.can.winfo_reqwidth() - self.size_bot - 4  # magic 4px
        self.height = self.can.winfo_reqheight() - self.size_bot - 4
        self.rectangle_id = self.can.create_rectangle(position, fill=self.fill)
        self.position = position[:2]

        self.left_bool = 0
        self.right_bool = 0
        self.up_bool = 0
        self.down_bool = 0

    def run_motion(self):
        left_el = self.can.find_closest(self.position[0] - self.size_bot // 3, self.position[1] + self.size_bot // 2)
        right_el = self.can.find_closest(self.position[0] + self.size_bot * 4 // 3, self.position[1] + self.size_bot // 2)
        up_el = self.can.find_closest(self.position[0] + self.size_bot // 2, self.position[1] - self.size_bot // 3)
        down_el = self.can.find_closest(self.position[0] + self.size_bot // 2, self.position[1] + self.size_bot * 4 // 3)

        self.left_bool = 0
        self.right_bool = 0
        self.up_bool = 0
        self.down_bool = 0

        if (left_el[0] == self.rectangle_id) and (self.position[0] != 0):
            self.left_bool = 1

        if (right_el[0] == self.rectangle_id) and (self.position[0] != self.width):
            self.right_bool = 1

        if up_el[0] == self.rectangle_id and self.position[1] != 0:
            self.up_bool = 1

        if down_el[0] == self.rectangle_id and self.position[1] != self.height:
            self.down_bool = 1

        if self.right_bool:
            self.position[0] += self.size_bot
        elif self.left_bool:
            self.position[0] -= self.size_bot

        if self.down_bool:
            self.position[1] += self.size_bot
        elif self.up_bool:
            self.position[1] -= self.size_bot

        # self.position[0] += self.size_bot * randint(-self.left_bool, self.right_bool) # random move
        # self.position[1] += self.size_bot * randint(-self.up_bool, self.down_bool)
        self.can.moveto(self.rectangle_id, *self.position)

    def get_id(self):
        return self.rectangle_id

    def del_bot(self):
        self.can.delete(self.rectangle_id)
        return self.index_bot
