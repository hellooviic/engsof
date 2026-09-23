# Exercícios de Git e GitHub

## Aula 04 - Gestão de configuração: Git

### Questão 1
Explique as três áreas do Git e diga qual comando move um arquivo entre cada par delas.

Resposta:
As três áreas do Git são:

- Diretório de trabalho: onde os arquivos estão sendo editados.
- Área de preparo (staging): contém as alterações selecionadas para o próximo commit.
- Repositório (.git): guarda permanentemente o histórico dos commits.

O comando `git add arquivo` leva uma alteração do diretório de trabalho para a área de preparo.  
O comando `git commit` registra o conteúdo preparado no repositório.  
Para retirar um arquivo da área de preparo, pode-se usar `git restore --staged arquivo`, e `git restore arquivo` desfaz alterações feitas no diretório de trabalho.

### Questão 2
Reescreva as mensagens de commit a seguir de modo que sirvam a quem lê o histórico: "ajustes", "agora foi", "correções diversas".

Resposta:
As mensagens precisam explicar claramente o que foi alterado. Por exemplo:

- `ajustes` → `docs: ajusta descrição dos comandos Git no README`
- `agora foi` → `fix: corrige validação de entrada de dados`
- `correções diversas` → `fix: corrige tratamento de erros na leitura do arquivo`

O importante é que a mensagem permita entender a alteração sem precisar abrir o código.

### Questão 3
Um colega pergunta por que não pode simplesmente fazer um commit por dia com tudo o que mexeu. Responda em cinco linhas.

### Questão 4
Explique por que ocorre um conflito, o que significa cada um dos três delimitadores inseridos pelo Git e quais passos resolvem a situação.

### Questão 5
Liste cinco tipos de arquivo que não devem ser versionados e explique o risco específico de cada um.

### Questão 6
Uma credencial foi commitada por engano e removida no commit seguinte. Explique por que isso não é suficiente e o que deve ser feito.

### Questão 7
Explique por que gestão de configuração é pré-requisito para testes automatizados e para qualquer forma de auditoria.

---

## Aula 05 - GitHub: colaboração e revisão de código

### Questão 1
Descreva os cinco passos do fluxo de contribuição, do clone ao merge, indicando o artefato produzido em cada um.

### Questão 2
Um pull request tem título "alterações", nenhuma descrição e 38 arquivos alterados. Liste o que falta para torná-lo revisável e explique o risco de aprová-lo assim.

### Questão 3
Escreva um comentário de revisão adequado para um trecho que ignora o caso de lista vazia, indicando se é bloqueante ou sugestão.

### Questão 4
Justifique cada uma das quatro regras de proteção da branch principal em termos do problema que ela evita.

### Questão 5
Traduza para comandos gh as seguintes ações: criar issue, abrir PR, trazer PR do colega para a máquina e aprovar a revisão.

### Questão 6
Compare GitHub Flow, Git Flow e trunk-based indicando em que contexto cada um é adequado.

### Questão 7
Explique por que revisão por pares é considerada uma prática de qualidade e não um mecanismo de controle sobre as pessoas.