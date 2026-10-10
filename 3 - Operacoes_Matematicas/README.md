# Operações Matemáticas

Pasta de exercícios em **Python** focados em **operações matemáticas** básicas e cálculos simples.

Os programas trabalham com soma, subtração, divisão, desconto, antecessor/sucessor, média e comparação de valores.

---

## Conceitos abordados

| Conceito | Descrição |
|----------|-----------|
| Operadores aritméticos | `+`, `-`, `*`, `/` |
| Precedência | Uso de parênteses `()` para garantir a ordem correta |
| Desconto percentual | `valor * 0.10` (10%) |
| Antecessor / Sucessor | `numero - 1` e `numero + 1` |
| Funções `max()` e `min()` | Encontrar o maior e o menor valor |
| Divisão | Calcular quantos salários mínimos cabem no salário |

---

## Exercícios

| Arquivo | Descrição |
|---------|-----------|
| `01_media.py` | Calcula a média de duas notas (com nome e idade). |
| `02_desconto.py` | Aplica 10% de desconto sobre um valor digitado. |
| `03_antecessor_sucessor.py` | Mostra o antecessor e o sucessor de um número. |
| `04_salario.py` | Calcula quantos salários mínimos equivalem ao salário informado. |
| `05_maior_menor.py` | Compara dois números e tenta identificar o maior e o menor. |
| `06_maior_menor_tres_numeros.py` | Encontra o maior e o menor entre três números usando `max()` e `min()`. |

---

## Como executar

```bash
python "01_media.py"
python "02_desconto.py"
# etc.
```

> **Observação:** A maioria dos arquivos usa `os.system('cls')` (limpa tela no Windows).  
> No Linux/macOS use `os.system('clear')` se preferir.

---

## Ordem sugerida de estudo

1. **Operações básicas**  
   `03_antecessor_sucessor.py` → `02_desconto.py`

2. **Média e divisão**  
   `01_media.py` → `04_salario.py`

3. **Maior e menor**  
   `05_maior_menor.py` → `06_maior_menor_tres_numeros.py`

---

## Observações

- Em Python a divisão `/` sempre retorna `float`.
- Use parênteses para garantir a ordem correta dos cálculos (ex.: média).
- `max()` e `min()` são as formas mais simples de encontrar o maior e o menor valor.
- Alguns arquivos possuem pequenos erros de lógica (ótimos para praticar a correção).
