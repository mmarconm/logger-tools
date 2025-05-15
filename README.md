
# Logger Tools

Um decorador reutilizável com rastreamento da função chamadora, baseado em `inspect`, com log configurável via arquivo `settings.py`.

## Uso

```python
from logger_tools import Logger, log_function_call

log = Logger()
log.inspect_function("Mensagem do log")

@log_function_call(level="info")
def minha_funcao():
    pass
```
