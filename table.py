from robot import Robot

TABLE_SIZE = 5


class Table:
    def __init__(self, size):
        self.table_size = (size, size)
        self.tb_min = 0
        self.tb_max_x = size - 1
        self.tb_max_y = size - 1
        # when placd a robot, this robot is added to robots[]
        self.robots = []
        self.active_robot = None

    def check_boarder(self, asmpt_position):
        x, y = asmpt_position
        if x > self.tb_max_x or y > self.tb_max_y or x < self.tb_min or y < self.tb_min:
            # exceed border
            return False
        else:
            return True

    # not allowed more than one robots in the same position
    def check_robots(self, asmpt_position):
        x, y = asmpt_position
        if len(self.robots) > 0:
            for tb_robot in self.robots:
                tb_rbt_x, tb_rbt_y = tb_robot.position
                if tb_rbt_x == x and tb_rbt_y == y:
                    return False
            return True
        else:
            return True


if __name__ == "__main__":
    table = Table(TABLE_SIZE)
    init_active_robot = Robot(table)
    table.active_robot = init_active_robot
    print('Please input instruction:')
    while True:
        instruction_str = input('')
        table.active_robot.get_instruction(instruction_str)
