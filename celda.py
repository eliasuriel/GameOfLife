class Cell:
    def __init__(self,state=False):
        self.state = state
        self.next_state =state
        
    def update_state(self):
        self.state = self.next_state

    def following_state(self,neighbors_alive):
        if self.state:
            if neighbors_alive < 2 or neighbors_alive > 3:
                self.next_state = False
            else:
                self.next_state = True
        else:
            if neighbors_alive == 3:
                self.next_state = True
            else:
                self.next_state = False

