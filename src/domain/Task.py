from uuid import uuid4

class Task:
    def __init__(self, title: str, end_date: str, description: str = "UNKNOWN", duration: int = 0, relevance: int = 1, finnished: bool = False):
        self._id = uuid4()
        self._title = title
        self._end_date = end_date
        self._description = description
        self._duration = duration
        self._relevance = relevance
        self._finnished = finnished
    