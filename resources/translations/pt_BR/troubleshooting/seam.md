De costura
====
As paredes da sua impressão são impressas em cachos contínuos, mas a impressora deve iniciar esse loop em algum lugar e fechá -la corretamente.Se o loop não estiver bem fechado, será criada uma costura visível.Essas costuras são difíceis de remover completamente, mas é possível escondê -las ou reduzir seu tamanho.

![Uma longa costura vertical na superfície](../../../articles/images/seam.jpg)

Não confunda com a "junta z", que é uma junta criada quando o bico se move na altura da próxima camada.Esse movimento interrompe o bico por um breve momento, criando um [blob](blobs.md) lá.A terminologia da cura relativa às configurações de costura está historicamente errada a esse respeito, porque suas configurações "z -sewing" tão chamadas realmente dizem respeito ao local onde a costura normal.

Colocação de costura
----
As costuras são difíceis de evitar, mas geralmente é muito fácil esconder a costura em um local onde não é tão visível.

O parâmetro principal para ajustar a localização da costura é o [alinhamento do z](../shell/z_seam_type.md).Para esconder a costura, coloque -a no canto mais claro.Com o parâmetro [preferência do canto](../shell/z_seam_corner.md), você pode escolher os tipos de cantos para selecionar.Para esconder a costura, é melhor escolher "ocultar" ou "máscara inteligente", que coloca a costura em um canto interno.Se o seu modelo não tiver cantos internos para se esconder, você poderá escolher "expor a junção" para colocar a costura em um canto externo angular, onde também é menos visível do que em uma superfície plana.

Se o posicionamento automático não funcionar bem, você também pode optar por colocar a costura escolhendo "usuário especificado".Isso permitirá que você insira as coordenadas [x](../shell/z_seam_x.md) e [y](../shell/z_seam_y.md) do local onde a costura será posicionada.Escolha um local onde a costura não será visível.

Se tudo o mais falhar, você também poderá espalhar a costura em toda a superfície selecionando "aleatório".Em vez de uma articulação contínua na sala, a articulação estará localizada em locais aleatórios na superfície.A superfície ficará um pouco marcada, mas não haverá costura real.

Fechamento da costura
----
A costura também pode ser menos visível fechando a articulação com mais cuidado quando foi criada.Aqui estão alguns parâmetros que podem ser ajustados para reduzir a visibilidade das costuras.
* Aumente ligeiramente a [distância de limpeza da parede externa](../shell/wall_0_wipe_dist.md).Esse ajuste significa que o bico continua brevemente seu movimento ao redor do contorno após fazer um loop.Isso evita criar um espaço onde o contorno esteja fechado.No entanto, se essa configuração for aumentada demais, existe o risco de depositar muito material em torno de onde a costura está localizada, o que a tornaria visível novamente.
* O oposto é usar [a roda livre](../experimental/Coasting_enable.md).Isso permite que você interrompa a extrusão do material pouco antes de o contorno ser fechado.Isso reduz a pressão dentro do bico.A idéia aqui é que não haverá muita superextrusão quando o contorno for concluído, o que reduz a projeção do selo para fora.Assim que o bico se move no início do contorno, o plástico colocado anteriormente bloqueia facilmente qualquer plástico novo, pois a pressão no bico não pode superar a falsificação da linha de parede solidificada.
* Imprima a parede externa mais [lentamente](../speed/speed_wall_0.md).O material poderá fluir melhor para fechar o selo no final.