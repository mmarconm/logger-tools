# Odoo Logtracer 🔧  
Um decorador reutilizável com rastreamento de chamadas, ideal para debugging e logging em projetos Python e módulos Odoo.

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

---

## ✨ Descrição

Odoo Logtracer é uma biblioteca simples e reutilizável de logging em Python, com foco em integração para projetos Odoo:

- Decoradores que rastreiam funções chamadoras usando `inspect`
- Log personalizável via `log_setup.py`
- Estrutura modular e fácil de integrar em qualquer projeto Python ou Odoo
- Suporte a logger singleton

---

## 📦 Instalação

### Via Git

```bash
pip install git+https://github.com/mmarconm/odoo-logtracer.git
```

### Instalação local (modo desenvolvimento)

```bash
git clone https://github.com/mmarconm/odoo-logtracer.git
cd odoo-logtracer
pip install -e .
```

---

## ⚙️ Configuração

Edite o arquivo `odoo_logtracer/log_setup.py` com as opções desejadas:

```python
LOG_FILE_PATH = "/var/log/odoo/odoo_default.log"   # Caminho do arquivo de log
LOG_LEVEL = "INFO"                                 # Níveis: DEBUG, INFO, WARNING, ERROR, CRITICAL
LOGGER_NAME = "odoo_logger"                        # Nome interno do logger
```

---

## 🚀 Como usar em projetos Odoo

### Exemplo básico em Python

```python
from odoo_logtracer import Logger, log_function_call

log = Logger()
log.inspect_function("Mensagem do log")  # Loga nome da função chamadora

@log_function_call(level="info")
def minha_funcao():
    print("Função executada")
```

### Exemplo de uso em um módulo Odoo

```python
from odoo import models, fields, api
from odoo_logtracer import Logger, log_function_call

log = Logger()

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @log_function_call(level="info")
    def action_confirm(self):
        log.inspect_function("Confirmação de pedido chamada!")
        return super().action_confirm()
```

O log será salvo no caminho definido em `log_setup.py` e incluirá rastreamento de chamadas e contexto da função.

---

## 🧪 Testando build local

Após instalar o módulo `build`:

```bash
pip install build
python -m build
```

Arquivos gerados ficarão em `dist/`.

---
## 👨‍💻 Autor

**Marcelo Marcon**  
[github.com/mmarconm](https://github.com/mmarconm)

---

## 📄 Licença

Este projeto é licenciado sob a [Licença MIT](LICENSE).