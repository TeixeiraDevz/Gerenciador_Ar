class EtapaDTO:
    def __init__(self, id: int = None, numero: int = None, nome: str = None,
                 responsavel: str = None, departamento_id: int = None):
        self.id = id
        self.numero = numero
        self.nome = nome
        self.responsavel = responsavel
        self.departamento_id = departamento_id
