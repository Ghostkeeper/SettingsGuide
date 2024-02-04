Espiralizar o contorno externo
====
Espiralizar o contorno externo é uma dica.

Durante a camada de impressão por camada, o bico normalmente deve se mover de uma camada para outra.Esse movimento significa que o bico permanece quase imóvel durante uma fração de segundo, o que deixa uma costura na superfície chamada costura Z. Essa configuração se destina a impedir isso e muito mais.

Ao colocar o modelo em espiral, o modelo não terá preenchimento ou enchimento superior.Ele terá apenas uma parede e um fundo.É essencial que, se [suavizar os contornos em espiral](smooth_spiralized_contours.md) for ativado, a altura do bico aumentará gradualmente na espessura de uma camada.Dessa maneira, uma espiral é criada seguindo o esboço do modelo.Não haverá movimento de uma camada para outra, porque o bico já se moveu gradualmente para a próxima camada.

O modo espiral é comum em muitos fatores de fatia.Às vezes, também é chamado de "moda de vaso", porque é uma boa maneira de imprimir vasos.Aqui estão algumas outras propriedades:
* Imprime extremamente rapidamente.
* A superfície se torna muito lisa.Não há mais [couture](../solucionamento de problemas/costure.md) onde foi para a próxima camada se [endireitar os contornos em espiral](smooth_spiralized_contours.md) for ativado.
* Não será muito sólido.Se o modelo for muito grande, ele tende a [dividir](../solucionar problemas/layer_splitting.md) devido à delicadeza da parede.
* Embora a remoção da costura ajude a impressão à prova d'água, é difícil tornar a impressão à prova d'água se tiver apenas um contorno.Para isso, é aconselhável ter pelo menos 2 paredes.É então impossível transformar o contorno exterior em uma espiral.

** A espiral não funcionará bem com impressões com muitas superfícies horizontais.Ele não gerencia as saliências e não imprime as superfícies superiores, para que nada possa confiar em uma superfície horizontal.Também não funciona bem quando há várias zonas em uma camada. **