Taxa de contração (compensação de encolhimento do fator de escala)
====
<!-se Cura_version> = 4.8-> Essa configuração permite que o modelo seja configurado antes de cortá-lo automaticamente.O objetivo é compensar qualquer estreitamento que ocorra quando a impressão esfria à temperatura ambiente.Ao tornar a impressão um pouco maior do que o desejável, o resultado final pode ser mais preciso em comparação com as dimensões originais do modelo de entrada.Esse fator de escala é aplicado da mesma maneira a todas as dimensões (x, y e z).

Toda a cena é montada em seu centro.Ao imprimir vários modelos, todos eles são configurados no mesmo ponto original.Isso permite que você posicione esses modelos muito próximos um do outro, sem que eles se sobreponham durante a impressão final.As áreas de colisão do modelo são escadas, para que você possa ver exatamente onde a impressão terminará.Isso também impedirá que você coloque os modelos na cena em locais onde eles colidiriam com elementos de impressão ou impressora, como a torre de impressão ou os clipes da bandeja de impressão.

Um fator de 100 % não causará escala.Uma escala de escala ligeiramente maior que 100 % é adequada para muitos materiais de engenharia, como ABS ou polipropileno.Um fator de escala inferior a 100 % indicaria que o material se desenvolve no resfriamento, como uma espuma, talvez.

Dados puramente químicos sobre o estreitamento de um material entre a temperatura de impressão e a temperatura ambiente não são suficientes para prever um bom valor para esse parâmetro, porque o processo de impressão também influencia o estreitamento.Quando extrudado on -line, o plástico é esticado na direção do comprimento da linha e encolhe mais neste eixo.O estreitamento não é uniforme, mas essa configuração aplica apenas um fator de escala uniforme em todas as direções.Para resultados específicos, você deve aplicar o fator de escala ao eixo mais importante para o seu aplicativo.Se houver muitas linhas retas longas ao longo da dimensão mais importante, o fator de escala deve ser mais importante.

Se o fator de escala for superior a 100,5 % e você imprimir algo grande, a Cura exibirá um aviso de que você poderá começar a ter [deformação](../distúrbios/Warping.md). <!-endive->>

<!-Se Cura_version <4.8: Este é um ajuste descritivo, permitindo que a cura soubesse o quão estreita o material é alterado da temperatura de impressão para a temperatura ambiente.

Atualmente, este parâmetro não é usado para cortar.Ele é usado apenas para exibir um aviso ao usuário ao imprimir grandes peças se a taxa de estreitamento for superior a 0,5%.
->

*Este parâmetro não está visível na lista de parâmetros.É apenas um ajuste interno que deve ser esmagado pelo perfil do material.*