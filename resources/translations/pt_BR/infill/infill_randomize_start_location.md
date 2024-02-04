Randomizar o início -up
====
Se esse parâmetro for ativado, a posição em que a impressora começará a imprimir o preenchimento em uma camada será aleatória.

O início da pista de enchimento é geralmente um pouco menor que o restante do recheio.Isso ocorre quando o enchimento é impresso mais rápido, com linhas mais espessas ou uma altura maior da camada.O fluxo do material deve acelerar repentinamente, e isso não ocorre instantaneamente, para que haja uma subestimação por um curto período de tempo.Se isso acontecer no mesmo local em cada camada, enfraquece a estrutura de enchimento.O local onde isso acontece será o link mais baixo e o material de enchimento que o envolverá será submetido a mais restrições.Se a impressão estiver sujeita a uma força, é neste local que mais corre o risco de quebrar.

Normalmente, o recheio começa com a linha mais próxima da posição em que o bico estava no momento do enchimento, a fim de reduzir o tempo de viagem.Se essa configuração for ativada, o local inicial será bastante aleatório.Isso permite que você espalhe os pontos fracos.Não haverá mais um único elo fraco na corrente, e o recheio será, portanto, mais forte no final.

No entanto, isso aumenta levemente o tempo de viagem e leva a um aumento de escorreamento dentro do modelo, uma vez que a distância até o ponto de partida do enchimento não é mais reduzida.

** Embora o local inicial seja distribuído aleatoriamente, ele permanece determinístico.Repita o mesmo cálculo duas vezes deve levar aos mesmos locais iniciais. **