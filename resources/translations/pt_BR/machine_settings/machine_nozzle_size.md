Diâmetro do bico
====
Esse ajuste indica o diâmetro do alargamento do bico através do qual o material flui.

![Dimensões da cabeça de impressão](../images/head_dimensions.svg)

Essa é uma dimensão importante na qual outros parâmetros podem ser baseados por padrão.Mais importante, a [largura da linha](../Resolução/Line_width.md) é normalmente ajustada de acordo com o tamanho do bico.Alguns perfis de impressora também limitam a altura da camada, dependendo do tamanho do bico, porque o tamanho do bico é o fator mais importante para a velocidade de extrusão do material.

<!-Se Cura_version <5.0: O tamanho do bico também é usado diretamente, para obter um detalhe: ao encher [pequenos espaços](../shell/preench_perimeter_gaps.md), as linhas mais distantes do que dois tamanhos de bicos não são mescladas .-->

Não ajuste o tamanho do bico, a menos que você realmente modifique o bico físico.Algumas fatias (incluindo Cura 15.04 e anterior) usam o termo "tamanho do bico" para designar a largura das linhas de impressão.O Cura usa o parâmetro [largura da linha](../Resolução/line_width.md) para isso.

*Como é uma configuração da máquina, esse parâmetro normalmente não é visível na lista de parâmetros.Se a sua impressora tiver perfis específicos para bicos disponíveis, você poderá selecioná -los no menu de configuração da impressora na parte superior da tela.Caso contrário, você pode ajustar o diâmetro dos bicos na caixa de diálogo Configurações da impressora, que está na lista de impressoras adicionadas na caixa de diálogo Preference.*