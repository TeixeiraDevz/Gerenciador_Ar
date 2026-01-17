"""
Entry point para Vercel Serverless Functions
"""
import os
import sys

# Adicionar o diretório raiz ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app

# Vercel espera que a aplicação seja exposta diretamente
handler = app
