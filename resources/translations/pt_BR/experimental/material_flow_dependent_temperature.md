Temperatura automática
====
Para imprimir mais rápido, é melhor imprimir a uma temperatura um pouco mais alta.Isso torna o termoplástico mais fluido, o que permite fluir mais rapidamente pela abertura do bico.Esse ajuste ajusta automaticamente a temperatura em função do fluxo médio do material para fora do bico.

Para descobrir até que ponto a temperatura deve ser ajustada, o [gráfico de temperatura de fluxo](material_flow_temp_graph.md) é referenciado.A vazão é calculada em milímetros cúbicos por segundo.Se colocarmos isso em relação à temperatura do fluxo, obtemos uma certa temperatura.Esta temperatura será usada como temperatura de impressão.Quando essa configuração é ativada, o ajuste comum [temperatura da impressão](../material/material_print_temperature.md) não será mais usado em favor da temperatura calculada a partir da taxa de fluxo.

O objetivo desse ajuste é obter melhor qualidade de impressão, reduzindo a extrusão e a subestusão, se houver grandes mudanças de fluxo na impressão.Um caso frequente é o da fronteira entre a pele e o recheio.Como a pele é normalmente impressa muito mais lentamente do que o material de enchimento, as camadas onde há muito material de enchimento devem ser impressas a uma temperatura ligeiramente mais alta, para que o material possa ser extrudado corretamente durante a impressão deste enchimento de material.

Para muitas impressoras, o regulador PID que regula as temperaturas no bico da impressora tende a reagir excessivamente quando há muitas mudanças de temperatura em pouco tempo.A temperatura de impressão pode, portanto, ser muito imprecisa quando essa configuração é usada.

** Esta configuração não está atualmente visível na interface cura e não pode ser ativada. **