from src.domain.value_objects.Title import Title
from src.domain.value_objects.Description import Description
from src.domain.value_objects.EndDate import EndDate
from src.domain.value_objects.Relevance import Relevance
from src.domain.value_objects.Duration import Duration
from src.domain.entities.Task import Task
from ..dto.SaveTaskDTO import SaveTaskDTO
from src.domain.repositories.TaskRepository import TaskRepository


class CreateTaskHandler:
    
    def __init__(self, repository: TaskRepository):
        self.repository = repository
        

    def handle(self, DTO: SaveTaskDTO):
        task_params = {
            "title": Title(DTO.title),
            "end_date": EndDate(DTO.end_date),
        }
        
        if DTO.description is not None:
            task_params["description"] = Description(DTO.description)
            
        if DTO.duration is not None:
            task_params["duration"] = Duration(DTO.duration)

        if DTO.relevance is not None:
            task_params["relevance"] = Relevance(DTO.relevance)
            
        if DTO.finnished is not None:
            task_params["finnished"] = DTO.finnished

        task = Task(**task_params)

        self.repository.save(task)