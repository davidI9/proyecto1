class Description:
    def __init__(self, desc: str):
        if len(desc)>200:
            raise ValueError("ERROR: description field limit is 200 characters\n")
        self.desc = desc
    
    def repr(self):
        return self.desc
    
    def __eq__(self, value):
        if self.desc == value.desc:
            return True
        return False