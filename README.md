# Logger Tools 🔧  
Um decorador reutilizável com rastreamento de chamadas, ideal para debugging e logging em projetos Python.

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## ✨ Descrição

Logger Tools é uma biblioteca simples e reutilizável de logging em Python com:

- Decoradores que rastreiam funções chamadoras usando `inspect`
- Log personalizável via `settings.py`
- Estrutura modular e fácil de integrar em qualquer projeto
- Suporte a logger singleton

---

## 📦 Instalação

### Via Git

```bash
pip install git+https://github.com/mmarconm/logger-tools.git
```

### Instalação local (modo desenvolvimento)

```bash
git clone https://github.com/mmarconm/logger-tools.git
cd logger-tools
pip install -e .
```

---

## ⚙️ Configuração

Crie ou edite um arquivo `settings.py` com as seguintes opções:

```python
LOG_FILE_PATH = "logs/app.log"   # Caminho do arquivo de log
LOG_LEVEL = "INFO"               # Níveis: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOGGER_NAME = "logger_tools"     # Nome interno do logger
```

---

## 🚀 Como usar

```python
from logger_tools import Logger, log_function_call

# Criando o logger
log = Logger()
log.inspect_function("Mensagem do log")  # Loga nome da função chamadora

# Usando o decorador para rastrear chamadas de função
@log_function_call(level="info")
def minha_funcao():
    print("Função executada")
```

---

## 🧪 Testando build local

Após instalar o módulo `build`:

```bash
pip install build
python -m build
```

Arquivos gerados ficarão em `dist/`.

---

## 📁 Estrutura do Projeto

```
logger-tools/
├── logger_tools/
│   ├── __init__.py
│   └── logger.py
├── pyproject.toml
├── settings.py         # (opcional, pode ser ignorado no .gitignore)
├── README.md
├── LICENSE
├── MANIFEST.in
```

---

## ✅ Features futuras (roadmap)

- [ ] Suporte a `loguru`
- [ ] Suporte a configuração via `.env`
- [ ] Integração com `colorlog` para terminal colorido
- [ ] Logging assíncrono opcional

---

## 👨‍💻 Autor

**Marcelo Marcon**  
[github.com/mmarconm](https://github.com/mmarconm)

---

## 📄 Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).