# streamlit-omdb-crud

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](#license)
[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](#requirements)
[![Streamlit](https://img.shields.io/badge/streamlit-app-brightgreen.svg)](#overview)

## 🎯 Visão Geral

`streamlit-omdb-crud` é um aplicativo web simples, construído com Streamlit, que permite buscar filmes/séries através da OMDb API e realizar operações CRUD (Create, Read, Update, Delete) sobre esses dados — armazenando metadados localmente, listando-os, editando e removendo conforme necessidade.

## 📁 Estrutura do Projeto

```
streamlit-omdb-crud/
│
├── database/           # Configuração de conexão com banco + DAO
├── util/               # Utilitários (helpers, logging, etc)
├── data/ script/       # scripts de dados (se houver)
├── main.py             # Arquivo principal: inicia o app Streamlit
├── requirements.txt    # Dependências
├── setup.py            # Configuração do pacote
├── .gitignore
└── README.md
```

## 🚀 Como Executar Localmente

1. Clone o repositório:

```bash
git clone https://github.com/DaviAlcanfor/streamlit-omdb-crud.git
cd streamlit-omdb-crud
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

3. Execute o aplicativo:

```bash
streamlit run main.py
```

4. Acesse:

```
http://localhost:8501
```

## ✅ Funcionalidades Principais

* Busca de filmes/séries pela OMDb API.
* Criação de entradas salvas localmente.
* Listagem de todos os filmes cadastrados.
* Edição de dados (Update).
* Remoção de itens (Delete).
* Interface web simples via Streamlit.

## 🔧 Tecnologias

* Python 3.x
* Streamlit
* Banco de dados conforme configuração em `database/config.py`
* Dependências adicionais em `requirements.txt`

## 📈 Possíveis Evoluções

* Filtros por gênero, ano, nota.
* Exportar/importar dados (CSV/JSON).
* Interface gráfica mais rica com capas e detalhes visuais.
* Deploy no Streamlit Cloud ou Heroku.
* Autenticação de usuários.

## 🛠️ Como Contribuir

1. Faça um fork.
2. Crie uma branch com sua feature.
3. Envie um Pull Request.

## 📄 Licença

MIT License. Veja o arquivo `LICENSE`.
