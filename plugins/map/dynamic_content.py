#Dynamic object creation

class GenerateChars():

    #Animate mario
    def birth_mario(self, screen, pg, im, num, bools):
        if num.walk_count + 1 >= 15:
            num.walk_count = 0

        if bools.backward:
            screen.blit(im.mario_backward[num.walk_count//3], (num.x_move, num.y_move))
            num.walk_count += 1
    
        elif bools.forward:
            screen.blit(im.mario_forward[num.walk_count//3], (num.x_move, num.y_move))
            num.walk_count += 1
    
        else:
            screen.blit(im.mario_idle, (num.x_move, num.y_move))

        pg.display.update()