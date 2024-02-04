Superfície máxima dos orifícios
====
Dado que [faça a saliência imprimível](conical_overhang_enabled.md) remove qualquer tipo de saliência, todas as pontes serão reduzidas automaticamente, fechando a saliência abaixo.No entanto, se a saliência estiver fechada por todos os lados, ela continuará sendo reduzida até que a saliência fechada seja completamente preenchida.De fato, todos os orifícios orientados para baixo serão completamente preenchidos, mesmo que a saliência que deve ser removida seja apenas um pequeno ponto no topo.

Para evitar esse efeito, esse parâmetro permite que a saliência permaneça aberta se estiver fechada por todos os lados e menor que uma determinada superfície.Isso se aplica apenas a buracos.As saliências regulares do lado de fora do modelo são sempre estendidas para manter um ângulo razoavelmente imprimível.

![Um pequeno ponto no topo pode permanecer com vista, para que este buraco não seja preenchido](../../../articles/images/conical_overhang_hole_size.png)

É certamente ajustar esse parâmetro para várias dezenas de milímetros quadrados para a maioria dos modelos.Se for ajustado muito baixo, o modelo será alterado mais, para suportar saliências que são realmente muito pequenas para exigir qualquer meio.Por outro lado, se estiver liquidado muito alto, haverá áreas significativas de saliência que poderiam ser difíceis de preencher.

Se houver grandes áreas de saliência devido a este parâmetro, é melhor começar [Ative os parâmetros da ponte](Bridge_Settings_enabled.md) antes de tentar modificar o modelo para remover a saliência.