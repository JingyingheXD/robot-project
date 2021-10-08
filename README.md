**Introduction**
This programming completes the basic requirements and extention requirements. Multiple robots can be added on the table and move based on input form keyborad.

### Commands

1. 'PLACE'
   e.g. 'PLACE 0,0,EAST'
   It adds a new robot on the table. However, the new robot cannot be placed in the same place with other robots. The first placed robot's named 'ROBOT 1'.
2. 'MOVE'
   It allows an activate robot to move one unit forward in the facing direction. It cannot move exceed the table border or move to other robots' positions.
3. 'LEFT', 'RIGHT'
   It rotates the robot 90 degrees in the specified direction without changing the position of the robot.
4. 'REPORT'
   It announces the positions and directions of all robots which are on the table.
5. 'ROBOT'
   e.g. 'ROBOT 2'
   It activates the specific robot, and the following commands/instructions affect this activate robot. By default the first robot placed will become the active robot.
