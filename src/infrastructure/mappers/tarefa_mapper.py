from src.domain.entities.tarefa import Tarefa
from src.domain.dtos.tarefa_dto import TarefaDTO

class TarefaMapper:
    @staticmethod
    def entity_to_dto(entity: Tarefa) -> TarefaDTO:
        if not entity:
            return None
        return TarefaDTO(
            id=entity.id,
            descricao=entity.descricao,
            concluida=entity.concluida,
            etapa_id=entity.etapa_id
        )
    
    @staticmethod
    def dto_to_entity(dto: TarefaDTO) -> Tarefa:
        if not dto:
            return None
        return Tarefa(
            id=dto.id,
            descricao=dto.descricao,
            concluida=dto.concluida,
            etapa_id=dto.etapa_id
        )
