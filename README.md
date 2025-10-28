# Morfologia Matemática (erosão / dilatação / abertura / fechamento)

Este repositório contém implementações manuais simples de operações de morfologia matemática (erosão e dilatação) em imagens binárias, além de um pequeno programa (`main.py`) para testar e visualizar as operações.

## Estrutura do repositório

- `main.py` - Script principal. Lê uma imagem (`paisagem2.jpg` por padrão), converte para binário (Otsu) e oferece um menu para aplicar: erosão, dilatação, abertura ou fechamento. Salva e mostra o resultado.
- `erosao.py` - Implementação manual da operação de erosão sobre uma imagem binária (listas de listas Python).
- `dilatacao.py` - Implementação manual da operação de dilatação sobre uma imagem binária (listas de listas Python).
- `printer.py` - Funções para converter listas de volta em arrays NumPy, mostrar janelas com OpenCV e salvar imagens de saída.

> Observação: alguns arquivos podem conter pequenas redundâncias/linhas não utilizadas (ex.: tentativa de uso de `cv2.UMat` em `erosao.py`) — não impactam o resultado final quando executado com `main.py`.

## Pré-requisitos

- Python 3.8 ou superior
- pip

Dependências Python (principalmente para execução/visualização):

- opencv-python
- numpy

## Instalação (Windows PowerShell)

1. (opcional) criar e ativar um ambiente virtual:

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1
```

2. Instalar dependências:

```powershell
pip install --upgrade pip
pip install opencv-python numpy
```

## Como executar

Coloque a imagem que você quer processar na mesma pasta do projeto e dê a ela o nome `paisagem2.jpg` (ou modifique a variável `caminho` em `main.py`). Depois execute:

```powershell
python main.py
```

O programa fará:

1. Ler a imagem `paisagem2.jpg`.
2. Converter para escala de cinza.
3. Aplicar threshold automático (Otsu) para gerar a imagem binária.
4. Perguntar qual operação executar (digite o número):
   - 1 — Erosão
   - 2 — Dilatação
   - 3 — Abertura (erosão seguida de dilatação)
   - 4 — Fechamento (dilatação seguida de erosão)
   - 5 — Sair

As janelas do OpenCV irão exibir a imagem original, a binária e o resultado da operação escolhida. Pressione qualquer tecla com a janela ativa para continuar.

## Arquivos de saída

O resultado de cada operação é salvo com o padrão `imagem_<texto>.jpg`, onde `<texto>` é uma string passada ao `printer_all` (`'erodida'`, `'dilatada'`, `'aberta'`, `'fechada'` etc.). Por exemplo: `imagem_erodida.jpg`.

## Notas de implementação

- As funções `erosao_binaria` e `dilatacao_binaria` trabalham com uma imagem binária expressa como uma lista de listas Python (valores 0 e 255). O `main.py` converte a matriz NumPy binária em uma lista de listas antes de passar para as funções manuais.
- As implementações são simples e intencionais para fins didáticos — não são otimizadas para desempenho. Para uso em imagens grandes ou aplicações em produção, prefira as funções prontas do OpenCV (`cv2.erode`, `cv2.dilate`) que são aceleradas.

## Possíveis melhorias

- Corrigir mensagens de log inconsistentes em `printer.py` (a mensagem de impressão aponta sempre para fechamento).
- Remover código não utilizado em `erosao.py` (linhas com `cv2.UMat(...) if False else None`).
- Adicionar argumentos de linha de comando para especificar caminho da imagem, kernel, e número de iterações.

## Licença

Sinta-se à vontade para usar e adaptar este código para fins acadêmicos e de aprendizado. Nenhuma licença explícita foi adicionada — adicione uma se desejar compartilhar com restrições específicas.

---

Se quiser, eu posso:

- adicionar um `requirements.txt` com as dependências;
- ajustar `main.py` para aceitar argumentos via linha de comando;
- remover as linhas redundantes e corrigir a mensagem de saída em `printer.py`.

Diga qual dessas melhorias você quer que eu faça em seguida.