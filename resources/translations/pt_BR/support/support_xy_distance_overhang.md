Distância X/Y Supports mínimos
====
Se a distância z do suporte for preferida na distância x/y, a distância horizontal entre o suporte e o modelo pode se tornar menor que o parâmetro [Distância X/Y de Suporte](Support_Xy_Distance.md) para satisfazer [Suporte Z Distância](support_z_distance.md) necessário.

Este parâmetro define uma distância mínima x/y que deve ser respeitada, independentemente da distância Z. Essa distância mínima x/y é novamente prioritária em comparação com a distância z.

![A distância mínima x/y é levada em consideração se a distância z significa que a distância x/y se tornaria muito pequena](../images/support_z_overrides_xy.svg)

Ao aumentar esse parâmetro, reduzimos o risco que apoia o modelo para o lado, deixando uma cicatriz onde não é necessária.Isso também facilita a retirada do apoio.Lembre -se, no entanto, que essa opção é eficaz apenas para saliência em uma altura média, onde a saliência normalmente deve ser suportada e, portanto, deve tocar no suporte para este local.Ao aumentar esse ajuste, a saliência é mais SAGS, o que reduz sua qualidade de superfície.