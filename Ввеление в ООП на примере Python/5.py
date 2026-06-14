class BigBell:
    def __init__(self):
        self.cnt = 0
    
    def sound(self):
        if self.cnt % 2 == 0:
            print("ding")
        else:
            print("dong")
        self.cnt += 1



bell = BigBell()
bell.sound()
bell.sound()
bell.sound()
