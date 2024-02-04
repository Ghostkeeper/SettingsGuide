Fluxo de espaguete
====
Esse ajuste possibilita ajustar diretamente a densidade do enfeite de espaguete.

Normalmente, ao imprimir um enchimento, a densidade de preenchimento](../preenchimento/refill_sparse_density.md) afeta apenas a [distância entre as linhas de enchimento](../preenchimento/enchill_line_distance. Md).Como a [largura da linha de enchimento](../Resolução/Infill_Line_Width.m) permanece a mesma, mas que as linhas estão mais próximas, o aumento da densidade de enchimento tem o efeito de uma parte maior do enchimento de volume de volume é preenchido com material no final.

Isso funciona de maneira diferente se o preenchimento [Spaghetti](Spaghetti_infill_enabled.md) for ativado.A distância entre as linhas de enchimento permite não apenas ajustar a distância entre as linhas de enchimento, mas a largura da linha também será ajustada para obter a densidade desejada, conforme especificado por este parâmetro.Este parâmetro especifica exatamente a fração do volume total de enchimento que será preenchido com material.Se esse parâmetro for aumentado, as linhas se tornarão mais amplas.

Ao usar espaguete para produzir recheios flexíveis, esse ajuste determina essencialmente a rigidez do material de enchimento.Ao reduzir a taxa de fluxo, é obtido um material de enchimento mais flexível, enquanto aumentamos o fluxo, obtemos um material de enchimento mais rígido.No entanto, a redução excessiva no fluxo impede que o material de enchimento também seja distribuído.Ele tenderá a cair no volume e produzir muito espaguete que não aumentará a rigidez acima.

Ao usar o recheio de espaguete para fluir do material, esse ajuste provavelmente deve estar próximo de 100% para preencher completamente o modelo de material.No entanto, você sempre pode ajustá -lo um pouco se o seu material tende a se contratar ou expandir.

** Este parâmetro é sempre multiplicado pelo parâmetro [fluxo de enchimento](../material/infill_material_flow.md). **


