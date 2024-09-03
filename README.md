# Atividade Prática Supervisionada: Sistema de Busca

## Descrição

Este projeto é uma atividade supervisionada que envolve a criação de um sistema de recomendação utilizando uma API. O sistema permite realizar consultas e retorna até dez documentos relevantes para a pesquisa, com base em um banco de dados escolhido pelo grupo.

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
docker build -t news-rec .
```

Esse comando cria uma imagem Docker com o nome `news-rec`, baseada no Dockerfile presente no diretório do projeto.

### Execução do Container

Após a construção da imagem, você pode executar a aplicação em um contêiner Docker utilizando o comando:

```bash
docker run -d -p 1515:1515 news-rec
```

Esse comando inicia o contêiner em segundo plano (`-d`), mapeando a porta `1515` do host para a porta `1515` do contêiner. Isso permite acessar a API em seu ambiente local.

### Acessando a API

Com o contêiner em execução, você pode acessar a API através do endereço:

```bash
http://localhost:1515
```
