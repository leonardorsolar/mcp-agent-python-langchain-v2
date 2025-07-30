import os
from github import Github
from langchain.tools import BaseTool
from typing import Type, Optional
from pydantic import BaseModel, Field

class CreateIssueInput(BaseModel):
    """Input para criar uma issue no GitHub."""
    title: str = Field(description="Título da issue")
    body: str = Field(description="Descrição/corpo da issue")

class GitHubIssueTool(BaseTool):
    """Ferramenta para criar issues no GitHub."""
    
    name: str = "create_github_issue"
    description: str = "Cria uma nova issue em um repositório do GitHub. Use quando o usuário pedir para criar, reportar ou abrir uma issue."
    args_schema: Type[BaseModel] = CreateIssueInput
    
    # Campos do Pydantic para armazenar configuração
    github_token: Optional[str] = Field(default=None, exclude=True)
    github_username: Optional[str] = Field(default=None, exclude=True)
    github_repo: Optional[str] = Field(default=None, exclude=True)
    github_client: Optional[Github] = Field(default=None, exclude=True)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Carregar configurações do ambiente
        self.github_token = os.getenv("GITHUB_TOKEN")
        self.github_username = os.getenv("GITHUB_USERNAME")
        self.github_repo = os.getenv("GITHUB_REPO")
        
        if not all([self.github_token, self.github_username, self.github_repo]):
            raise ValueError("Configure GITHUB_TOKEN, GITHUB_USERNAME e GITHUB_REPO no arquivo .env")
        
        # Inicializar cliente GitHub
        self.github_client = Github(self.github_token)
    
    def _run(self, title: str, body: str) -> str:
        """Executa a criação da issue."""
        try:
            # Obter o repositório
            repo_name = f"{self.github_username}/{self.github_repo}"
            repo = self.github_client.get_repo(repo_name)
            
            # Criar a issue
            issue = repo.create_issue(title=title, body=body)
            
            return f"✅ Issue criada com sucesso!\n📝 Título: {title}\n🔗 URL: {issue.html_url}\n📊 Número: #{issue.number}"
            
        except Exception as e:
            return f"❌ Erro ao criar issue: {str(e)}\n💡 Verifique se o repositório '{self.github_username}/{self.github_repo}' existe e se você tem permissões."