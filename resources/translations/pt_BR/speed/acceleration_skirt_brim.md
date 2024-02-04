Aceleração da saia/borda
====
Esse ajuste controla a velocidade na qual o bico acelera em direções diferentes durante a impressão da saia ou borda.A aceleração durante a impressão da saia ou borda pode ser ajustada para uma velocidade diferente da restante da impressão.Mesmo que a saia e a borda sejam sempre exclusivas da camada inicial, esse parâmetro substitui o parâmetro [aceleração da impressão da camada inicial](aceleração_print_layer_0.md).Eles são impressos usando a aceleração determinada com este parâmetro, não o parâmetro para a camada inicial em geral.

A borda é crucial para a adesão do leito; portanto, a redução das taxas de aceleração durante a impressão na borda pode reduzir as vibrações durante a impressão na borda, depois melhorar a adesão da borda ao platô de impressão, aumentando a eficácia da borda para um menor custo de tempo de impressão.

O efeito da aceleração na borda e na saia é geralmente muito baixo, porque são linhas com curvas doces.A aceleração é frequentemente completamente suportada pelo parâmetro [sacada da saia/borda](jerk_skirt_bim.md).