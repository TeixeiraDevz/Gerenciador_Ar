from src.domain.entities.etapa import Etapa
from src.domain.dtos.etapa_dto import EtapaDTO

class EtapaMapper:
    @staticmethod
    def entity_to_dto(entity: Etapa) -> EtapaDTO:
        if not entity:
            return None
        return EtapaDTO(
            id=entity.id,
            numero=entity.numero,
            nome=entity.nome,
            responsavel=entity.responsavel,
            departamento_id=entity.departamento_id
        )
    
    @staticmethod
    def dto_to_entity(dto: EtapaDTO) -> Etapa:
        if not dto:
            return None
        return Etapa(
            id=dto.id,
            numero=dto.numero,
            nome=dto.nome,
            responsavel=dto.responsavel,
            departamento_id=dto.departamento_id
        )
