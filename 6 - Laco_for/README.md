# Laço For

Pasta de exercícios em **Python** focados no uso do **laço `for`**.

Os programas demonstram contagens, tabuadas, somas, contagem regressiva, números pares/ímpares e cálculo de médias.

---

## Conceitos abordados

| Conceito | Descrição |
|----------|-----------|
| `for i in range(n)` | Repete de 0 até n-1 |
| `range(início, fim)` | Define início e fim (fim não incluso) |
| `range(início, fim, passo)` | Define o incremento (ex.: 2 para pares) |
| Contagem regressiva | `range(n, 0, -1)` |
| Acumuladores | `soma += valor` |
| Contadores | `pares += 1` |
| `time.sleep()` | Pausa entre iterações |

---

## Exercícios

| Arquivo | Descrição |
|---------|-----------|
| `01_for_exemplo.py` | Imprime os números de 1 a 10. |
| `02_tabuada.py` | Tabuada de adição, subtração, multiplicação e divisão. |
| `03_for_exemplo.py` | Pede o nome 5 vezes usando `for`. |
| `04_for_de_tras_para_frente.py` | Contagem de 10 até 1. |
| `05_for_numeros_pares.py` | Números pares de 100 a 120. |
| `06_for_numeros_impares.py` | Números ímpares de 1 a 20. |
| `07_for_contagem_regressiva.py` | Contagem regressiva com pausa de 1 segundo. |
| `08_for_soma.py` | Soma de 5 números digitados pelo usuário. |
| `09_for_pares.py` | Mostra quais números entre 1 e 10 são pares. |
| `10_for_exemplo_pares.py` | Conta quantos pares e ímpares em 5 números. |
| `11_notas.py` | Calcula a média de 4 notas. |
| `12_numeros_impares_1.py` | Números ímpares de 1 a 20 (versão com `if`). |
| `13_numeros_impares.py` | Números ímpares de 1 a 20. |
| `14_numeros_pares.py` | Números pares de 100 a 120 (com `if`). |
| `15_numeros_pares.py` | Números de 100 a 120 (sem filtro). |
| `16_pares_impares.py` | Conta pares e ímpares em 5 números. |
| `18_valor_variavel.py` | Demonstra o acúmulo de valores em uma variável. |
| `19_regressiva.py` | Contagem regressiva com `time.sleep`. |
| `20_aprovado_reprovado.py` | Média de 3 notas e classificação (Aprovado / Recuperação / Reprovado). |

---

## Como executar

```bash
python "01_for_exemplo.py"
python "02_tabuada.py"
# etc.
```

> **Observação:** A maioria dos arquivos usa `os.system('cls')` (limpa tela no Windows).  
> No Linux/macOS use `os.system('clear')` se preferir.

---

## Ordem sugerida de estudo

1. **Básico do `for` e `range`**  
   `01_for_exemplo.py` → `04_for_de_tras_para_frente.py` → `03_for_exemplo.py`

2. **Passo e filtros**  
   `05_for_numeros_pares.py` → `06_for_numeros_impares.py` → `09_for_pares.py`

3. **Acumuladores e contadores**  
   `08_for_soma.py` → `18_valor_variavel.py` → `10_for_exemplo_pares.py` → `16_pares_impares.py`

4. **Aplicações práticas**  
   `11_notas.py` → `20_aprovado_reprovado.py` → `02_tabuada.py` → `07_for_contagem_regressiva.py`

---

## Observações

- O `range()` **não inclui** o valor final.
- Use `passo = 2` para percorrer apenas pares ou ímpares.
- `soma += numero` é o padrão para acumular valores.
- Alguns arquivos têm pequenas variações/repetições (ex.: versões de pares e ímpares) para reforçar o aprendizado.
