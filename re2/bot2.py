from random import randint


class Bot:
    def __init__(self, position: list, pole):
        self.pos_x, self.pos_y = position
        self.pole = pole
        self.pole[self.pos_x][self.pos_y] = 1
        self.max_x = len(pole) - 1
        self.max_y = len(pole[0]) - 1

        self.left_bool = 0
        self.right_bool = 0
        self.up_bool = 0
        self.down_bool = 0

        self.revers1 = True
        self.revers2 = True

    def default_method(self):
        pass

    def run_motion(self, x, y):
        if not(self.pos_x == x and self.pos_y == y):
            x, y = self.pos_x, self.pos_y
            self.pole[self.pos_x][self.pos_y] -= 1

            self.default_method()

            self.pole[self.pos_x][self.pos_y] += 1

            return x, y

    def right_or_down_or_left_or_up(self):
        if self.revers1:
            self.check_right()
            self.simple_right_motion()
            if not self.right_bool:
                self.revers1 = False
        else:
            self.check_left()
            self.simple_left_motion()
            if not self.left_bool:
                self.revers1 = True

        if self.revers2:
            self.check_down()
            self.simple_down_motion()
            if not self.down_bool:
                self.revers2 = False
        else:
            self.check_up()
            self.simple_up_motion()
            if not self.up_bool:
                self.revers2 = True

    def interesting_right_or_down_or_left_or_up4(self):
        self.check_motion()

        if self.revers1:
            self.simple_right_motion()
            if self.right_bool:
                self.revers2 = False
        else:
            self.simple_left_motion()
            if self.left_bool:
                self.revers2 = True

        if self.revers2:
            self.simple_down_motion()
            if self.down_bool:
                self.revers1 = True
        else:
            self.simple_up_motion()
            if self.up_bool:
                self.revers1 = False

    def interesting_right_or_down_or_left_or_up3(self):
        self.check_motion()

        if self.revers1:
            self.simple_right_motion()
            if self.pos_x == self.max_x:
                self.revers2 = False
        else:
            self.simple_left_motion()
            if self.pos_x == 0:
                self.revers2 = True

        if self.revers2:
            self.simple_down_motion()
            if self.pos_y == self.max_y:
                self.revers1 = True
        else:
            self.simple_up_motion()
            if self.pos_y == 0:
                self.revers1 = False

    def interesting_right_or_down_or_left_or_up2(self):
        self.check_motion()

        if self.revers1:
            self.right_motion()
            if not self.right_bool:
                self.revers1 = False
        else:
            self.left_motion()
            if not self.left_bool:
                self.revers1 = True

        if self.revers2:
            self.down_motion()
            if not self.down_bool:
                self.revers2 = False
        else:
            self.up_motion()
            if not self.up_bool:
                self.revers2 = True

    def interesting_right_or_down_or_left_or_up(self):
        self.check_motion()

        if self.revers1:
            self.simple_right_motion()
            if self.pos_x == self.max_x:
                self.revers1 = False
        else:
            self.simple_left_motion()
            if self.pos_x == 0:
                self.revers1 = True

        if self.revers2:
            self.simple_down_motion()
            if self.pos_y == self.max_y:
                self.revers2 = False
        else:
            self.simple_up_motion()
            if self.pos_y == 0:
                self.revers2 = True

    def interesting_right_down_or_left_up(self):
        self.check_motion()
        if not self.revers1:
            self.simple_right_motion()
            self.simple_down_motion()
            if not(self.right_bool and self.down_bool):
                self.revers1 = True
        else:
            self.simple_left_motion()
            self.simple_up_motion()
            if not(self.left_bool and self.up_bool):
                self.revers1 = False

    def interesting_right_down_or_left_up2(self):
        self.check_motion()
        if not self.revers1:
            self.simple_right_motion()
            self.simple_down_motion()
            if self.pos_x == self.max_x:
                self.revers1 = True
        else:
            self.simple_left_motion()
            self.simple_up_motion()
            if self.pos_x == 0:
                self.revers1 = False

    def interesting_right_down(self):
        self.check_motion()
        self.right_motion()
        self.down_motion()

    def right_down(self):
        self.check_left_right()
        self.right_motion()
        self.check_up_down()
        self.down_motion()

    def interesting_right_down_left_up(self):
        self.check_motion()
        self.right_motion()
        self.down_motion()
        self.left_motion()
        self.up_motion()

    def right_down_left_up(self):
        self.check_left_right()
        self.right_motion()
        self.check_up_down()
        self.down_motion()
        self.check_left_right()
        self.left_motion()
        self.check_up_down()
        self.up_motion()

    def simple_right_down_left_up(self):
        self.check_right()
        self.simple_right_motion()
        self.check_down()
        self.simple_down_motion()
        self.check_left()
        self.simple_left_motion()
        self.check_up()
        self.simple_up_motion()

    def random(self):
        self.check_left_right()
        self.pos_x += randint(-self.left_bool, self.right_bool)
        self.check_up_down()
        self.pos_y += randint(-self.up_bool, self.down_bool)

    def right_motion(self):
        if self.right_bool:
            self.pos_x += 1
        elif self.left_bool:
            self.pos_x -= 1

    def left_motion(self):
        if self.left_bool:
            self.pos_x -= 1
        elif self.right_bool:
            self.pos_x += 1

    def down_motion(self):
        if self.down_bool:
            self.pos_y += 1
        elif self.up_bool:
            self.pos_y -= 1

    def up_motion(self):
        if self.up_bool:
            self.pos_y -= 1
        elif self.down_bool:
            self.pos_y += 1

    def simple_right_motion(self):
        if self.right_bool:
            self.pos_x += 1

    def simple_left_motion(self):
        if self.left_bool:
            self.pos_x -= 1

    def simple_down_motion(self):
        if self.down_bool:
            self.pos_y += 1

    def simple_up_motion(self):
        if self.up_bool:
            self.pos_y -= 1

    def check_motion(self):
        self.check_left_right()
        self.check_up_down()

    def check_left_right(self):
        self.check_left()
        self.check_right()

    def check_up_down(self):
        self.check_up()
        self.check_down()

    def check_right(self):
        if self.pos_x != self.max_x and self.pole[self.pos_x + 1][self.pos_y] != 1:
            self.right_bool = 1
        else:
            self.right_bool = 0

    def check_left(self):
        if self.pos_x != 0 and self.pole[self.pos_x - 1][self.pos_y] != 1:
            self.left_bool = 1
        else:
            self.left_bool = 0

    def check_up(self):
        if self.pos_y != 0 and self.pole[self.pos_x][self.pos_y - 1] != 1:
            self.up_bool = 1
        else:
            self.up_bool = 0

    def check_down(self):
        if self.pos_y != self.max_y and self.pole[self.pos_x][self.pos_y + 1] != 1:
            self.down_bool = 1
        else:
            self.down_bool = 0

    def del_bot(self):
        self.pole[self.pos_x][self.pos_y] = 0
        return self.pos_x, self.pos_y
