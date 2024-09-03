# Atividade Prática Supervisionada: Sistema de Busca

## Descrição

Este projeto faz parte de uma atividade supervisionada na disciplina de Processamento de Linguagem Natural do Insper. O objetivo é desenvolver um sistema de recomendação que funcione através de uma API.

## Contexto Geral

Esta API foi desenvolvida com o objetivo de fornecer recomendações de notícias relevantes com base em pesquisas específicas dos usuários. Utilizando como fonte o site brasileiro Poder360, conhecido por sua cobertura detalhada de assuntos políticos e econômicos, o sistema analisa o conteúdo de todas as notícias publicadas nos últimos 15 dias. A partir dessa análise, a API sugere as notícias mais relacionadas à consulta realizada, oferecendo uma ferramenta eficiente para manter os usuários informados sobre temas de interesse.

## Técnicas Utilizadas

A API utiliza a técnica de TF-IDF (Term Frequency-Inverse Document Frequency) para avaliar a relevância de segmentos de texto em relação a uma consulta específica. Esta abordagem permite identificar as partes mais pertinentes das notícias, atribuindo maior peso a termos que são frequentes na consulta, mas raros no restante do corpus de documentos. Dessa forma, a API consegue priorizar as notícias que contêm informações mais relevantes para o usuário, melhorando a precisão das recomendações.

Além do TF-IDF, o sistema também aplica técnicas de pré-processamento de texto, como a remoção de stop words, para garantir que a análise seja feita de forma eficiente e precisa. A combinação dessas técnicas permite que a API ofereça resultados robustos e bem direcionados, adaptados às necessidades específicas de cada consulta.

## Construção do Dataset

Para criar o dataset que alimenta nosso sistema de recomendação, realizamos um processo de scraping no site de notícias Poder360. Abaixo, descrevemos o racional e as etapas seguidas para a construção desse dataset.

### Coleta de Dados

O primeiro passo foi acessar o site Poder360 e coletar todas as notícias publicadas nos últimos 15 dias. Optamos por essa abordagem para garantir que o sistema de recomendação seja alimentado com informações atualizadas e relevantes, refletindo os eventos mais recentes cobertos pelo site.

### Extração de Informações

Para cada notícia coletada, extraímos as informações essenciais, como o título, subtítulo, data de publicação, autor, e o corpo do texto. Essa extração foi realizada de forma automatizada, garantindo que todas as notícias seguissem o mesmo formato e pudessem ser analisadas consistentemente pelo sistema.

### Armazenamento dos Dados

Após a extração, as informações de cada notícia foram armazenadas em arquivos JSON. A escolha pelo formato JSON se deu pela sua flexibilidade e facilidade de manipulação, permitindo que os dados fossem organizados de maneira estruturada e acessível.

### Consolidação

Para facilitar a análise posterior, todos os dados coletados foram consolidados em um único arquivo. Essa etapa foi crucial para garantir que todas as notícias estivessem disponíveis em um formato unificado, permitindo que o sistema de recomendação processasse as informações de maneira eficiente.

### Conversão para DataFrame e CSV

Finalmente, os dados foram carregados em um DataFrame, o que facilitou a manipulação e a análise estatística das notícias. O DataFrame foi, então, salvo em um arquivo CSV, um formato amplamente utilizado que permite uma fácil integração com outras ferramentas e sistemas.

## Deploy com Docker

Para simplificar a execução da API e garantir um ambiente de execução consistente, o projeto foi dockerizado. A seguir, explicamos como construir e executar a aplicação utilizando Docker.

### Construção da Imagem

Para construir uma imagem Docker da aplicação, utilize o seguinte comando:

```bash
docker build -t hudsonma-marcosvs3 .
```

Esse comando cria uma imagem Docker com o nome `hudsonma-marcosvs3`, baseada no Dockerfile presente no diretório do projeto.

### Execução do Container

Após a construção da imagem, você pode executar a aplicação em um contêiner Docker utilizando o comando:

```bash
docker run -d -p 1515:1515 hudsonma-marcosvs3
```

Esse comando inicia o contêiner em segundo plano (`-d`), mapeando a porta `1515` do host para a porta `1515` do contêiner. Isso permite acessar a API em seu ambiente local.

### Acessando a API

Com o contêiner em execução, você pode acessar a API através do endereço:

```bash
http://10.103.0.28:1515
```
Como Usar a API
Pontos Finais
A API possui os seguintes endpoints:

/query: Recebe uma consulta do usuário e retorna as notícias recomendadas com base na relevância calculada pelo sistema.
Exemplos de Consultas
Para ajudar a entender o funcionamento da API, você pode acompanhar o arquivo test_query.py, que contém exemplos de consultas à API. Abaixo estão três exemplos de testes realizados, cada um com uma consulta diferente:

1. Teste 1: Query = "Elon Musk briga com Alexandre de Moraes"
Este teste realiza uma consulta sobre um tema específico, envolvendo Elon Musk e Alexandre de Moraes. A API retorna 10 notícias que são consideradas relevantes para essa consulta, baseadas no conteúdo do banco de dados.

Como testar: Acesse o endereço http://10.103.0.28:1515/docs, clique no botão "Try it out" ao lado do endpoint /query, e insira o texto "Elon Musk briga com Alexandre de Moraes" no campo query. Em seguida, clique em "Execute" para visualizar as 10 notícias mais relevantes.
2. Teste 2: Query = "Treino Paralimpíadas"
Neste teste, a consulta é mais específica, focando em treinamentos para as Paralimpíadas. A API retorna 1 notícia relevante, o que demonstra a capacidade do sistema em identificar e filtrar conteúdos mesmo em consultas com resultados limitados.

Como testar: Acesse http://10.103.0.28:1515/docs, clique em "Try it out" no endpoint /query, e insira a consulta "Treino Paralimpíadas" no campo query. Clique em "Execute" para visualizar a notícia relevante.
3. Teste 3: Query = "crescimento verde"
Aqui, a consulta envolve o tema de "crescimento verde", um tópico amplamente discutido em contextos econômicos e ambientais. A API retorna novamente 10 notícias relevantes, mostrando sua capacidade de lidar com temas amplos e populares.

Como testar: Visite http://10.103.0.28:1515/docs, selecione "Try it out" ao lado do endpoint /query, insira "crescimento verde" no campo query, e clique em "Execute" para receber as 10 notícias relacionadas ao tema.
