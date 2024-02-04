Diâmetro máximo suportado pela torre
====
Essa configuração é um limite para o diâmetro de um pedaço de saliência, permitindo escolher entre torres de suporte normais e torres de suporte.Se a peça for mais fina que esse limite, ela será suportada por uma [Torre de Suporte](support_use_towers.md).Se for mais largo que esse limite, será suportado por estruturas de suporte comuns.

![O suporte tem uma superfície pendente menor que o diâmetro mínimo](../images/support_use_towers.svg)

Se uma tira muito fina de saliência precisar ser suportada, o suporte normal será derrubado.Esse suporte é muito vasculhado para ser impresso corretamente.Em vez disso, uma torre mais sólida é gerada.

Ao aumentar esse parâmetro, as torres serão geradas com mais frequência.Isso aumenta a confiabilidade do suporte, mas também requer um pouco mais de material e tempo de impressão.