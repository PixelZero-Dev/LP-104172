# Switch Case (match / case)

Pasta de exercícios em **Python** focados no uso do **`match/case`** (equivalente ao `switch/case` de outras linguagens).

Disponível a partir do **Python 3.10**.

---

## Conceitos abordados

| Conceito | Descrição |
|----------|-----------|
| `match valor:` | Inicia a estrutura de seleção |
| `case 'opção':` | Define um caso específico |
| `case _:` | Caso padrão (default) — quando nenhuma opção combina |
| Múltiplos valores | `case 'sabádo' \| 'domingo':` |
| Comparação exata | Funciona com strings, números e outros tipos |

---

## Exercícios

| Arquivo | Descrição |
|---------|-----------|
| `01_semana.py` | Recebe um número (1–7) e mostra o dia da semana correspondente. |
| `02_dia.py` | Recebe o nome do dia e identifica se é dia útil ou final de semana. |
| `03_operacao_basica.py` | Calculadora simples com os operadores `+`, `-`, `*` e `/`. |
| `04_cardapio.py` | Cardápio de restaurante: escolhe o prato pelo código e mostra o valor. |
| `05_mes.py` | Recebe o número do mês e mostra o nome do mês + ano. |
| `06_mercadinho_senai.py` | Sistema de pagamento (à vista com desconto ou à prazo com parcelas). |

---

## Como executar

```bash
python "01_semana.py"
python "06_mercadinho_senai.py"
# etc.
```

> **Requisito:** Python **3.10 ou superior** (o `match/case` não existe em versões anteriores).  
> A maioria dos arquivos usa `os.system('cls')` (limpa tela no Windows).

---

## Ordem sugerida de estudo

1. **Básico**  
   `01_semana.py` → `05_mes.py`

2. **Com strings e múltiplos valores**  
   `02_dia.py`

3. **Operações e menus**  
   `03_operacao_basica.py` → `04_cardapio.py` → `06_mercadinho_senai.py`

---

## Observações

- O `case _:` funciona como o `default` do `switch` em outras linguagens.
- Você pode combinar valores com `|` (ex.: `case 'sábado' | 'domingo':`).
- Diferente do `if/elif`, o `match` compara o valor completo de uma vez.
- Alguns exercícios ainda têm pequenos ajustes possíveis (ex.: nomes de pratos no cardápio).
