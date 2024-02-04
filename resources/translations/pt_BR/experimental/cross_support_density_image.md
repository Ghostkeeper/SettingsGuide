Imagem da densidade de enchimento cruzado para suporte
====
Neste parâmetro, você pode fornecer uma imagem que especifica a densidade em diferentes locais do suporte.A densidade do suporte varia em certos lugares, dependendo do brilho da imagem.Isso funciona apenas para o [motivo cruzado](../support/support_pattern.md), porque esse padrão é capaz de ajustar sua densidade sem cruzar as linhas, o que resultaria em uma interrupção do fluxo e uma redução na força.

![A densidade do suporte é mais importante nas laterais](../../../articles/images/cross_support_density_image.png)

![O arquivo de imagem usado para criar este padrão](../../../articles/images/cross_support_density_image_mask.png)

O caminho para a imagem é fornecido como um caminho local, por exemplo, `C: \ Projects \ 3D Printing \ Support_Dension.png` em Windows Or`/Home/Ghostkeeper/3D_Printing/Support_Dension.png` sous Unix.Os formatos de arquivo suportados são JPG, PNG, TGA, BMP, PSD, GIF, HDR e PIC.A imagem é configurada na impressão para que ela se adapte exatamente à caixa da cena impressa.O brilho da imagem determina a densidade do suporte:
* Quando a imagem é preta, é usada a [densidade do suporte](../support/support_infill_rate.md).
* Se a imagem for branca, a densidade de suporte será próxima de 0 %.

A densidade de suporte nunca excederá o valor especificado pela [distribuição do processo da pressa](../support/support_line_distente.md).Só pode ser reduzido.O modelo também é limitado nos casos em que pode reduzir sua densidade.Embora ele tente chegar o mais próximo possível da densidade de suporte desejada, isso nem sempre é possível.Se a densidade do suporte for realmente baixa, haverá particularmente poucas possibilidades de ajustar a densidade do suporte, o que fará com que a impressão siga a imagem de uma maneira muito solta.Em locais onde a densidade do suporte é alta, a imagem será seguida de perto.A densidade escolhida também é altamente quantificada.A densidade só pode ser dobrada ou reduzida pela metade, mas o Cura [percebe uma difusão de erro](https://fr.wikipedia.org/wiki/diffusion_d%27erreur) sobre o motivo para obter maior precisão efetiva.

Com essa configuração, você pode personalizar seu suporte muito longe.Se certas partes da sua impressão provavelmente cederão ou devem ser impressas com grande precisão, você pode aumentar localmente a densidade neste local para melhor apoiá -las, sem ter que dar um grande golpe no tempo de impressão ou tornar o suporte mais difícil de remover .

** Este parâmetro não será bem transferido através dos arquivos do projeto Cura.O arquivo do projeto gravará o caminho da imagem como um valor de ajuste, mas não armazenará a imagem.Se o arquivo do projeto estiver aberto a outro computador, a imagem de densidade provavelmente não será restaurada. **

