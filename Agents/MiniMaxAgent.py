class AI_minimax_Agent:
    def __init__(self,ai_player='○',human_player='●', depth = 4):
        self.depth = depth
        self.ai_player = ai_player
        self.human_player = human_player

    #def minimax(self, depth,alpha,beta,is_maximizing):
