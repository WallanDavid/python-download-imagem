# 🖼️ Python Download de Imagens

Este é um script em **Python** que permite baixar **todas as imagens de um site** informado pelo usuário. Ele oferece tanto uma **interface de linha de comando (CLI)** quanto uma **interface gráfica (GUI)** para facilitar o uso e melhorar a experiência.

---

## ⚙️ Funcionalidades

- 🔽 **Download de Imagens:** Baixa automaticamente todas as imagens de um site informado
- 🌐 **Escolha de URL:** Usuário informa o site de onde as imagens serão baixadas
- 📁 **Escolha de Pasta de Saída:** Usuário define onde salvar as imagens
- 📊 **Exibição de Progresso:** Mostra status durante o download
- 🔄 **Gerenciamento de Exceções:** Trata erros de conexão, URLs inválidas, timeout e mais
- 🖥️ **Interface CLI:** Versão simples para terminal
- 🖱️ **Interface GUI:** Versão com janelas gráficas (intuitiva)
- ⚙️ **Opções de Configuração:** Timeout, número de tentativas, entre outros
- 💬 **Feedback Interativo:** Mensagens durante a execução para guiar o usuário

---

## 📦 Como Usar

1. **Clone o repositório:**
   git clone https://github.com/WallanDavid/python-download-imagem.git

2. **Acesse o diretório do projeto:**
   cd python-download-imagem

3. **(Opcional) Crie e ative um ambiente virtual:**
   python -m venv venv  
   source venv/bin/activate (Linux/macOS)  
   venv\Scripts\activate (Windows)

4. **Instale as dependências:**
   pip install -r requirements.txt

---

## ▶️ Execução

- **Modo CLI (linha de comando):**
  python main_cli.py

- **Modo GUI (gráfico):**
  python main_gui.py

---

## 📁 Resultado

As imagens serão salvas na pasta especificada durante a execução. O script garante que não haja duplicações e evita arquivos corrompidos.

---

## 🛠️ Possíveis Melhorias Futuras

- Suporte a filtros (por tipo de imagem, resolução etc.)
- Histórico de URLs acessadas
- Modo headless (sem abrir janela na GUI)
- Exportar log de imagens baixadas

---

## 📜 Licença

Este projeto está licenciado sob os termos da [MIT License](LICENSE).

---

## 📫 Contato

**Desenvolvedor:** Wallan David Peixoto  
**Email:** bobwallan2@gmail.com  
**LinkedIn:** https://www.linkedin.com/in/wallanpeixoto
