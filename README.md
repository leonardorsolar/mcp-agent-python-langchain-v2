## 🧠 Objetivo

> Criamos o **LangGraph** + **LangChain OpenAI** que utilize ferramentas simples para responder ao usuário.

![Descrição da imagem](doc/tools.png)

> Agora vamos criar uma agnte com MCP

![Descrição da imagem](doc/mcpgif.gif)

## 1️⃣ Criar o ambiente do projeto

tenha o python3.10 instalado:

python3.10 --version

depois

```bash
python3.10 -m venv .venv
source .venv/bin/activate
```

---

## 2️⃣ Instalar dependências

```bash
pip install langchain-openai

```

e

```bash
pip install langgraph python-dotenv

```

---

## 3️⃣ Criar os arquivos do projeto

```bash
touch main.py tools.py .env
```

---

## 4️⃣ 📁 Estrutura final

```
agente_langgraph/
├── .env
├── .gitignore
├── main.py
├── tools.py
└── .venv/
```

---

### 3. Configure sua API key

Crie um arquivo `.env` na pasta do projeto:

```env
OPENAI_API_KEY=sk-sua_chave_aqui
```

> 📝 **Como obter uma API key:**
>
> 1. Acesse [platform.openai.com](https://platform.openai.com)
> 2. Faça login ou crie uma conta
> 3. Vá em "API Keys" e crie uma nova chave
> 4. Copie e cole no arquivo `.env`

Crie o arquivo .gitignore
No arquivo `.gitignore`, adicione:

```gitignore
# Ambiente virtual
.venv/
venv/
env/

# VSCode
.vscode/

# Arquivo de variáveis de ambiente
.env

# Cache do Python
__pycache__/
*.pyc
*.pyo
*.pyd

# Arquivos de log ou temporários
*.log
*.tmp

# Configuração de dependências (caso seja gerado automaticamente)
pip-wheel-metadata/
*.egg-info/
```

# Parte 1: MCP

Model Context Protocol (MCP) Para Sistemas de IA Generativa

### O Que é o Model Context Protocol (MCP)?

> O Model Context Protocol (MCP) é, essencialmente, um protocolo aberto e universal que padroniza a forma como aplicações de IA interagem com dados e serviços externos.

> É uma especificação aberta criada para padronizar como modelos de linguagem grande (LLMs) e agtentes de IA se conectam a dados, ferramnetas e serviços externos. Lançado pela Antropic em novembro de 2024.

-   Em vez de cada sistema de IA precisar de conectores específicos para cada fonte de dados (o que resultava no problema “M x N”, onde M modelos precisavam integrar com N ferramentas diferentes), o MCP propõe um caminho único. Com ele, modelos generativos e Agentes de IA podem acessar bases de dados, APIs, arquivos e outras ferramentas através de um protocolo unificado, independentemente de quem forneça o modelo ou a ferramenta.

![Descrição da imagem](doc/mcpmxn.png)
