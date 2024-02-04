Preenchimento de espaguete
====
Se esse parâmetro for ativado, o Cura extrudará todo o preenchimento de várias camadas ao mesmo tempo em uma camada superior.Isso constitui uma forma extrema de [espessura da camada de enchimento](../preenchimento/preenchimento_sparse_thickness.md), mas sem o objetivo de manter a rigidez do recheio.Tem uma certa funcionalidade para lidar com quantidades extremas de extrusão.

Essa característica não é funcional para materiais comuns.Você normalmente deseja a resistência dos padrões de preenchimento comum ou não levará em consideração o preenchimento.No entanto, existem dois casos de uso.

Caso de uso
----
Com materiais flexíveis, essa técnica pode produzir texturas muito macias.O preenchimento de espaguete tende a produzir anéis mal colocados que não aderem bem um ao outro.Esses anéis também são compactos em todas as direções.Para obter esse efeito, a densidade de enchimento não deve ser muito fraca, caso contrário, todo o espaguete será encontrado na parte inferior da impressão.É aconselhável usar uma [densidade de fluxo](espaguete_flow.md) entre 30 e 60 %, dependendo da largura da linha e da altura da camada.O resultado será um recheio que também será rígido em todas as direções e bastante flexível.

A outra aplicação do recheio de espaguete é a moldagem.Se você possui uma impressora que inclua uma ferramenta para fluir em locais específicos, essa função pode ser usada para preencher seu modelo de maneira bastante uniforme com depósitos de materiais controlados.Se você usar essa função, o [Spaghetti Mode Flow](Spaghetti_flow.md) provavelmente deve estar em torno de 100 %, dependendo da taxa de contração/dilatação do material que flui.

Ajustando outros parâmetros para o preenchimento de espaguete
----
Essas duas solicitações exigem um processamento muito especial da sua solicitação de preenchimento.Aqui estão alguns parâmetros que você provavelmente deseja adaptar às suas necessidades:
* A [velocidade de enchimento do enchimento](../speed/speed_infill.md) deve ser massivamente reduzida.Se o bico for extrudar o material de preenchimento de 10 camadas ao mesmo tempo, você precisará reduzir a velocidade de impressão em pelo menos um fator 8.
* Ajuste sua [espessura da camada de enchimento](../prelochill_sparse_thickness.md) para que seja igual à altura da camada.
* Aumente ligeiramente sua [temperatura de impressão](../material/MATTER_PRINT_TEMPERATURA.MD) (para a extrusora que imprimirá o preenchimento).Isso permite que o material passe corretamente para fora do bico e permite uma extrusão mais rápida.
* Defina o [alinhamento do z -z](../shell/z_seam_type.md) aleatoriamente para espalhar a estrutura aleatoriamente.

** Na vista da camada de cura, o recheio aparecerá na forma de linhas muito grossas.Isso ocorre porque o Cura assume que o material permanece na mesma camada e se espalha lá.Na realidade, ele cairá.

** Quando um enchimento de espaguete é usado, o parâmetro [largura da linha de enchimento](../Resolução/Infill_line_width.md) não tem mais efeito.A largura da linha é ajustada para atender às necessidades dos parâmetros [distância da linha de enchimento](../prelocill_line_distance.mdis) e [Spaghetti Flow](spaghetti_flow.md). **


