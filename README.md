# 📊 API de Estatísticas com FastAPI, CI/CD e Docker

Este projeto é uma API desenvolvida em Python com FastAPI para calcular estatísticas (média, mediana e moda) a partir de uma lista de números. Ele foi criado com foco em práticas modernas de DevOps, integrando **testes automatizados**, **CI/CD com GitHub Actions** e **containerização com Docker**.

---

## ⚙️ Funcionalidades

- `POST /stats`: Recebe um JSON com uma lista de números e retorna:
  - Média
  - Mediana
  - Moda (ou erro se não houver moda única)

---

## 🚀 Tecnologias Utilizadas

- [FastAPI](https://fastapi.tiangolo.com/)
- [Pytest](https://docs.pytest.org/)
- [Docker](https://www.docker.com/)
- [GitHub Actions](https://github.com/features/actions)
- [Pydantic](https://docs.pydantic.dev/)

---

## 📦 Como Rodar Localmente

### Pré-requisitos
- Python 3.11+
- Docker (opcional)

### 1. Clonar o repositório
```bash
git clone https://github.com/alepertile28/api-ci-cd.git
cd api-ci-cd

```

### 2. Rodar localmente (modo dev)
```bash
source fastapi-env/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```
Acesse a documentação interativa em: http://localhost:8000/docs

# Rodando os Testes

```bash
pytest
```
Inclui testes pada:
* Respostas válidas
* Dados inválidos
* Casos sem moda única

## Rodando com Docker

### Build da imagem
```bash
docker build -t stast-api .
```

### Executar o container
```bash
docker run -p 8000:8000 stats-api
```
Acesse: http://localhost:8000/docs

## CI/CD

Este projeto usa **GitHub Actions** com os seguintes passos:
* flake8: Análise de código (lint)
* black --check: Formatação
* pytest: Execução de testes automatizados
* Build e push da imagem do container pro DockerHUB (CD)

##  Estrutura do Projeto

```plaintext
api-ci-cd/                     
├── app/
│   ├── main.py                # Código principal da API
├── tests/                     
│   └── test_main.py           # Testes automatizados
├── Dockerfile                 # Imagem Docker customizada 
├── .github/workflows/         # CI/CD com GitHub Actions
├── requirements.txt           # Dependencias do python
└── README.md                  # Este arquivo
```

### Exemplos de Uso

### Requisição
```http
POST /stats
Content-Type: application/json

{
    "numbers": [1, 2, 2, 3]
}
```
### Resposta
```http
{
    "mean": 2.0,
    "median": 2.0,
    "mode": 2
}
```
##  Autor

**Alexandre Augusto Pertile da Luz**  
[LinkedIn](https://www.linkedin.com/in/alexandre-pertile-36a350102) | [GitHub](https://github.com/alepertile28)
