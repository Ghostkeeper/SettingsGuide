Linha de enchimento
====
As linhas de enchimento geralmente são orientadas em um ângulo de 45 graus o máximo possível.Nesse ângulo, os motores X e Y trabalham juntos para obter uma aceleração máxima da cabeça de impressão, ao usar uma impressora com o mecanismo de pórtico cartesiano comum.

Essa configuração permite ajustar este ângulo.Você pode especializá -lo para criar maior força para o seu modelo específico ou obter maior aceleração para o seu sistema específico de pórtico (como para as impressoras delta).

![Preenchimento de linhas com ângulos padrão de 45 e 135 graus](../../../articles/images/infill_pattern_lines.png)

![Linhas de enchimento com ângulos personalizados de 0 e 30 graus](../../../articles/images/infill_angles_0_30.png)

O valor deste parâmetro deve ser uma lista de ângulos separados por vírgulas e cercados por ganchos.Um ângulo de 0 grau fornecerá uma linha paralela ao eixo y. A lista de ângulos será alternada nas camadas.
* A impressão final será a mais forte nas direções das linhas de enchimento.Se você precisar da impressão de uma força específica em uma direção horizontal, é útil orientar as linhas de enchimento nessa direção.
* Deixe a configuração uma lista vazia para usar o valor padrão.
* O valor padrão depende do modelo de enchimento:
  * Para padrões de preenchimento cruzado e 3D, o valor padrão é [22].Isso torna possível guiar o maior número possível de linhas próximas às diagonais.
  * Para modelos de enchimento de linha e ziguezague, o valor padrão é [45.135].Isso alterna a camada da camada por camada entre as duas diagonais.
  * Todos os outros motivos usam um valor padrão de [45].Isso torna possível guiar o maior número possível de linhas próximas às diagonais.