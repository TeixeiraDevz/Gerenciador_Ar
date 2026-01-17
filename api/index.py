"""
Entry point para Vercel Serverless Functions
"""
import os
import sys

# Adicionar o diretório raiz ao path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)

try:
    from app import app
    
    # Vercel precisa que o handler seja exposto
    # Para Flask, o app já é o handler
    handler = app
except Exception as e:
    # Se houver erro, criar um handler de fallback
    def handler(request):
        return {
            'statusCode': 500,
            'body': f'Error initializing app: {str(e)}'
        }
