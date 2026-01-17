from src.domain.dtos.tarefa_dto import TarefaDTO
from src.infrastructure.repositories.tarefa_repository import TarefaRepository
from src.infrastructure.mappers.tarefa_mapper import TarefaMapper

class TarefaService:
    def __init__(self):
        self.repository = TarefaRepository()
        self.mapper = TarefaMapper()
    
    def listar_por_etapa(self, etapa_id: int):
        entities = self.repository.find_by_etapa_id(etapa_id)
        return [self.mapper.entity_to_dto(entity) for entity in entities]
    
    def obter_por_id(self, id: int):
        entity = self.repository.find_by_id(id)
        return self.mapper.entity_to_dto(entity) if entity else None
    
    def atualizar_conclusao(self, id: int, concluida: bool):
        self.repository.update_concluida(id, concluida)
    
    def listar_todas(self):
        entities = self.repository.find_all()
        return [self.mapper.entity_to_dto(entity) for entity in entities]
