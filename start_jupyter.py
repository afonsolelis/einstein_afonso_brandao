#!/usr/bin/env python3
"""
Script para iniciar Jupyter Lab ou Notebook facilmente
"""

import subprocess
import sys
import argparse

def main():
    parser = argparse.ArgumentParser(
        description='Iniciar Jupyter Lab ou Notebook',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Exemplos de uso:
  python start_jupyter.py lab          # Inicia Jupyter Lab
  python start_jupyter.py notebook     # Inicia Jupyter Notebook
  python start_jupyter.py --help       # Mostra esta mensagem
        """
    )
    
    parser.add_argument(
        'mode',
        nargs='?',
        default='lab',
        choices=['lab', 'notebook', 'lab-daemon'],
        help='Modo de execução (padrão: lab)'
    )
    
    parser.add_argument(
        '--port',
        type=int,
        default=8888,
        help='Porta para executar Jupyter (padrão: 8888)'
    )
    
    args = parser.parse_args()
    
    print(f"🚀 Iniciando Jupyter {args.mode.upper()}...")
    print(f"📍 Porta: {args.port}")
    print(f"🌐 Acesse: http://localhost:{args.port}")
    print()
    
    try:
        if args.mode == 'lab':
            subprocess.run(
                ['jupyter', 'lab', f'--port={args.port}'],
                check=True
            )
        elif args.mode == 'lab-daemon':
            subprocess.run(
                ['jupyter', 'lab', f'--port={args.port}', '--no-browser'],
                check=True
            )
        else:  # notebook
            subprocess.run(
                ['jupyter', 'notebook', f'--port={args.port}'],
                check=True
            )
    except FileNotFoundError:
        print("❌ Erro: Jupyter não encontrado!")
        print("📦 Instale com: pip install jupyter jupyterlab")
        sys.exit(1)
    except KeyboardInterrupt:
        print("\n\n👋 Jupyter encerrado pelo usuário")
        sys.exit(0)

if __name__ == '__main__':
    main()
