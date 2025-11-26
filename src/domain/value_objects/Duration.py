class Duration:
    def __init__(self, duration: int):
        if duration>999999999:
            raise ValueError("ERROR: duration time limit is 999999999 minutes\n")
        self.duration = duration
    
    def repr(self):
        return self.duration
    
    def __eq__(self, value):
        if self.duration == value.duration:
            return True
        return False