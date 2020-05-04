class GenerateMap():
    def place_ground(self, screen, pg, im, num):

        #Place ground across screen width
        for x in range(0, num.width, 40):

            #Sett according to block size
            screen.blit(im.parse_ground, (x, 620))
            screen.blit(im.parse_ground, (x, 660))

    def place_obstacles(self, screen, pg, im, obs_pos):

        screen.blit(im.parse_small_pipe, obs_pos)