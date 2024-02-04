Velocidade máxima do ventilador
====

A velocidade na qual os ventiladores da cabeça de impressão são executados quando a camada é impressa no tempo mínimo.No horário mínimo da camada, você deseja esfriar a camada o mais rápido possível para reduzir o tempo necessário para resfriar a camada antes que a impressora imprima a próxima camada na parte superior.

![Qual velocidade do ventilador é usada onde](../images/cool_fan_speed.svg)

Se a impressão de uma camada estiver entre os parâmetros [limite de velocidade regular/máxima do ventilador
](cool_min_layer_time_fan_speed_max.md) e [duração mínima de uma camada](cool_min_layer_time.md), a velocidade do ventilador será interpolada entre [velocidade normal do ventilador](cool_fan_speed_min.md) e [maximum fanAx].Quando o tempo mínimo da camada for atingido, a velocidade máxima do ventilador também será alcançada.Dessa forma, a impressão será resfriada ao máximo para resfriá -la o mais rápido possível antes que a próxima camada seja impressa.