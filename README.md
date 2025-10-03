# 🎯 AI-Powered Marketing Slogan Generator

Uma aplicação Flask avançada que gera slogans publicitários contextualizados usando Inteligência Artificial, com integração a APIs de clima, dados em tempo real e sistema de publicação automatizada.

## 🚀 Funcionalidades

### 🧠 Geração Inteligente de Slogans
- **IA Multimodal**: Integração com OpenAI GPT-4 e Google Gemini
- **Contextualização Avançada**: Considera localização, clima, feriados e eventos
- **Múltiplas Marcas**: Sistema modular para diferentes brands (A, B, C)
- **Personalização**: Slogans adaptados por horário, dia da semana e público-alvo

### 🎨 Processamento de Mídia
- **Geração de Imagens**: Criação automática de assets visuais
- **Processamento de Vídeo**: Integração com OpenCV e MoviePy
- **Fontes Personalizadas**: Sistema de tipografia por marca
- **Templates Dinâmicos**: Layouts responsivos e customizáveis

### 🌐 Integração Externa
- **API de Clima**: Dados meteorológicos em tempo real
- **Sistema de Publicação**: Integração com plataforma de displays digitais
- **Dados Geográficos**: Base completa de estados, cidades e bairros
- **Calendário de Feriados**: Sistema de eventos e datas comemorativas

### 📊 Sistema de Avaliação
- **Feedback de Usuários**: Sistema de likes/dislikes
- **Histórico de Campanhas**: Armazenamento e análise de performance
- **Dashboard Interativo**: Interface para visualização de resultados

## 🏗️ Arquitetura

### Estrutura MVC Moderna
```
app/
├── controllers/          # Lógica de controle
│   ├── auth_controller.py
│   ├── slogan_controller.py
│   └── zkong_controller.py
├── models/              # Modelos de dados
│   └── user.py
├── services/            # Camada de serviços
│   ├── brands/          # Serviços específicos por marca
│   ├── utils/           # Utilitários de processamento
│   └── slogan_service.py
└── routes.py           # Roteamento centralizado
```

### Tecnologias Utilizadas
- **Backend**: Flask, Python 3.11+
- **IA**: OpenAI GPT-4, Google Gemini
- **Processamento**: OpenCV, MoviePy, Pillow
- **APIs**: Requests, JSON
- **Frontend**: HTML5, CSS3, JavaScript

## 🛠️ Instalação e Configuração

### Pré-requisitos
- Python 3.11+
- pip (gerenciador de pacotes Python)
- Chaves de API (OpenAI e Google Gemini)

### 1. Clone o Repositório
```bash
git clone https://github.com/seu-usuario/ai-slogan-generator.git
cd ai-slogan-generator
```

### 2. Crie o Ambiente Virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows
```

### 3. Instale as Dependências
```bash
pip install -r requirements.txt
```

### 4. Configure as Variáveis de Ambiente
Copie o arquivo `.env.example` para `.env` e configure suas chaves:

```bash
cp .env.example .env
```

Edite o arquivo `.env`:
```env
SECRET_KEY=sua-chave-secreta-aqui
BEARER_TOKEN=seu-bearer-token-aqui
OPENAI_API_KEY=sua-chave-openai-aqui
GEMINI_API_KEY=sua-chave-gemini-aqui
```

### 5. Execute a Aplicação
```bash
python app.py
```

A aplicação estará disponível em `http://localhost:5000`

## 🎮 Como Usar

### 1. Acesso ao Sistema
- **Brand A**: `brand_a` / `demo123`
- **Brand B**: `brand_b` / `demo123`
- **Brand C**: `brand_c` / `demo123`

### 2. Geração de Slogans
1. Faça login com uma das contas
2. Selecione localização (estado, cidade, bairro)
3. Configure parâmetros da campanha
4. Clique em "Gerar Slogans"
5. Avalie os resultados com like/dislike

### 3. Publicação
- Use a funcionalidade de publicação para enviar conteúdo para displays
- Monitore campanhas através do dashboard
- Analise performance através do sistema de avaliações

## 📁 Estrutura de Arquivos

```
├── app/                 # Aplicação principal
├── static/             # Assets estáticos
│   ├── brands/         # Assets por marca
│   ├── data/          # Dados estruturados
│   └── fonts/         # Fontes personalizadas
├── templates/         # Templates HTML
├── config.py         # Configurações
├── requirements.txt  # Dependências
└── README.md        # Documentação
```

## 🔧 Configuração Avançada

### Adicionando Nova Marca
1. Crie pasta em `static/brands/nova-marca/`
2. Adicione serviço em `app/services/brands/nova_marca.py`
3. Configure paths no `config.py`
4. Adicione rotas e templates correspondentes

### Customização de IA
- Modifique prompts nos arquivos de serviço das marcas
- Ajuste parâmetros de temperatura e criatividade
- Implemente novos modelos de IA conforme necessário

## 🚀 Deploy

### Produção
1. Configure `ENV=production` no `.env`
2. Use servidor WSGI (Gunicorn, uWSGI)
3. Configure proxy reverso (Nginx)
4. Implemente SSL/HTTPS

### Docker (Opcional)
```dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 🎯 Roadmap

- [ ] Integração com mais modelos de IA
- [ ] Sistema de A/B testing
- [ ] Analytics avançados
- [ ] API REST completa
- [ ] Interface mobile
- [ ] Suporte a mais idiomas

## 📞 Contato

**Desenvolvedor**: Seu Nome  
**Email**: seu.email@exemplo.com  
**LinkedIn**: [seu-perfil](https://linkedin.com/in/seu-perfil)  
**Portfolio**: [seu-portfolio.com](https://seu-portfolio.com)

---

⭐ **Se este projeto foi útil para você, considere dar uma estrela!**
