#Object mechanics

class GameMechanics():
    def obstacle_mechanics(self, bools, num):
        if bools.forward:
            if bools.onPipe:
                if num.x_move in range(60,180) and bools.isJump:
                    num.y_move = num.y_move - 73
                    bools.onPipe = False
                elif num.x_move in range(60,70) and not(bools.isJump):
                    num.x_move = 60

            elif not(bools.onPipe):
                if num.x_move == 190:
                    num.y_move = num.y_move + 73
                    bools.onPipe = True 

        if bools.backward:
            if not(bools.onPipe):
                if num.x_move in range(30,60):
                    num.y_move = num.y_move + 73
                    bools.onPipe = True
                    
            elif bools.onPipe:
                if num.x_move in range(50,190) and bools.isJump:
                    num.y_move = num.y_move - 73
                    bools.onPipe = False
                elif num.x_move in range (180,190) and not(bools.isJump):
                    num.x_move = 190