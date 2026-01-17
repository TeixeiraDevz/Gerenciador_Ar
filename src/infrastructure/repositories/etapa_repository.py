from src.domain.entities.etapa import Etapa
from src.infrastructure.database.database_config import get_db_connection

class EtapaRepository:
    def __init__(self):
        pass
    
    def find_by_departamento_id(self, departamento_id: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM etapas 
            WHERE departamento_id = ? 
            ORDER BY numero
        ''', (departamento_id,))
        rows = cursor.fetchall()
        conn.close()
        
        return [Etapa(
            id=row['id'],
            numero=row['numero'],
            nome=row['nome'],
            responsavel=row['responsavel'],
            departamento_id=row['departamento_id']
        ) for row in rows]
    
    def find_by_id(self, id: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM etapas WHERE id = ?', (id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return Etapa(
                id=row['id'],
                numero=row['numero'],
                nome=row['nome'],
                responsavel=row['responsavel'],
                departamento_id=row['departamento_id']
            )
        return None
