"""
Entry point para Vercel Serverless Functions
"""
from app import app

# Vercel espera a variável 'handler'
handler = app
