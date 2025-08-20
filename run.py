# run.py — ponto de entrada para executar o Flask
from app import create_app  # importa a factory que cria a aplicação

# Cria a app usando a factory (permite testes e configuração modular)
app = create_app()

# Executa o servidor de desenvolvimento quando rodar `python run.py`
if __name__ == "__main__":
    # debug=True recarrega a app em mudanças de código (não usar em produção)
    app.run(debug=True)
