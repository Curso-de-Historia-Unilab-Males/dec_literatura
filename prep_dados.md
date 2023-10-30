# Preparação dos dados

Para importar os dados para o Omeka S, sugerimos que os mesmos sejam adaptados para uma estrutura baseada no [DCMI](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) (*DublinCore Metadata Initiative*). 

## Estrutura sugerida

| Nome do termo DCMI    | Etiqueta | Definição | Coluna atual | Comentário/Sugestão |
|-------------------    | -------- | --------- | ------------ | ------------------- |
| title                 | Título | O título do recurso. | TITULO | Manter título como está, apenas colocar entre aspas duplas `"` |
| alternative           | Título Alternativo | Um título alternativo para o recurso (caso exista). | | Avaliar se é necessário |
| creator               | Criador | O criador ou autor do recurso. | AUTOR(A) | Quando houver mais de uma autor, separar com `;` |
| contributor           | Contribuidor | Um contribuidor para o recurso. | ILUSTRADOR(A)| Sugestão de incluir ilustradores/as nessa coluna |
| subject               | Assunto | O assunto ou tópico do recurso. | | Sugestão de incluir assuntos como palavras-chave. Separar com `;` |
| abstract              | Resumo | O resumo ou sumário do recurso. | SINOPSE | Manter sinopse como está, apenas colocar entre aspas duplas `"` |
| description           | Descrição | Uma breve descrição do recurso. |  | Avaliar se é necessário |
| publisher             | Editora | O editor ou publicador do recurso. | EDITORA | Manter editora como está |
| date                  | Data | A data de criação ou publicação do recurso. | ANO DA EDIÇÃO | Colocar apenas ano |
| type                  | Tipo | O tipo ou gênero do recurso. | | Sugestão de incluir tipo de livro (se é físico ou digital) |
| identifier            | Identificador | Um identificador único para o recurso. | | Sugestão de incluir ISBN ou DOI |
| source                | Fonte | A fonte ou origem do recurso, se aplicável. | | Avaliar se é necessário |
| language              | Idioma | O idioma do recurso. | | Sugestão de inserir `pt-BR` |
| coverage              | Cobertura | A cobertura geográfica ou temporal do recurso. | | Avaliar se é necessário |
| educationLevel        | Nível de educação da audiência | O nível de educação do público-alvo do recurso. | | Sugestão de incluir aqui a classificação indicativa |
| extent                | Extensão | A extensão do recurso. | | Sugestão de incluir aqui o número de páginas |
| rights                | Direitos | As informações de direitos autorais ou licença do recurso. | | Avaliar se é necessário |
| bibliographicCitation | Citação Bibliográfica | Uma citação bibliográfica para o recurso. | | Sugestão de incluir aqui a referência bibliográfica completa do livro, colocar entre aspas duplas `"` |
| file[^file]           | Arquivo | O arquivo do recurso. | CAPA | Sugestão de colocar o link para a imagem de capa |

[^file]: Esse termo não é do DCMI, mas é importante para incluirmos a imagem da capa no Omeka S.

Exemplo de csv contento todos os campos DCMI:

```
title,alternative,creator,contributor,subject,abstract,description,publisher,date,format,identifier,source,language,coverage,educationLevel,extent,rights,bibliographicCitation,file
DIÁRIO DE PILAR NA ÁFRICA,,FLÁVIA LINS E SILVA,JOANA PENNA,África,"Na luta pela liberdade e contra a injustiça, Pilar e seus amigos vão parar do outro lado do Atlântico. Nessa aventura eles aprendem muito sobre a cultura africana.",,Pequeno Zahar,2022,impresso,978-65-8889-919-9,,pt-BR,,infantojuvenil,200p,,"LINS E SILVA, Flávia. Diário de Pilar na África. Rio de Janeiro: Pequeno Zahar, 2022.",https://cdl-static.s3-sa-east-1.amazonaws.com/covers/gg/9786588899199/diario-de-pilar-na-africa-nova-edicao.jpg
```

Acesse o exemplo de csv [aqui](/data/exemplo_dcmi/exemplo.csv).
