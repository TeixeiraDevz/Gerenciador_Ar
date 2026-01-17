class TarefaDTO:
    def __init__(self, id: int = None, descricao: str = None,
                 concluida: bool = False, etapa_id: int = None):
        self.id = id
        self.descricao = descricao
        self.concluida = concluida
        self.etapa_id = etapa_id
