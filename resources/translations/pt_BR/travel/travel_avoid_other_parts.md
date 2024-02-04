Evite as peças impressas durante a viagem
====
Ao ativar esse parâmetro, a cabeça de impressão tentará evitar acertar outros objetos ao viajar no volume de construção.Em vez disso, ela fará um pequeno desvio.Se um desvio for possível e não afetar nenhum outro objeto, nenhuma retração será acionada, a menos que o comprimento da jornada exceda o parâmetro [distância máxima de desvio sem retração](retraction_combing_max_distance.md).

![Quando este parâmetro é desativado, os movimentos de movimento podem atravessar outras partes](../../../articles/images/travel_avoid_other_parts_disabled.png)

![Quando esta opção é ativada, a viagem evita outras peças](../../../articles/images/travel_avoid_other_parts_enabled.png)

Além de evitar outras peças, a viagem também tentará ficar perto das paredes o mais rápido possível.Isso significa que, quando sai ou entra em uma sala através de uma parede, ele sai ou entra perpendicular às paredes.

Essa configuração tende a melhorar a qualidade da superfície de impressão, porque o bico não atravessa as paredes com tanta frequência.A passagem pelas paredes deixa uma cicatriz na parede, que deve ser evitada.

No entanto, esse ajuste aumenta, pois haverá mais movimento sem retração e as viagens serão mais longas.Com materiais que escorrem muito, pode ser aconselhável desativar outras partes.

O tempo de impressão pode ser ligeiramente aumentado porque o deslocamento é mais longo, mas isso geralmente é compensado, reduzindo o número de saques que isso causa.