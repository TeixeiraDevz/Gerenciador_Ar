from src.domain.entities.departamento import Departamento
from src.domain.dtos.departamento_dto import DepartamentoDTO

class DepartamentoMapper:
    @staticmethod
    def entity_to_dto(entity: Departamento) -> DepartamentoDTO:
        if not entity:
            return None
        return DepartamentoDTO(
            id=entity.id,
            nome=entity.nome
        )
    
    @staticmethod
    def dto_to_entity(dto: DepartamentoDTO) -> Departamento:
        if not dto:
            return None
        return Departamento(
            id=dto.id,
            nome=dto.nome
        )
