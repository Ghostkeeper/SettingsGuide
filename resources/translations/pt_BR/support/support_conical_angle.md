Ângulo de suportes cônicos
====
Esse ajuste determina o ângulo da inclinação para o qual o suporte cônico é impresso.

![Um ângulo de 30 graus](../../../articles/images/support_conical_enabled.png)

![Um ângulo de 10 graus](../../../articles/images/support_conical_angle_10.png)

![Um ângulo de -10 graus, o que significa que a base é mais ampla](../../../articles/images/support_conical_angle_neg10.png)

O ângulo de suporte cônico é o compromisso mais importante entre a estabilidade do suporte e a quantidade de suporte gerada.

O uso de um grande angular tornará o suporte muito fino em grande parte de sua altura.Isso economiza muito material e tempo de impressão.Quando é preciso muito material de suporte, isso economiza muito tempo e material, porque até metade do suporte é deixado de lado.No entanto, à medida que o suporte se torna muito fino na parte inferior, também pode se tornar menos estável, o que aumenta o risco de falha da impressão.Você pode aumentar a [largura mínima](support_conical_min_width.md) para evitar isso.

O uso de um ângulo negativo tornará o suporte mais amplo, na forma de um vulcão.Se a sua impressão tiver pequenos elementos de altura que devem ser suportados, eles normalmente produzirão [Tours] muito altos (support_use_towers.md), que tenderão a cair durante a impressão.Com um ângulo negativo, essas estruturas de suporte alto e fino serão ampliadas na parte inferior.Isso lhes dá alguma estabilidade adicional.No entanto, a impressão desse suporte levará mais tempo porque requer mais material.Um ângulo de aproximadamente -5 ° é normalmente suficiente para fornecer as estruturas de suporte mais altas e mais finas suficientes.Se o seu material tende a inchar muito durante a viagem, um ângulo negativo maior será necessário porque a estrutura será mais extensa devido às manchas do suporte.