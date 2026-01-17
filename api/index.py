"""
Entry point para Vercel Serverless Functions
"""
import os
import sys

# Adicionar o diretório raiz ao path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)

# Importar o app Flask
from app import app

# Para Vercel Python, o Flask app deve ser exposto diretamente
# O @vercel/python detecta automaticamente aplicações WSGI/Flask
handler = app
