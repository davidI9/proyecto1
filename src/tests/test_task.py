from src.domain.entities.Task import Task
from src.domain.value_objects.Title import Title
from src.domain.value_objects.EndDate import EndDate
from src.domain.value_objects.Description import Description
from src.domain.value_objects.Duration import Duration
from src.domain.value_objects.Relevance import Relevance
from uuid import UUID
import pytest

def test_task_creation():
    #arrange
    #act
    task = Task(title=Title("testTask"), end_date=EndDate("2026/06/11"))
    #assert
    assert(task._title == Title("testTask"))
    assert(task._description == Description("UNKNOWN"))
    assert(task._end_date == EndDate("2026/06/11"))
    assert(task._duration == Duration(0))
    assert(task._relevance == Relevance(1))
    assert(task._finnished == False)

def test_task_has_id():
    
    #arrange
    #act
    task = Task("test Task", "2026/06/11")
    
    #assert
    assert(hasattr(task, "_id") == True)
    assert(isinstance(task._id, UUID))

def test_title_cap_is_50_letters():
    #arrange
    title="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    #act
    #assert
    with pytest.raises(ValueError):
        title2 = Title(title)

def test_date_format_incorrect():
    #arrange
    date = "11/06/2026"
    #act
    #assert
    with pytest.raises(ValueError):
        date2 = EndDate(date)

def test_date_format_correct():
        #arrange
    date = "2026/06/11"
    #act
    date2 = EndDate(date)
    #assert
    assert(isinstance(date2, EndDate))

def test_desc_cap_is_200_letters():
    #arrange
    desc="a"*201
    #act
    #assert
    with pytest.raises(ValueError):
        desc2 = Description(desc)

def test_duration_cap_is_999_999_999():
    #arrange
    duration=999999999999
    #act
    #assert
    with pytest.raises(ValueError):
        duration2 = Duration(duration)

def test_relevance_must_be_between_0_and_3():
    #arrange
    relevance1=1
    relevance2=4
    
    #act
    relevance3 = Relevance(relevance1)
    
    #assert
    assert(isinstance(relevance3, Relevance))
    with pytest.raises(ValueError):
        relevance4 = Relevance(relevance2)