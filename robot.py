class Robot:
    def __init__(self, table):
        self.position = None
        self.direction = None
        self.table = table
        self.id = None

    # parse instruction from input
    def get_instruction(self, instr_str):
        try:
            instruction = instr_str.split(' ')[0]
            if instruction == 'PLACE':
                position_direction = instr_str.split(' ')[1]
                self.place(position_direction)
            elif instr_str == 'MOVE':
                self.move()
            elif instr_str == 'LEFT' or instr_str == 'RIGHT':
                self.rotate(instruction)
            elif instr_str == 'REPORT':
                self.report()
            # 'ROBOT xx'
            elif instruction == 'ROBOT':
                activate_rbt_id = instr_str.split(' ')[1]
                self.activate_robot(activate_rbt_id)
        except:
            print("Wrong input. Please input valid instruction again.\n")

    # place and add a robot
    def place(self, pos_dirc):
        x, y, dirc = tuple(map(str, pos_dirc.split(',')))
        result_robot = self.table.check_robots((int(x), int(y)))
        if result_robot == True:
            new_robot = Robot(self.table)
            new_robot.position = (int(x), int(y))
            new_robot.direction = dirc
            new_robot.id = len(self.table.robots) + 1
            self.table.robots.append(new_robot)
            if new_robot.id == 1:
                self.table.active_robot = new_robot
        else:
            print('There is a robot in this position. Please choose another positon.')

    def check_border_result(self, rbt_asmpt_position):
        result_border = self.table.check_boarder(rbt_asmpt_position)
        result_robot = self.table.check_robots(rbt_asmpt_position)
        if result_border == True and result_robot == True:
            self.position = rbt_asmpt_position
        else:
            print('Invalid position. Please input antoher instruction.')

    def move(self):
        if self.position != None and self.direction != None:
            x, y = self.position
            if self.direction == 'EAST':
                rbt_assumption_position = (x + 1, y)
                self.check_border_result(rbt_assumption_position)
            elif self.direction == 'SOUTH':
                rbt_assumption_position = (x, y - 1)
                self.check_border_result(rbt_assumption_position)
            elif self.direction == 'WEST':
                rbt_assumption_position = (x - 1, y)
                self.check_border_result(rbt_assumption_position)
            elif self.direction == 'NORTH':
                rbt_assumption_position = (x, y + 1)
                self.check_border_result(rbt_assumption_position)
        else:
            print("Robot has not been placed on the table.")

    def rotate(self, rot_direction):
        # turn_left_dict = {original_direction: new_direction}
        turn_left_dict = {'EAST': 'NORTH',
                          'NORTH': 'WEST',
                          'WEST': 'SOUTH',
                          'SOUTH': 'EAST'}

        # turn_right_dict = {original_direction: new_direction}
        turn_right_dict = {'NORTH': 'EAST',
                           'EAST': 'SOUTH',
                           'SOUTH': 'WEST',
                           'WEST': 'NORTH'}
        if rot_direction == 'LEFT':
            if self.position != None and self.direction != None:
                new_direction = turn_left_dict[self.direction]
                self.direction = new_direction
            else:
                print("Robot has not been placed on the table.")
        else:
            if self.position != None and self.direction != None:
                new_direction = turn_right_dict[self.direction]
                self.direction = new_direction
            else:
                print("Robot has not been placed on the table.")

    def report(self):
        if self.table.robots == []:
            print("Robot has not been placed on the table.")
        else:
            for robot in self.table.robots:
                x, y = robot.position
                print('Robot <', robot.id, '>: ', x,
                      ',', y, ',', robot.direction)

    def activate_robot(self, activate_rbt_id):
        self.table.active_robot = self.table.robots[int(activate_rbt_id) - 1]
