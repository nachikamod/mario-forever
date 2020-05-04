class SubRoutine():
    def routine_pipe(self, num, map_init, screen, pg, im):
        for x in range(0, len(num.obstacle_position_map)):
            map_init.place_obstacles(screen, pg, im, num.obstacle_position_map[x])
            #num.obstacle_position = num.obstacle_position_map[x]