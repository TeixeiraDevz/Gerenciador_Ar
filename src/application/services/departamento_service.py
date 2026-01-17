from src.domain.dtos.departamento_dto import DepartamentoDTO
from src.infrastructure.repositories.departamento_repository import DepartamentoRepository
from src.infrastructure.mappers.departamento_mapper import DepartamentoMapper

class DepartamentoService:
    def __init__(self):
        self.repository = DepartamentoRepository()
        self.mapper = DepartamentoMapper()
    
    def listar_todos(self):
        entities = self.repository.find_all()
        return [self.mapper.entity_to_dto(entity) for entity in entities]
    
    def obter_por_id(self, id: int):
        entity = self.repository.find_by_id(id)
        return self.mapper.entity_to_dto(entity) if entity else None
