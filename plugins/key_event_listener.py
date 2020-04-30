#Mario movement
def key_press(pg, num, bools):
    keys = pg.key.get_pressed()
    
    #Forward movement pixels
    if (keys[pg.K_RIGHT] or keys[pg.K_d]) and num.x_move < num.move_max:
        num.x_move += num.step_size
        bools.backward = False
        bools.forward = True

    #Backward movement pixels
    elif (keys[pg.K_LEFT] or keys[pg.K_a]) and num.x_move > 0:
        num.x_move -= num.step_size
        bools.backward = True
        bools.forward = False

    #Idle
    else:
        bools.forward = False
        bools.backward = False
        num.walk_count = 0  #Idle mario image index

    #Jump sequence
    if not(bools.isJump):
        if keys[pg.K_SPACE] or keys[pg.K_w] or keys[pg.K_UP]:
            bools.isJump = True
            bools.forward = False
            bools.backward = False
            num.walk_count = 0
            
    else:
        num.walk_count = 3
        #0 - 10 - 0 pixel jump
        if num.jumpCount >= -10:
            neg = 1
            if num.jumpCount < 0:
                neg = -1
            num.y_move -= (num.jumpCount ** 2) * 0.5 * neg
            num.jumpCount -= 1
        
        else:
            bools.isJump = False
            num.jumpCount = 10