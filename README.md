# Análise de emoções em tweets de resposta a posts do ex-presidente do Brasil

<p align="justify">
Neste repositório estão armazenados os códigos e recursos empregados na pesquisa de TCC conduzida pela aluna Fernanda Malheiros Assi. O estudo consistiu na aplicação do modelo goEmotions adaptado para o Português, para identificar as emoções presentes nas respostas a posts do ex-presidente do Brasil, Jair Bolsonaro. A Figura abaixo ilustra o pipeline geral adotado no trabalho. A investigação foi segmentada em três módulos principais: extração dos <em>tweets</em>, pré-processamento dos dados e inferência de emoções dos <em>tweets</em> pelo GoEmotions para Português. Adicionalmente, foram conduzidas análises exploratórias dos dados resultantes da aplicação do GoEmotions, bem como uma análise linguística dos erros do modelo para as três emoções mais proeminentes no córpus: Raiva, Curiosidade e Admiração.

<br>
<br>

<p align="center">
  <img src="https://github.com/LALIC-UFSCar/TCC_Fernanda_Malheiros/assets/31036627/c0313fde-521c-4da6-8107-954e5b29fe89)" width="700">
</p>

<br>

## Estrutura do Repositório

- [**annotation**](https://github.com/LALIC-UFSCar/TCC_Fernanda_Malheiros/tree/main/annotation): Resultado da anotação manual de 100 instâncias de cada classe para as emoções mais presentes no córpus.
- [**data_collect**](https://github.com/LALIC-UFSCar/TCC_Fernanda_Malheiros/tree/main/data_collect): Scripts desenvolvidos para coletar os dados do Elasticsearch e salvá-los em uma pasta do Google Drive.
- [**goEmotions**](https://github.com/LALIC-UFSCar/TCC_Fernanda_Malheiros/tree/main/goEmotions): Códigos de inferência do goEmotions no córpus utilizado e análise exploratória realizada.
- [**preprocessing**](https://github.com/LALIC-UFSCar/TCC_Fernanda_Malheiros/tree/main/preprocessing): Códigos utilizados para pre-processar os textos do Twitter em duas fases: antes e após passar pelo goEmotions.

<br>

## Datasets

Devido ao tamanho, os datasets utilizados no projeto não estão hospedados diretamente neste repositório. Você pode acessá-los nos links abaixo:

- [**all_replies.csv**](https://drive.google.com/file/d/10orWJfOPN-EJ0Wbu-OawOebWGQIUiBea/view?usp=sharing): Todas as respostas, sem nenhum processo de pre-processamento.
- [**all_replies_clean.csv**](https://drive.google.com/file/d/1RxXLzVQHUqQBRV2bQk26pFh8UayYlmHA/view?usp=sharing): Todas as respostas após a primeira etapa do pre-processamento.
- [**all_replies_goEmotions.csv**](https://drive.google.com/file/d/1KpYLp4s1gqzj6mi7-VzV1Tf8izgr16uI/view?usp=sharing): Os dados após passar pelo goEmotions.
- [**all_replies_goEmotions_clean.csv**](https://drive.google.com/file/d/1haI3tfX2qkJb7v7aAQPKq0kvMEq6ckTt/view?usp=sharing): Os dados após a segunda etapa de pré-processamento.

</p>
