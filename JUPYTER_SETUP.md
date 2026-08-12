# Ambiente Jupyter Completo

Este projeto contém um ambiente Jupyter configurado com todas as ferramentas necessárias para análise de dados em Python.

## 📦 Dependências Instaladas

- **Jupyter Lab**: Interface interativa avançada
- **Notebook**: Interface clássica do Jupyter
- **NumPy**: Computação científica
- **Pandas**: Manipulação e análise de dados
- **Matplotlib**: Visualização de dados
- **Seaborn**: Visualização estatística
- **SciPy**: Computação científica avançada
- **Scikit-Learn**: Machine Learning

## 🚀 Como Usar

### Opção 1: Iniciar Jupyter Lab (Recomendado)
```bash
jupyter lab
```
Acesse no navegador: `http://localhost:8888`

### Opção 2: Iniciar Jupyter Notebook Clássico
```bash
jupyter notebook
```

### Opção 3: Usar no VS Code
- Abra o arquivo `analise_dados.ipynb` no VS Code
- Clique em "Executar Tudo" ou execute célula por célula

## 📖 Estrutura do Notebook

O arquivo `analise_dados.ipynb` contém exemplos práticos de:

1. **Importação de Bibliotecas** - Setup inicial
2. **NumPy** - Operações com arrays
3. **Pandas** - Manipulação de DataFrames
4. **Matplotlib** - Visualizações
5. **Agrupamento e Filtragem** - Análise de dados
6. **Machine Learning** - Classificação com Random Forest

## 📋 Reinstalar Dependências

Se precisar reinstalar todas as dependências:
```bash
pip install -r requirements.txt
```

## 🔧 Configurações Úteis

Para salvar configurações padrão do Jupyter:
```bash
jupyter notebook --generate-config
```

O arquivo de configuração será criado em:
- Linux/Mac: `~/.jupyter/jupyter_notebook_config.py`
- Windows: `%APPDATA%\.jupyter\jupyter_notebook_config.py`

## 💡 Dicas

- Use `Tab` para autocompletar código
- Use `Shift+Tab` para visualizar documentação
- Use `Ctrl+/` para comentar/descomentar linhas
- Use `Ctrl+Shift+P` (VS Code) para comandos rápidos
- Execute `?função_name` ou `?função_name?` para help

## 📚 Recursos Adicionais

- [Documentação Jupyter](https://jupyter.org/)
- [NumPy Documentation](https://numpy.org/doc/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Scikit-Learn Documentation](https://scikit-learn.org/stable/)
