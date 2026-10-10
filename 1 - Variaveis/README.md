# Variáveis

Pasta de exercícios em **Python** focados em **declaração e uso de variáveis**.

Os programas mostram a diferença entre tipagem estática (com anotações) e tipagem dinâmica (padrão do Python).

---

## Conceitos abordados

| Conceito | Descrição |
|----------|-----------|
| Variável | Espaço na memória que guarda um valor |
| Atribuição | `nome = "Marta"` |
| Tipagem dinâmica | O tipo é definido automaticamente pelo valor |
| Anotações de tipo | `nome: str`, `idade: int`, `peso: float` (opcional) |
| Tipos básicos | `str` (texto), `int` (inteiro), `float` (decimal) |
| `print()` | Exibe o conteúdo da variável |

---

## Exercícios

| Arquivo | Descrição |
|---------|-----------|
| `1_tipos_dados_estaticos.py` | Declara variáveis com anotações de tipo (`str`, `int`, `float`) e depois atribui valores. |
| `2_tipos_dados_dinamicos.py` | Atribui valores diretamente (tipagem dinâmica — forma mais comum em Python). |

---

## Como executar

```bash
python "1_tipos_dados_estaticos.py"
python "2_tipos_dados_dinamicos.py"
```

---

## Ordem sugerida de estudo

1. `2_tipos_dados_dinamicos.py` → Forma natural do Python  
2. `1_tipos_dados_estaticos.py` → Como declarar o tipo explicitamente (anotações)

---

## Observações

- Em Python **não é obrigatório** declarar o tipo da variável.
- As anotações (`nome: str`) servem apenas como documentação e ajuda de IDEs — elas **não** forçam o tipo em tempo de execução.
- Python é uma linguagem de **tipagem dinâmica**: o tipo é definido no momento da atribuição.
- Boas práticas:
  - Use nomes claros (`idade` em vez de `i`)
  - Evite palavras reservadas (`print`, `input`, `for`, etc.)
