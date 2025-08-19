###  NeoData.AI – Organize, Limpe, Reutilize  

Projeto desenvolvido como **sistema de ingestão e limpeza de dados estruturados**, focado em **qualidade, automação e reutilização de dados** para relatórios, sistemas e modelos de IA.  

---

## 🎯 Objetivo  
Criar uma plataforma capaz de **ingerir dados (CSV/SQL)**, **detectar inconsistências**, **corrigir automaticamente** e **disponibilizar os dados tratados** para reuso em aplicações analíticas e preditivas.  

---

## 🔍 Problema  
Empresas frequentemente enfrentam:  
- Dados com **valores ausentes, duplicados ou inconsistentes**.  
- **Outliers** que distorcem análises.  
- **Integrações manuais** e demoradas entre fontes de dados.  

---

## ✨ Solução  
- **Ingestão automatizada** (arquivos CSV/Excel e bancos SQL).  
- **Análise automática** para detectar falhas nos dados.  
- **Limpeza inteligente com IA + regras** (imputação com KNN/Random Forest, tratamento de outliers, conversão de formatos).  
- **Reutilização simplificada**: exportação em CSV/JSON, integração com bancos de dados e dashboards (Power BI, Metabase).  
- **Dashboard de demonstração** com comparação **antes vs depois** da limpeza.  

---

## 🛠️ Tecnologias  

| Área         | Ferramentas |
|--------------|-------------|
| **Back-end** | Python (Flask ou FastAPI), SQLAlchemy |
| **Front-end** | HTML/CSS, Bootstrap ou Tailwind |
| **Dados** | Pandas, Numpy, Scikit-learn, Great Expectations |
| **Banco** | SQLite (protótipo), PostgreSQL/MySQL (produção) |
| **Visualização** | Plotly, Matplotlib, Dash |

---

## 📅 Cronograma (Fases)  

- **Fase 1 (MVP)** → Upload CSV → Limpeza → Download CSV  
- **Fase 2** → Integração via API (FastAPI/Flask)  
- **Fase 3** → Conexão direta com bancos SQL  
- **Fase 4** → Dashboard interativo (comparação antes vs depois)  

---

## 🚀 Próximos Passos  
- [ ] Criar protótipo inicial com upload de CSV.  
- [ ] Adicionar banco SQL para armazenar dados brutos e limpos.  
- [ ] Disponibilizar API segura para integração com outros sistemas.  
- [ ] Desenvolver visualização interativa dos resultados da limpeza.  
