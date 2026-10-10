# Vetores (Listas)

Pasta de exercícios em **Python** focados no uso de **vetores / listas** (`list`).

Os programas demonstram como armazenar vários valores em uma única estrutura, percorrê-los e realizar cálculos.

---

## Conceitos abordados

| Conceito | Descrição |
|----------|-----------|
| Criação de lista | `vetor = []` |
| Inserção de elementos | `vetor.append(valor)` |
| Acesso por índice | `vetor[0]`, `vetor[i]` |
| Percorrer com `for` | `for i in range(len(vetor))` |
| Funções úteis | `sum()`, `len()` |

---

## Exercícios

| Arquivo | Descrição |
|---------|-----------|
| `1 - exemplo.py` | Lê 3 notas, armazena em uma lista e calcula a média. |
| `2 - exemplo_2.py` | Compara o uso de **variável simples** versus **vetor** (lista). |
| `3 - nome.py` | Lê 3 nomes, armazena em uma lista e depois os exibe. |

---

## Como executar

```bash
python "1 - exemplo.py"
python "2 - exemplo_2.py"
python "3 - nome.py"
```

> **Observação:** Os arquivos usam `os.system('cls')` (limpa tela no Windows).  
> No Linux/macOS troque por `os.system('clear')` se desejar.

---

## Ordem sugerida de estudo

1. `2 - exemplo_2.py` → Entender a diferença entre variável e vetor  
2. `3 - nome.py` → Praticar inserção e exibição de textos  
3. `1 - exemplo.py` → Combinar lista + cálculo de média  

---

## Observações

- Em Python, o que chamamos de “vetor” na programação estruturada é implementado com a estrutura `list`.
- Os índices começam em **0**.
- `append()` adiciona o elemento no **final** da lista.
