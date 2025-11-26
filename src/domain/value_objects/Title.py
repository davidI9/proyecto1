class Title:
    def __init__(self, title: str):
        if len(title)>50:
            raise ValueError("ERROR: title field limit is 50 characters\n")
        self.title = title
    
    def repr(self):
        return self.title
    
    def __eq__(self, value):
        if self.title == value.title:
            return True
        return False