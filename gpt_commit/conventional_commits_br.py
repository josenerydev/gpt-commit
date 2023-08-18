CONVENTIONAL_COMMITS_BR = """
### Estrutura do Commit:
```
<tipo>[escopo opcional]: <descrição>

[corpo opcional]

[rodapé(s) opcional]
```

### Elementos:

1. **fix:** corrige um bug. Corresponde a [`PATCH`](http://semver.org/#summary) em Semantic Versioning.
   - Exemplo: `fix: corrige erro de carregamento em dispositivos móveis`

2. **feat:** introduz um novo recurso. Corresponde a [`MINOR`](http://semver.org/#summary) em Semantic Versioning.
   - Exemplo: `feat: adiciona botão de compartilhamento nas postagens`

3. **BREAKING CHANGE:** muda algo que quebra a compatibilidade. Corresponde a [`MAJOR`](http://semver.org/#summary) em Semantic Versioning. Pode ser parte de qualquer tipo de commit.
   - Exemplo no rodapé: 
     ```
     feat: altera a API para suportar multiusuários
     BREAKING CHANGE: a estrutura do objeto de usuário foi modificada
     ```
   - Exemplo com `!`: `feat!: remove suporte à versão antiga da API`

4. Outros _tipos_ além de `fix:` e `feat:` são permitidos, como `docs:`, `style:`, `refactor:`, entre outros.
   - Exemplo: `docs: atualiza comentários no código para melhor clareza`

5. _rodapés_ seguem um formato semelhante ao [formato de trailer do git](https://git-scm.com/docs/git-interpret-trailers).

6. Um escopo pode ser fornecido ao tipo de commit para dar mais informações contextuais.
   - Exemplo: `feat(autenticação): adiciona verificação em duas etapas`

### Exemplos:

- **Com descrição e rodapé de breaking change:**
  ```
  feat: permite que o objeto de configuração estenda outras configurações
  BREAKING CHANGE: a chave `extends` no arquivo de configuração agora é usada para estender outros arquivos de configuração
  ```

- **Com `!` para chamar a atenção para uma breaking change:**
  ```
  feat!: envia um email para o cliente quando um produto é enviado
  ```

- **Sem corpo:**
  ```
  docs: corrige ortografia no CHANGELOG
  ```

- **Com escopo:**
  ```
  feat(lang): adiciona suporte ao idioma português
  ```

- **Com corpo de várias linhas e vários rodapés:**
  ```
  fix: impede corrida de solicitações
  Adiciona um ID de solicitação e uma referência para a última solicitação. Descarta
  respostas que não sejam da última solicitação.
  Reviewed-by: Z
  Refs: #123
  ```

### Especificações:

- Commits DEVEM ser prefixados com um tipo.
- Um escopo PODE ser fornecido após o tipo.
- Uma descrição DEVE seguir imediatamente após o tipo/escopo.
- Um corpo mais longo PODE ser fornecido após a descrição curta.
- Um ou mais rodapés PODEM ser fornecidos após o corpo.
- BREAKING CHANGE DEVE ser em letras maiúsculas.

Essas são as convenções principais e exemplos do "Conventional Commits". Essa convenção é útil para manter uma história de commit clara e legível, facilitando a geração automática de registros de mudanças e a determinação de versões semânticas.
"""