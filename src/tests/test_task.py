from ..domain.Task import Task
from uuid import UUID

def test_task_creation():
    
    #arrange
    #act
    task = Task(title="testTask", end_date="2026/06/11")
    #assert
    assert(task._title == "testTask")
    assert(task._description == "UNKNOWN")
    assert(task._end_date == "2026/06/11")
    assert(task._duration == 0)
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
    #act
    task = Task(title="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
    #assert
    
    
    
    #TERMINAR EL TEST