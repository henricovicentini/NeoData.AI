### NeoData – Organize, Limpe, Reutilize  

Sistema de ingestão e limpeza de dados estruturados, focado em automação, qualidade e reutilização para relatórios, sistemas e modelos de IA.

---

## 🎯 Objetivo

Fornecer uma plataforma capaz de ingerir dados (CSV/SQL), detectar inconsistências, corrigir automaticamente e disponibilizar os dados tratados para reuso em análises e aplicações preditivas.

---

## 🔍 Problema

Empresas frequentemente enfrentam:  

- Dados ausentes, duplicados ou inconsistentes.  
- Outliers que distorcem análises.  
- Integrações manuais demoradas entre diferentes fontes de dados.

---

## ✨ Solução

- Ingestão automatizada de arquivos CSV/Excel e bancos SQL.  
- Análise automática de falhas nos dados.  
- Limpeza inteligente com IA + regras (imputação com KNN/Random Forest, tratamento de outliers, conversão de formatos).  
- Exportação simplificada: CSV/JSON, integração com bancos e dashboards (Power BI, Metabase).  
- Dashboard de demonstração mostrando comparação **antes vs depois** da limpeza.

---

## 🛠️ Tecnologias

| Área         | Ferramentas                                   |
|-------------|-----------------------------------------------|
| Back-end    | Python (Flask ou FastAPI), SQLAlchemy        |
| Front-end   | HTML/CSS, Bootstrap ou Tailwind              |
| Dados       | Pandas, Numpy, Scikit-learn, Great Expectations |
| Banco       | SQLite (protótipo), PostgreSQL/MySQL (produção) |
| Visualização| Plotly, Matplotlib, Dash                      |

---

## 📂 Estrutura do Repositório

```
NeoData.IA/ 
│── run.py                     # Arquivo principal para rodar a aplicação Flask
│── requirements.txt            # Dependências do projeto
│
├── app/
│   ├── __init__.py             # Inicializa o Flask (configuração principal)
│   ├── routes.py               # Rotas principais (upload, raw, clean, profile, dashboard)
│   │
│   ├── auth/                   # Módulo de autenticação
│   │   ├── __init__.py
│   │   ├── routes.py           # Login, logout, cadastro
│   │
│   ├── pred/                   # Módulo de predição (placeholder)
│   │   ├── __init__.py
│   │   ├── routes.py
│   │
│   ├── static/                 # Arquivos estáticos (CSS, JS, imagens, gráficos)
│   │   ├── css/
│   │   │   └── style.css
│   │   ├── js/
│   │   │   └── script.js
│   │   └── graphs/             # Gráficos gerados pelo matplotlib
│   │
│   ├── templates/              # Templates HTML estilizados
│   │   ├── base.html           # Estrutura base (head + body)
│   │   ├── header.html         # Cabeçalho/nav
│   │   ├── home.html           # Tela inicial
│   │   ├── login.html          # Tela de login
│   │   ├── cadastro.html       # Tela de cadastro
│   │   ├── raw.html            # Dados brutos
│   │   ├── clean.html          # Dados limpos + download CSV
│   │   ├── profile.html        # Placeholder de perfil
│   │   ├── dashboard.html      # Gráficos comparativos
│   │  
│   │
│   └── utils/                  # Funções auxiliares
│       ├── __init__.py
│       ├── cleaning.py         # Lógica de limpeza (pandas)
│       └── graphs.py           # Geração de gráficos (matplotlib)
```

---

## 🚀 Como rodar o projeto

### 1. Clonar o repositório

```bash
git clone https://github.com/henricovicentini/NeoData.git
cd NeoData
```

### 2. Criar e ativar o ambiente virtual

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows (PowerShell):**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Instalar dependências

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Configurar variáveis de ambiente (opcional)

Se houver `.env` ou configuração necessária, configure conforme o modelo `env.example`.

### 5. Rodar a aplicação

**Flask:**

```bash
export FLASK_APP=app.py   # Linux/macOS
set FLASK_APP=app.py      # Windows
flask run
```

**FastAPI:**

```bash
uvicorn app:app --reload
```

Acesse:  
- Flask → [http://127.0.0.1:5000](http://127.0.0.1:5000)  
- FastAPI → [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 6. Testar funcionalidades

- Enviar arquivos CSV/Excel para ingestão.  
- Visualizar dashboard de comparação antes/depois.  
- Exportar dados tratados em CSV/JSON ou integrar com banco de dados.

---

## 📝 Licença

MIT

---

## 📫 Contato

Para mais informações ou dúvidas, entre em contato:  

**Email:** vicentinihenrico@gmail.com
