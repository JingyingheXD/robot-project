class Robot:
    def __init__(self, table):
        self.position = None
        self.direction = None
        self.table = table

    # parse instruction from input
    def get_instruction(self, instr_str):
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
        else:
            print("Wrong input. Please input valid instruction again.\n")

    def place(self, pos_dirc):
        x, y, dirc = tuple(map(str, pos_dirc.split(',')))
        self.position = (int(x), int(y))
        self.direction = dirc

    def check_border_result(self, rbt_asmpt_position):
        result = self.table.check_boarder(rbt_asmpt_position)
        if result == True:
            self.position = rbt_asmpt_position
        else:
            print('Exceed the border. Please input valid instruction again.')

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
        if self.position == None and self.position == None:
            print("Robot has not been placed on the table.")
        else:
            x, y = self.position
            print(x, ',', y, ',', self.direction)
