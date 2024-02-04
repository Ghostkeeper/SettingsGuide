Tolerância ao corte
====
Graças à tolerância ao corte, você pode ajustar como tratar a imprecisão da subdivisão de um ponto em um número finito de fraldas.Ele permite que você escolha se as camadas devem se aproximar da superfície, permanecer delimitadas pela superfície ou incluir completamente a superfície.

Meio
----
! [Meio](../imagens/slicing_tolerance_middle.svg)

Usando o meio, as camadas permanecerão o mais próximo possível da superfície original.Isso significa que as camadas às vezes excedem a superfície original e às vezes afundam na superfície original.No geral, o volume das camadas corresponderá muito ao volume da malha original.

Para obter tolerância média, o Cura calculará uma seção transversal no meio da espessura de cada camada.Tudo está dentro da seção transversal fará parte da camada.

Inclusão
----
! [Inclus](../imagens/slicing_tolerance_inclusive.svg)

Quando você usa inclusivo, as camadas contêm * pelo menos * todo o volume original.Quando a superfície é inclinada, as camadas serão ligeiramente salientes.O volume total de camadas quase sempre será maior que o volume da malha original.

Para obter tolerância inclusiva, o Cura calculará as seções transversais na parte superior e inferior da altura de cada camada.Todas as superfícies encontradas em uma ou outra * dessas seções transversais serão consideradas como parte dessa camada.Os pequenos detalhes que estão entre as duas seções transversais sempre serão ignorados, sendo inferiores à altura de uma camada.

Exclusivo
----
! [Exclusif](../imagens/slicing_tolerance_exclusive.svg)

No caso de uso exclusivo, as camadas estarão contidas no volume original.Quando a superfície é inclinada, as camadas serão um pouco menores que o volume original.O volume total de camadas quase sempre será menor que o volume da malha original.

Para obter tolerância exclusiva, o Cura calculará as seções transversais na parte superior e inferior da altura de cada camada.Somente as superfícies localizadas dentro dessas* seções transversais serão consideradas como parte dessa camada.

Usar
----
Este parâmetro carrega o nome de seu uso planejado, e não seu efeito funcional.Se você tiver várias peças que devem deslizar umas sobre as outras, a forma teórica de camadas poderá impedir fisicamente um ajuste exato.Nesse caso, você pode definir esse parâmetro exclusivo para garantir que as camadas permaneçam dentro dos limites do volume original.Com exceção dos efeitos de deformação semelhante à esquerda e outros efeitos de deformação, isso garantirá que as peças se encaixem e possam deslizar umas sobre as outras.

Na realidade, sempre existem outros efeitos que impedem isso.Na prática, esse ajuste pode ser usado para obter uma tolerância um pouco mais ou menos grande entre duas áreas inclinadas, como pode ser visto nas imagens acima.