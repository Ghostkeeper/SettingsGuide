Modificador de velocidade de resfriamento de extrusão
====
Se a função [temperatura automática](../experimental/material_flow_dependent_temperature.md) for ativada, a temperatura da impressão será ajustada de acordo com a quantidade de material extrudado.

Quando o material é aquecido dentro da sala do bico, o calor é evacuado do bico.A extrusão mais rápida do material tende a remover mais calor do bico.Se a sonda de temperatura não estiver exatamente no final do bico, o bico terá uma temperatura ligeiramente mais baixa durante a extrusão do material do que quando interrompida, mesmo com um bom regulador PID.

Esse ajuste descreve a quantidade de calor perdido no bico durante a impressão.O calor adicional perdido por extrusão será então compensado, aumentando a temperatura de impressão desejada do código g.O valor do ajuste depende do design do bico, da capacidade térmica do material impresso e da velocidade de extrusão.