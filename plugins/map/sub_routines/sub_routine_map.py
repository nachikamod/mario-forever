class SubRoutine():
    #Pipe creation - input (x and y position of pipes)
    def routine_pipe(self, num, map_init, screen, pg, im):
        for x in range(0, len(num.obstacle_position_map)):
            map_init.place_obstacles(screen, pg, im, num.obstacle_position_map[x])

    #Obstacle mechanics - Passing starting position of obstacle to mechanics method for further calculations    
    def routine_game_mech(self, bools, num, mechanics_init):
        for x in range(0, len(num.mech_pipe_map)):
            mechanics_init.obstacle_mechanics(bools, num, num.mech_pipe_map[x])