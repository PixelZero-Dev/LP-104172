# If / Else (Estruturas Condicionais)

Pasta de exercícios em **Python** focados no uso de **`if`**, **`elif`** e **`else`**.

Os programas trabalham com decisões simples e compostas: maioridade, notas, IMC, voto, aposentadoria, etc.

---

## Conceitos abordados

| Conceito | Descrição |
|----------|-----------|
| `if` | Executa um bloco se a condição for verdadeira |
| `else` | Executa quando a condição do `if` é falsa |
| `elif` | Testa uma nova condição (senão se) |
| Operadores relacionais | `>`, `<`, `>=`, `<=`, `==`, `!=` |
| Operadores lógicos | `and`, `or` |
| Condições compostas | Combinar mais de uma verificação |

---

## Exercícios

| Arquivo | Descrição |
|---------|-----------|
| `01_estrutura_condicional_simples.py` | Exemplo básico: compara duas variáveis fixas. |
| `02_condicional_simples.py` | Verifica se a idade é maior ou igual a 18 (maioridade). |
| `03_condicional_composta.py` | Maioridade com `if/else` (maior ou menor de idade). |
| `04_maior_menor.py` | Verifica se o número digitado é menor ou maior que 10. |
| `05_condicionais.py` | Classifica o número: igual, maior ou menor que 10 (`if/elif/else`). |
| `06_alistamento.py` | Verifica se deve se alistar (idade ≥ 18 e sexo masculino). |
| `07_aposentadoria.py` | Verifica se o trabalhador pode requerer aposentadoria. |
| `08_nota_aluno.py` | Calcula a média de 3 notas e informa se o aluno está aprovado ou reprovado. |
| `09_produto.py` | Calcula soma, média, produto, maior e menor de dois números. |
| `10_soma.py` | Similar ao anterior (versão com pequenas diferenças). |
| `11_voto.py` | Classifica o tipo de voto conforme a idade (obrigatório, opcional, etc.). |
| `12_macas.py` | Calcula o valor total da compra de maçãs (preço muda a partir de 12 unidades). |
| `13_nota_aluno_conceitos.py` | Média de 2 notas com conceitos (A, B, C, D, E) e situação (aprovado/reprovado). |
| `14_imc.py` | Calcula o IMC e classifica o resultado (abaixo do peso, ideal, obesidade, etc.). |

---

## Como executar

```bash
python "02_condicional_simples.py"
python "14_imc.py"
# etc.
```

> **Observação:** A maioria dos arquivos usa `os.system('cls')` (limpa tela no Windows).  
> No Linux/macOS use `os.system('clear')` se preferir.

---

## Ordem sugerida de estudo

1. **Condicional simples**  
   `01_estrutura_condicional_simples.py` → `02_condicional_simples.py` → `04_maior_menor.py`

2. **If / Else e Elif**  
   `03_condicional_composta.py` → `05_condicionais.py` → `11_voto.py`

3. **Condições compostas (and/or)**  
   `06_alistamento.py` → `07_aposentadoria.py`

4. **Aplicações práticas**  
   `08_nota_aluno.py` → `12_macas.py` → `13_nota_aluno_conceitos.py` → `14_imc.py` → `09_produto.py`

---

## Observações

- `if` sozinho = decisão simples.
- `if + else` = decisão composta (duas possibilidades).
- `if + elif + else` = múltiplas possibilidades.
- Alguns arquivos possuem pequenos bugs de aprendizado (ex.: cálculo de média ou comparação de maior/menor) — ótimos para praticar a correção.
- O operador `and` exige que **as duas** condições sejam verdadeiras.
