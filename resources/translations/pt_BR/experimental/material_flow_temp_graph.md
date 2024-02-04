Gráficos de temperatura de fluxo
====
Para imprimir mais rápido, é melhor imprimir a uma temperatura um pouco mais alta.Isso torna o termoplástico mais fluido, o que permite fluir mais rapidamente pela abertura do bico.Quando [temperatura automática](material_flow_dependent_temperature.md) é ativada, esse parâmetro especifica para cada fluxo em que temperatura o material deve ser impresso.A taxa de fluxo é calculada para cada camada para determinar uma temperatura para essa camada.

A vazão é calculada em milímetros cúbicos por segundo, a média de uma camada inteira.A temperatura é expressa em graus Celsius.O valor deste parâmetro deve ser uma lista de coordenadas separadas por vírgulas.Cada coordenada está no formulário `[<dé Flow>, <mupremuy>]`.

O objetivo desta configuração é obter melhor qualidade de impressão, reduzindo a extrusão e a subestusão, se houver grandes mudanças de fluxo na impressão.Um caso frequente é o da fronteira entre a pele e o recheio.Como a pele é normalmente impressa muito mais lentamente do que o material de enchimento, as camadas onde há muito material de enchimento devem ser impressas a uma temperatura ligeiramente mais alta, para que o material possa ser extrudado corretamente durante a impressão deste enchimento de material.

Para muitas impressoras, o regulador PID que regula as temperaturas no bico da impressora tende a reagir excessivamente quando há muitas mudanças de temperatura em pouco tempo.A temperatura de impressão pode, portanto, ser muito imprecisa quando essa configuração é usada.

** Esta configuração não está atualmente visível na interface cura e não pode ser ativada. **