from uuid import uuid4
from ..value_objects.Title import Title
from ..value_objects.EndDate import EndDate
from ..value_objects.Description import Description
from ..value_objects.Duration import Duration
from ..value_objects.Relevance import Relevance

class Task:
    def __init__(self, 
        title: Title, 
        end_date: EndDate, 
        description: Description = Description("UNKNOWN"), 
        duration: Duration = Duration(0), 
        relevance: Relevance = Relevance(1), 
        finnished: bool = False
    ):
        
        self._id = uuid4()
        self._title = title
        self._end_date = end_date
        self._description = description
        self._duration = duration
        self._relevance = relevance
        self._finnished = finnished
    