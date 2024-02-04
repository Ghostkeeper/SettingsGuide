Padrão acima/abaixo
====
Este parâmetro permite escolher como as superfícies superior e inferior são preenchidas com material.Vários padrões de impressão diferentes estão disponíveis, mas os padrões aqui são mais limitados do que para o preenchimento.Somente os padrões que criam camadas completas estão disponíveis.

Linhe
----
! [Lignes](../../../artigos/imagens/top_bottom_pattern_lines.png)

O diagrama básico traça linhas retas na superfície.Essas linhas são orientadas por padrão, para que sejam bem suportadas pelo preenchimento e suporte.A direção da linha alterna entre as fraldas.
* Fornece uma boa qualidade da superfície.
* Muito rígido nas direções em que as linhas são rastreadas.
* Adere fortemente às paredes, criando partes relativamente sólidas.

Concêntrico
----
! [Concentric](../../../Artigos/Images/Top_bottom_pattern_concentric.png)

O motivo concêntrico continua a desenhar contornos para dentro do modelo.
* Também forte em todas as direções.
* Impede a criação de bolsos de ar e espaço.É mais fácil criar objetos à prova d'água com este modelo.
* Alta qualidade de saliência, porque as linhas tendem a se sobrepor muito bem.
* Se a peça for circular, isso pode criar um ponto desagradável no centro onde os contornos convergem.
* A qualidade da superfície está longe de ser ideal.

Ziguezague
----
! [Zigzag](../../../Artigos/Images/Top_bottom_pattern_zigzag.png)

O padrão em zigue -zague é muito semelhante ao motivo da linha, mas, em vez de terminar as linhas nas paredes, continuará extinto em direção à seguinte linha de pele.
* Fornece alta qualidade superficial.
* Muito rígido nas direções em que as linhas são rastreadas.
* Mantenha a taxa de extrusão mais constante, o que melhora a consistência da superfície para materiais mais difíceis.
* Não grude as duas paredes como o desenho das linhas.O efeito da [porcentagem de sobreposição da camada externa](skin_overlap.md) é reduzido.Isso torna a sala mais baixa e reduz a qualidade dos transbordamentos.


