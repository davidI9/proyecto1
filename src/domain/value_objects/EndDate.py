from datetime import datetime

class EndDate:
    def __init__(self, date: str):
        try:
            datetime.strptime(date, "%Y/%m/%d")
        except:
            raise ValueError("ERROR: incorrect date format, end date should follow AAAA/MM/DD format")
        
        self.date = date
    
    def repr(self):
        return self.date
    
    def __eq__(self, value):
        if self.date == value.date:
            return True
        
        return False