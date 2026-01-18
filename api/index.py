"""
Entry point para Vercel Serverless Functions
"""
import os
import sys

# Adicionar o diretório raiz ao path
root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, root_dir)

# IMPORTANTE:
# No runtime do Vercel, exportar um objeto "handler" (que não seja função/classe esperada)
# pode causar erro no vc__handler__python.py.
# Para Flask, exportamos o objeto WSGI como "app".

from app import app as app  # Vercel irá detectar o WSGI callable
