# IS_Challenge2

## Desafio
 ![image](https://github.com/user-attachments/assets/25abf4bd-824d-4c04-8ec6-878828146def)

## Project RoadMap

### Estrutura do Projeto

1. Entrada de Dados
 - Dataset (CSV)
   * Arquivo CSV que contém os dados iniciais para conversão em XML.

2. Conversão para XML Base

  - Script em Python para converter o CSV para um formato XML inicial (XML Base).
     * Objetivo: Ler o CSV, processar os dados e criar um arquivo XML que será a base para os próximos passos.
     * Ferramentas: Python (pode usar bibliotecas como pandas para ler o CSV e xml.etree.ElementTree ou lxml para gerar o XML).

3. Validação do XML Base

  - Script em Python para validar o XML gerado usando um arquivo de esquema XML (XSD).
     * Objetivo: Garantir que o XML Base gerado atende às restrições e estrutura definidas no XSD.
     * Ferramentas: Python (pode usar bibliotecas como xmlschema para validar o XML com o XSD).

4. Criação de Sub-XML por Categorias

  - Script em Python para gerar arquivos XML específicos (Sub XML) com base em categorias dos dados.
     * Objetivo: Criar sub-arquivos XML a partir do XML Base, dividindo os dados conforme uma categoria específica (por exemplo, tipo ou localização).
     * Ferramentas: Python (continuando com xml.etree.ElementTree ou lxml para manipulação do XML).

5. Transformação com XSLT ou XQuery (Opção 1 e Opção 2)

  - Opção 1 (Básica, Ineficiente): Realizar todas as transformações necessárias usando apenas Python.
     * Objetivo: Criar e manipular os Sub XMLs sem utilizar XSLT/XQuery, mas isso pode resultar em maior esforço manual para futuras modificações.
     * Ferramentas: Python, se seguir por esta opção, para manipular o XML diretamente.

  - Opção 2 (Ideal, Mais Eficiente): Aplicar XSLT ou XQuery para transformar o XML conforme o layout e filtros necessários.
     * Objetivo: Utilizar scripts XSLT para transformar o XML conforme um layout específico ou usar XQuery para realizar consultas.
     * Ferramentas: Scripts XSLT e/ou XQuery para gerar o Sub XML transformado.

6. Exploração do XML usando XPath e XQuery

  - Script em Python para explorar e consultar o XML usando XPath e XQuery.
     * Objetivo: Realizar consultas e extrair informações específicas do XML transformado.
     * Ferramentas: Python (pode usar a biblioteca lxml para executar XPath e pyxquery ou outra biblioteca para XQuery, caso necessário).

## What is done

1. Entrada de Dados - **DONE**
2. Conversão para XML Base - **DONE**
3. Validação XML Base - **DONE**
4. Criação de Sub-XML por Categorias - **DONE**

**REST TODO**

