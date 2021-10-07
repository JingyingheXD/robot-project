from robot import Robot

TABLE_SIZE = 5


class Table:
    def __init__(self, size):
        self.table_size = (size, size)
        self.tb_min = 0
        self.tb_max_x = size - 1
        self.tb_max_y = size - 1
        self.robots = []

    def add_robot(self):
        pass

    def instruction(self):
        pass

    def check_boarder(self, position):
        x, y = position
        if x > self.tb_max_x or y > self.tb_max_y or x < self.tb_min or y < self.tb_min:
            # exceed border
            return False
        else:
            return True


if __name__ == "__main__":
    table = Table(TABLE_SIZE)
    robot = Robot(table)
    print('Please input instruction:')
    while True:
        instruction_str = input('')
        robot.get_instruction(instruction_str)
