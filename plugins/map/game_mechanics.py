#Object mechanics

class GameMechanics():
    def obstacle_mechanics(self, bools, num, mech_pipe_map):
        print(mech_pipe_map)
        if bools.forward:
            if bools.onPipe:
                if num.x_move in range(mech_pipe_map,mech_pipe_map + 120) and bools.isJump:
                    num.y_move = num.y_move - 73
                    bools.onPipe = False
                elif num.x_move in range(mech_pipe_map,mech_pipe_map + 10) and not(bools.isJump):
                    num.x_move = mech_pipe_map

            elif not(bools.onPipe):
                if num.x_move == mech_pipe_map + 130:
                    num.y_move = num.y_move + 73
                    bools.onPipe = True 

        if bools.backward:
            if not(bools.onPipe):
                if num.x_move in range(mech_pipe_map - 30,mech_pipe_map):
                    num.y_move = num.y_move + 73
                    bools.onPipe = True
                    
            elif bools.onPipe:
                if num.x_move in range(mech_pipe_map - 10,mech_pipe_map + 130) and bools.isJump:
                    num.y_move = num.y_move - 73
                    bools.onPipe = False
                elif num.x_move in range (mech_pipe_map + 120,mech_pipe_map + 130) and not(bools.isJump):
                    num.x_move = mech_pipe_map + 130