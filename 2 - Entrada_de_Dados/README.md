# Entradas de Dados

Pasta de exercícios em **Python** focados na **entrada de dados** pelo usuário (`input`).

Os programas demonstram como ler textos, números inteiros e números reais digitados no terminal.

---

## Conceitos abordados

| Conceito | Descrição |
|----------|-----------|
| `input()` | Lê o que o usuário digita (sempre retorna `str`) |
| `int()` | Converte o texto digitado em número inteiro |
| `float()` | Converte o texto digitado em número real (decimal) |
| Mensagens claras | Orientar o usuário sobre o que digitar |
| Exibição dos dados | Usar `print()` para mostrar o que foi lido |

---

## Exercícios

| Arquivo | Descrição |
|---------|-----------|
| `1_solicitando_dados.py` | Solicita nome, sobrenome, idade, peso e altura e depois exibe todos os dados. |

---

## Como executar

```bash
python "1_solicitando_dados.py"
```

> **Observação:** O arquivo usa `os.system("cls")` (limpa tela no Windows).  
> No Linux/macOS use `os.system('clear')` se preferir.

---

## Ordem sugerida de estudo

1. `1_solicitando_dados.py` — leia o código e observe:
   - Como o `input()` funciona
   - A diferença entre `int()` e `float()`
   - Como os dados são armazenados e depois impressos

---

## Observações

- Tudo que o `input()` lê é **texto** (`str`).
- Para fazer contas, é obrigatório converter com `int()` ou `float()`.
- Se o usuário digitar algo inválido (ex.: letra no lugar de número), o programa gera erro — isso será tratado em exercícios futuros com `try/except`.
