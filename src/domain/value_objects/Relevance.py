class Relevance:
    def __init__(self, relevance: int):
        if relevance>3 or relevance<0:
            raise ValueError("ERROR: relevance time limit is 999999999 minutes\n")
        self.relevance = relevance
    
    def repr(self):
        return self.relevance
    
    def __eq__(self, value):
        if self.relevance == value.relevance:
            return True
        return False