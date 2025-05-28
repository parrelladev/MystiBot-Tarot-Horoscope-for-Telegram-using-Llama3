
# MystiBot - Bot de Tarot e Horóscopo para Telegram

Um bot do Telegram que oferece leituras de tarot e horóscopo diário, utilizando a API do Ollama para gerar interpretações personalizadas.

## 🚀 Funcionalidades

- **🔮 Tarot**: Realiza leituras de tarot com 3 cartas, oferecendo interpretações personalizadas baseadas na pergunta do usuário
- **✨ Horóscopo**: Fornece horóscopo diário para todos os signos do zodíaco
- **🤖 Interface Intuitiva**: Menu interativo com botões para fácil navegação
- **🧠 IA Avançada**: Utiliza o modelo Deepseek para gerar interpretações contextualizadas e significativas

## 📋 Pré-requisitos

- Python 3.8 ou superior
- Token do Telegram Bot (obtido através do [@BotFather](https://t.me/botfather))
- [Ollama](https://ollama.ai/) instalado e rodando localmente

## 🛠️ Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/mystibot.git
cd mystibot
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o bot:
   - Copie o arquivo `config/settings.example.py` para `config/settings.py`:
   ```bash
   cp config/settings.example.py config/settings.py
   ```
   - Edite o arquivo `config/settings.py` com suas configurações:
     - `TELEGRAM_TOKEN`: Token do seu bot do Telegram
     - `LLM_API_URL`: URL da API do Ollama (padrão: http://localhost:11434/api/generate)
     - `MODELO`: Nome do modelo que você quer usar (ex: deepseek-coder:6.7b)

## 🐧 Ollama no Ubuntu com GPU (WSL ou nativo)

Para usar o MystiBot com IA local no Linux/Ubuntu, você precisa rodar o servidor Ollama com suporte à GPU (NVIDIA). Veja como configurar:

### 1. Instale o Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Verifique se você tem CUDA instalado

Certifique-se de que o driver NVIDIA está instalado e funcionando:

```bash
nvidia-smi
```

Se não funcionar, instale o driver e bibliotecas com:

```bash
sudo apt update
sudo apt install -y nvidia-driver-535 nvidia-cuda-toolkit
```

Reinicie após a instalação.

### 3. Ative o uso da GPU

Inicie o servidor Ollama com suporte à GPU com:

```bash
OLLAMA_USE_CUDA=1 ollama serve
```

Esse comando inicia o servidor local que o MystiBot usa para se comunicar com o modelo de linguagem.

### 4. Carregue o modelo Deepseek

Após o servidor estar rodando, em outro terminal:

```bash
ollama pull deepseek-r1:8b
```

> 💡 Modelos maiores como `deepseek-r1:14b` exigem mais memória. Use `deepseek-r1:8b` se tiver até 8 GB de VRAM.

### 5. Configure seu `settings.py`

No arquivo `config/settings.py`:

```python
LLM_API_URL = "http://localhost:11434/api/generate"
MODELO = "deepseek-r1:8b"
```

Pronto! Agora o bot usará o modelo Deepseek rodando localmente com aceleração por GPU.

## 🏗️ Estrutura do Projeto

```
mystibot/
├── config/
│   ├── settings.py      # Configurações do bot (não versionado)
│   ├── settings.example.py # Exemplo de configurações
│   ├── prompts.py       # Prompts para o LLM
│   └── messages.py      # Mensagens do sistema e do bot
├── constants/
│   └── tarot_cards.py   # Definição das cartas do tarot
├── services/
│   ├── tarot_service.py     # Serviço de leitura de tarot
│   └── horoscope_service.py # Serviço de horóscopo
├── .env                # Variáveis de ambiente (não versionado)
├── .gitignore
├── README.md
├── requirements.txt
└── bot.py             # Arquivo principal do bot
```

## 🚀 Como Executar

1. Ative o ambiente virtual (se ainda não estiver ativo):
```bash
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

2. Execute o bot:
```bash
python bot.py
```

## 💡 Uso

1. Inicie o bot no Telegram
2. Use o comando `/start` para ver o menu principal
3. Escolha entre:
   - 🔮 Tarot: Faça uma pergunta e receba uma leitura com 3 cartas
   - ✨ Horóscopo: Selecione seu signo para receber o horóscopo do dia
   - ℹ️ Sobre o Bot: Informações sobre o bot e suas funcionalidades

## 🔧 Configuração

### Prompts
Os prompts para o LLM estão configurados em `config/prompts.py`:
- `TAROT_PROMPT`: Formato da leitura de tarot
- `HOROSCOPE_PROMPT`: Formato do horóscopo diário

### Mensagens
As mensagens do sistema e do bot estão em `config/messages.py`:
- `ERROR_MESSAGES`: Mensagens de erro do sistema
- `BOT_MESSAGES`: Mensagens de interação com o usuário

## 🤝 Contribuindo

1. Faça um Fork do projeto
2. Crie uma Branch para sua Feature (`git checkout -b feature/AmazingFeature`)
3. Faça o Commit das suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Faça o Push para a Branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## ✨ Recursos Adicionais

- Processamento de respostas do LLM para remover conteúdo de pensamento (`<think>`)
- Formatação automática das respostas em Markdown
- Sistema de estados para gerenciar a interação com o usuário
- Tratamento de erros robusto
- Mensagens personalizadas para cada tipo de interação