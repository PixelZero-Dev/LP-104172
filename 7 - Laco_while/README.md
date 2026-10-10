# Laço While

Pasta de exercícios em **Python** focados no uso do **laço `while`**.

Os programas trabalham com validação de dados, menus interativos, sistemas de login e cálculos com acumuladores.

---

## Conceitos abordados

| Conceito | Exemplos |
|----------|----------|
| `while True` + `break` | Validação de notas, login, números positivos |
| Validação de intervalo | Notas (0–10), números (1–10) |
| Menu interativo | `match/case` ou `if/elif` |
| Acumuladores | `soma`, contadores, médias |
| Limite de tentativas | Login com 3 tentativas |
| Tratamento de entrada | `try/except`, `float` com vírgula |

---

## Exercícios

| Arquivo | Descrição |
|---------|-----------|
| `2 - aluno.py` | Lê a nota de um aluno e valida se está entre 0 e 10. |
| `3 - nota.py` | Lê 2 notas (com validação), calcula e exibe a média. |
| `4 - login_exemplo.py` | Sistema de login simples (usuário + senha fixos). |
| `5 - login.py` | Tentativa de cadastro e login de senha (versão incompleta). |
| `6 - login_while.py` | Login com limite de **3 tentativas**. |
| `7 - nota_while.py` | Média de 2 notas com validação e limpeza de tela. |
| `8 - familia.py` | Menu para cadastrar famílias e calcular média salarial, média de filhos, maior e menor salário. |
| `9 - loop_positivo.py` | Lê números positivos até digitar 0. Conta pares/ímpares e calcula médias. |
| `10 - notas.py` | Menu interativo (S/N) para inserir notas e calcular a média aritmética. |
| `11 - prefeitura_backup.py` | Versão antiga/bugada da pesquisa da prefeitura. |
| `12 - prefeitura.py` | Pesquisa da prefeitura (versão corrigida): cadastra pessoas e calcula média salarial, maior/menor idade e quantidade de mulheres com salário ≥ R$ 5.000. |
| `13 - valores_positivos.py` | Lê valores positivos e calcula a média aritmética (sai com número negativo). |
| `nota_loops.py` | Lê notas continuamente até o usuário responder `N`. |

---

## Como executar

```bash
python "2 - aluno.py"
python "12 - prefeitura.py"
# etc.
```

> **Observação:** A maioria dos arquivos usa `os.system('cls')` (limpa tela no Windows).  
> No Linux/macOS use `os.system('clear')` se preferir.

---

## Ordem sugerida de estudo

1. **Validação básica**  
   `2 - aluno.py` → `3 - nota.py` → `7 - nota_while.py`

2. **Acumuladores e saída controlada**  
   `13 - valores_positivos.py` → `nota_loops.py` → `9 - loop_positivo.py`

3. **Login e tentativas**  
   `4 - login_exemplo.py` → `6 - login_while.py`

4. **Menus interativos**  
   `10 - notas.py` → `8 - familia.py` → `12 - prefeitura.py`

---

## Observações

- Os programas foram escritos com fins **didáticos**.
- Existe uma versão antiga com bugs (`11 - prefeitura_backup.py`) e a versão corrigida (`12 - prefeitura.py`).
- Prefira sempre a versão mais recente quando houver duas versões do mesmo exercício.
- O `while True` + `break` é o padrão mais usado para validação de entrada.
