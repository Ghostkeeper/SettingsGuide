Relatório de classificação
====
Essa função permite modificar o método usado pela sua impressora para ajustar a largura da linha: em vez de modificar o fluxo do material através do bico, a impressora modifica a velocidade para a qual o bico se move.

As impressoras FFF são notoriamente incapazes de modificar a velocidade na qual o material sai do bico.Se a impressora alterar a velocidade da extrusora, é necessária uma fração de segundo antes que isso realmente se traduz em uma mudança de fluxo.Naquela época, dependendo da velocidade de impressão, o bico pode já ter excedido vários milímetros, o ponto em que o fluxo deveria ter sido ajustado.É ainda pior se a sua impressora tiver a extrusão longe da cabeça de impressão com um tubo de Bowden entre os dois.

Em vez de modificar a velocidade de potência, a impressora também pode alterar a velocidade de movimento da cabeça de impressão.A cabeça de impressão pode acelerar muito mais rápido, o que permite controlar melhor a largura da linha.Se a cabeça de impressão acelerar enquanto o fluxo permanecer o mesmo, a mesma quantidade de material será esticada em um comprimento mais longo, o que reduz a largura da linha.Se a cabeça de impressão diminuir, a mesma quantidade de material será agrupada em um espaço menor, o que aumenta a largura da linha.

Este parâmetro é uma proporção.Ele pode ajustar o fluxo (0 %) ou a velocidade de impressão (100 %) ou uma combinação dos dois.O relatório pode até exceder 100 %, o que significa que o fluxo é reduzido para produzir linhas mais grossas, mas que a velocidade é ainda menor para compensar.

Aumentar essa proporção para 100% significa que ele usa velocidade em vez de fluxo para modificar a largura da linha, que tem os seguintes efeitos na impressão:
* A largura da linha é provavelmente mais precisa, o que melhora a precisão dimensional da impressão.
* O fluxo será mantido igual, o que torna a impressão mais confiável, especialmente com materiais exóticos.
* Em alguns lugares, a cabeça de impressão se move mais rápido, o que pode causar vibrações.

Esse ajuste se aplica apenas a variações na largura das linhas causadas pela adaptação de linhas à largura de paredes finas e ângulos agudos.As variações no fluxo devido a parâmetros como diferentes larguras de linha para enchimento em comparação com as paredes não serão compensadas, nem as funções como ponte ou suavização.As impressoras que implementam a função de avanço linear ou funções de remuneração semelhantes devem continuar a usá -las, mesmo que esse parâmetro esteja definido em mais de 100 %, pois as alterações na taxa de fluxo sempre podem ocorrer devido a esses parâmetros.