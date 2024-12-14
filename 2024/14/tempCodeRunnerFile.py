
        position_x, position_y, velocity_x, velocity_y = map(int, re.findall('-?\d+', robot))
        robot_location = move_robot(position_x, position_y, velocity_x, velocity_y, width, height, 1)
        image[robot_location[0]][robot_location[1]] = '█'