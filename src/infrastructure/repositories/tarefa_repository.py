from src.domain.entities.tarefa import Tarefa
from src.infrastructure.database.database_config import get_db_connection

class TarefaRepository:
    def __init__(self):
        pass
    
    def find_by_etapa_id(self, etapa_id: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM tarefas 
            WHERE etapa_id = ? 
            ORDER BY id
        ''', (etapa_id,))
        rows = cursor.fetchall()
        conn.close()
        
        return [Tarefa(
            id=row['id'],
            descricao=row['descricao'],
            concluida=bool(row['concluida']),
            etapa_id=row['etapa_id']
        ) for row in rows]
    
    def find_by_id(self, id: int):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tarefas WHERE id = ?', (id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            return Tarefa(
                id=row['id'],
                descricao=row['descricao'],
                concluida=bool(row['concluida']),
                etapa_id=row['etapa_id']
            )
        return None
    
    def update_concluida(self, id: int, concluida: bool):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE tarefas 
            SET concluida = ? 
            WHERE id = ?
        ''', (1 if concluida else 0, id))
        conn.commit()
        conn.close()
    
    def find_all(self):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM tarefas ORDER BY etapa_id, id')
        rows = cursor.fetchall()
        conn.close()
        
        return [Tarefa(
            id=row['id'],
            descricao=row['descricao'],
            concluida=bool(row['concluida']),
            etapa_id=row['etapa_id']
        ) for row in rows]
