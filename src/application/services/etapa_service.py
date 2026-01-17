from src.domain.dtos.etapa_dto import EtapaDTO
from src.infrastructure.repositories.etapa_repository import EtapaRepository
from src.infrastructure.mappers.etapa_mapper import EtapaMapper

class EtapaService:
    def __init__(self):
        self.repository = EtapaRepository()
        self.mapper = EtapaMapper()
    
    def listar_por_departamento(self, departamento_id: int):
        entities = self.repository.find_by_departamento_id(departamento_id)
        return [self.mapper.entity_to_dto(entity) for entity in entities]
    
    def obter_por_id(self, id: int):
        entity = self.repository.find_by_id(id)
        return self.mapper.entity_to_dto(entity) if entity else None
