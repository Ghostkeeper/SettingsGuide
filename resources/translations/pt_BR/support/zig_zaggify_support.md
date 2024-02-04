Conecte as linhas de suporte
====
Com alguns modelos de suporte, o suporte pode se tornar muito instável quando são necessárias tiras de suporte finas.Esse ajuste resultará nas extremidades das linhas de suporte entre elas.Isso lhes dá mais estabilidade.Isso também permite que o suporte imprima com um fluxo mais contínuo.Menos viagens serão necessárias.

![Linhas de suporte desconectadas](../../../articles/images/zig_zaggify_support_disabled.png)

![Linhas de suporte conectadas](../../../articles/images/zig_zaggify_support_enabled.png)

Quando uma linha de suporte é desenhada, em vez de ir para a próxima linha, uma linha será desenhada ao longo da borda da área de suporte para a próxima linha.Isso permite que toda a área de suporte seja convertida em uma única linha ou em muito poucas linhas.A conversão em uma única linha nem sempre é possível.O ponto de partida dessa linha é arbitrário, de modo que, com muita frequência, haverá linhas suspensas no ar porque, em uma camada, duas linhas podem ser conectadas a um ponto final, enquanto na próxima camada, elas estão conectadas ao outro lado .Isso torna o suporte um pouco menor, mas sempre estável e evita interrupções de fluxo.O comportamento desse parâmetro é o mesmo que o de [conectar as linhas de enchimento](../preenchimento/zig_zaggify_infill.md).

A conexão das linhas de suporte tem algumas vantagens, mas também algumas desvantagens:
* O suporte será mais estável, com menos probabilidade de alternar durante a impressão.
* O fluxo será mantido mais constante, o que permitirá imprimir o suporte em velocidade mais alta, sem problemas com o fluxo.Isso é particularmente importante para suportes difíceis de extrudar adequadamente.
* Se forem feitas as retiradas durante o suporte, haverá muito menos saques durante a impressão do suporte, o que impede a moagem do material.
* É preciso mais material para imprimir o suporte.
* Geralmente, é mais tempo para imprimir o suporte, porque os movimentos de movimento são normalmente mais rápidos que a impressão das linhas de suporte.

O padrão de suporte em zigue -zague está sempre conectado (de acordo com uma técnica ligeiramente diferente).Essa configuração não está disponível para o padrão em zigue -zague.