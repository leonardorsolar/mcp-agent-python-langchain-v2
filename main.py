import os
import warnings
from dotenv import load_dotenv
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from github_tool import GitHubIssueTool

# Carregar variáveis de ambiente
load_dotenv()

# Suprimir warnings de depreciação (opcional)
warnings.filterwarnings("ignore", category=DeprecationWarning)

def criar_agente():
    """Cria e configura o agente IA."""
    
    # Verificar se as variáveis estão definidas
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("Configure OPENAI_API_KEY no arquivo .env")
    
    # Inicializar o modelo de linguagem
    llm = ChatOpenAI(
        model="gpt-3.5-turbo",
        temperature=0.3,
        verbose=False  # Mudei para False para saída mais limpa
    )
    
    # Criar ferramenta do GitHub
    github_tool = GitHubIssueTool()
    
    # Inicializar agente
    agent = initialize_agent(
        tools=[github_tool],
        llm=llm,
        agent=AgentType.OPENAI_FUNCTIONS,
        verbose=False,  # Mudei para False para saída mais limpa
        handle_parsing_errors=True
    )
    
    return agent

def main():
    """Função principal."""
    print("🤖 Iniciando Agente GitHub...")
    
    try:
        # Criar agente
        agent = criar_agente()
        
        print("\n✅ Agente criado com sucesso!")
        print("💬 Digite suas solicitações (ou 'sair' para terminar):")
        print("📝 Exemplo: 'Crie uma issue sobre bug no login'")
        print("-" * 50)
        
        while True:
            # Receber input do usuário
            user_input = input("\n👤 Você: ").strip()
            
            if user_input.lower() in ['sair', 'exit', 'quit']:
                print("👋 Até logo!")
                break
            
            if not user_input:
                continue
            
            try:
                # Executar agente (usando invoke ao invés de run)
                print("\n🤖 Agente: Processando...")
                resposta = agent.invoke({"input": user_input})
                print(f"\n🤖 Agente: {resposta['output']}")
                
            except Exception as e:
                print(f"\n❌ Erro: {str(e)}")
                
    except Exception as e:
        print(f"❌ Erro ao inicializar: {str(e)}")

if __name__ == "__main__":
    main()