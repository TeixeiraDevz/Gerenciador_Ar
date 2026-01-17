from src.domain.entities.departamento import Departamento
from src.infrastructure.database.database_config import get_db_connection

class DepartamentoRepository:
    def __init__(self):
        pass
    
    def find_all(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM departamentos ORDER BY nome')
        rows = cursor.fetchall()
        conn.close()
        
        return [Departamento(id=row['id'], nome=row['nome']) for row in rows]
    
    def find_by_id(self, id: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM departamentos WHERE id = ?', (id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return Departamento(id=row['id'], nome=row['nome'])
        return None
    
    def find_by_nome(self, nome: str):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM departamentos WHERE nome = ?', (nome,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return Departamento(id=row['id'], nome=row['nome'])
        return None
