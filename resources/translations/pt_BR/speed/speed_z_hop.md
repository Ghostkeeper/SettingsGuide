Velocidade de deslocamento z
====
Este parâmetro configura a velocidade de movimento à qual os movimentos verticais são realizados em um z hop.Os movimentos horizontais de um z hop não são afetados, pois são configurados pela [velocidade de movimento](speed_travel.md).

![O movimento vertical é realizado na velocidade do z hop](../images/speed_z_hop.svg)

<!-Se Cura_version> = 4.2-> A velocidade do deslocamento z também é usada como uma velocidade de movimento entre as camadas.Na prática, essa velocidade importa muito pouco, já que o movimento de uma espessura de uma única camada é tão curta que quase sempre é limitada pela aceleração, e não pela velocidade máxima de movimento. <!-endif->>

Para a maioria das impressoras, o eixo Z é construído para ser robusto, mas lento.O aumento na velocidade do deslocamento Z possibilita testar os limites do movimento do eixo z, que pode tomar certas medidas para o motor do eixo z. Portanto, o bico pode estar em uma altura diferente após o z Z. Reduza essa velocidade reduz os riscos que isso acontece.

Por outro lado, uma velocidade de compensação Z mais alta fará com que o bico se afaste da superfície impressa mais rapidamente.Isso pode reduzir o tamanho das marcas.

Devido às baixas taxas de aceleração no eixo z, é raro que a velocidade de deslocamento Z desejada seja atingida, a menos que a altura do deslocamento z seja muito alta ou a velocidade muito baixa.