Inicie as camadas com a mesma posição
====
Originalmente, esse parâmetro significava que a impressora iniciou cada camada com o objeto mais próximo da posição especificada nos parâmetros [x camada inicial](Layer_Start_X.MD) e [y Start Layer](Layer_Start_Y.md), em vez do objeto que possuía foi impresso por último na camada anterior.

** O parâmetro estava oculto no Cura 2.4 e não foi excluído corretamente, e é por isso que esse parâmetro ainda existe nesta lista.No entanto, não tem efeito na impressão. **

O comportamento alternativo não era mais possível após a implementação da impressão de peça por peça, portanto o parâmetro estava oculto.

A impressão de cada camada na mesma ordem evita empilhar duas camadas umas sobre as outras imediatamente após a outra, se houver várias peças para imprimir.Isso permite que a camada anterior esfrie mais enquanto o bico está ocupado imprimindo as outras partes.Isso melhora a saliência e reduz a banda e a flacidez.Por outro lado, isso permite que a impressora se mova um pouco mais, o que aumenta um pouco o tempo de impressão.