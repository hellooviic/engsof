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

Resposta:
Um commit deve representar uma alteração com um único objetivo.  
Juntar tudo que foi feito durante o dia mistura mudanças que podem não ter relação entre si.  
Isso dificulta entender posteriormente o histórico do projeto.  
Também dificulta desfazer apenas uma alteração que apresentou problema.  
Commits pequenos e bem definidos tornam o histórico mais claro, rastreável e seguro.

### Questão 4
Explique por que ocorre um conflito, o que significa cada um dos três delimitadores inseridos pelo Git e quais passos resolvem a situação.

Resposta:
Um conflito acontece quando dois ramos alteram a mesma parte de um mesmo arquivo e o Git não consegue decidir automaticamente qual versão deve permanecer.

Os delimitadores são:

`<<<<<<< HEAD` indica o conteúdo do ramo atual.

`=======` separa as duas versões em conflito.

`>>>>>>> nome-do-ramo` indica o conteúdo do outro ramo que está sendo integrado.

Para resolver, deve-se analisar as duas versões, escolher ou combinar o conteúdo correto, apagar os delimitadores, salvar o arquivo, executar os testes, adicionar o arquivo novamente com `git add` e concluir o commit.

### Questão 5
Liste cinco tipos de arquivo que não devem ser versionados e explique o risco específico de cada um.

**Resposta:**

1. Arquivos com senhas, tokens ou chaves de API: podem permitir acesso não autorizado a sistemas e serviços.
2. Arquivos de ambiente, como `.env`: podem conter credenciais e configurações privadas.
3. Ambientes virtuais, como `.venv`: ocupam espaço e podem ser recriados a partir das dependências do projeto.
4. Arquivos de cache, como `__pycache__`: são gerados automaticamente e não representam código-fonte.
5. Arquivos com dados pessoais ou grandes conjuntos de dados: podem causar problemas de privacidade, segurança e tamanho excessivo do repositório.

Esses arquivos devem ser excluídos do versionamento através do `.gitignore`, quando aplicável.

### Questão 6
Uma credencial foi commitada por engano e removida no commit seguinte. Explique por que isso não é suficiente e o que deve ser feito.

**Resposta:**

Remover a credencial no commit seguinte não é suficiente porque ela continua registrada nos commits anteriores do histórico do Git. Qualquer pessoa que tenha acesso ao histórico pode recuperar esse valor.

Por isso, a credencial deve ser considerada comprometida e deve ser revogada ou substituída imediatamente. Também é necessário impedir que o arquivo com a credencial volte a ser versionado, por exemplo utilizando o `.gitignore`.

### Questão 7
Explique por que gestão de configuração é pré-requisito para testes automatizados e para qualquer forma de auditoria.


**Resposta:**

A gestão de configuração permite saber exatamente qual versão do código, dos dados, das dependências e das configurações foi utilizada em determinado momento.

Isso é necessário para que um teste automatizado possa ser reproduzido nas mesmas condições e produza resultados confiáveis.

Também é essencial para auditorias, pois permite identificar o que foi alterado, quando a alteração aconteceu e qual versão foi utilizada.

Sem um histórico íntegro e reproduzível, não é possível testar, investigar ou justificar uma decisão técnica com segurança.

---

## Aula 05 - GitHub: colaboração e revisão de código

### Questão 1
Descreva os cinco passos do fluxo de contribuição, do clone ao merge, indicando o artefato produzido em cada um.

**Resposta:**

Partindo de um clone local do repositório, o fluxo possui cinco etapas:

1. Escolher uma issue e criar um ramo para o trabalho. O artefato produzido é uma nova branch associada à tarefa.
2. Realizar o trabalho e criar commits pequenos e descritivos. Os artefatos produzidos são os commits.
3. Enviar o ramo ao GitHub e abrir um pull request. Os artefatos são a branch remota e o PR.
4. Receber a revisão, realizar os ajustes necessários e integrar a alteração. São produzidos comentários de revisão, aprovações e a integração na main.
5. Apagar o ramo após a integração e fechar a issue. O resultado final é a main atualizada, a branch de trabalho removida e a issue concluída.

### Questão 2
Um pull request tem título "alterações", nenhuma descrição e 38 arquivos alterados. Liste o que falta para torná-lo revisável e explique o risco de aprová-lo assim.

**Resposta:**

Esse pull request precisa de um título que explique claramente a alteração, uma descrição informando por que ela foi feita e quais decisões foram tomadas, vínculo com a issue correspondente, uma seção explicando como testar e um tamanho menor.

Os 38 arquivos alterados indicam que o PR provavelmente deveria ser dividido em contribuições menores.

Aprovar um PR assim dificulta uma revisão cuidadosa e pode fazer com que erros sejam integrados à branch principal. Além disso, uma aprovação sem revisão adequada cria uma falsa sensação de segurança.

### Questão 3
Escreva um comentário de revisão adequado para um trecho que ignora o caso de lista vazia, indicando se é bloqueante ou sugestão.

**Resposta:**

**Bloqueante:** O que acontece se a lista estiver vazia? Nesse caso, o código pode tentar acessar um elemento que não existe e gerar um erro. Seria necessário tratar esse cenário e adicionar um teste para uma lista vazia antes da integração.

### Questão 4
Justifique cada uma das quatro regras de proteção da branch principal em termos do problema que ela evita.

**Resposta:**

1. Proibir push direto na main: evita que uma alteração entre na branch principal sem passar por revisão.
2. Exigir pelo menos uma aprovação: garante que outra pessoa tenha analisado a alteração antes da integração.
3. Exigir que as verificações automáticas passem: evita integrar código que falha nos testes ou verificações configuradas.
4. Exigir que todas as conversas sejam resolvidas: impede que dúvidas ou problemas apontados durante a revisão sejam ignorados antes do merge.

### Questão 5
Traduza para comandos gh as seguintes ações: criar issue, abrir PR, trazer PR do colega para a máquina e aprovar a revisão.

### Questão 6
Compare GitHub Flow, Git Flow e trunk-based indicando em que contexto cada um é adequado.

### Questão 7
Explique por que revisão por pares é considerada uma prática de qualidade e não um mecanismo de controle sobre as pessoas.