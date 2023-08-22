意面填充最大角度
====
此设定可规划最大悬垂角度，在该角度下，当填充材料沉积在材料旁边时，材料将达到该角度。如果由于此限制而无法使用正确的密度填充某个点，则将沿填充体积的高度引入附加的[步长](spaghetti_infill_stepped.md)，以确保正确到达这些位置。

如果要将意面填充用作弹性填充，则此设定可能应设定得相当高。增加此设置将导致引入更多台阶以到达浅屋顶下。由于意面填充不会在水平方向上扩展很远，因此添加其他台阶有助于将材质推到这些浅屋顶的下方。

如果意面填充物打算与铸造材料一起使用，则该设置可显著降低。因为铸造材料是液体，所以它可以到达表面下很远的地方。但不要将其设置为0 °，因为大多数模型材料都有一定的粘度。您可能仍然希望在一些浅屋顶下铸造一些，以确保铸件完全遵循其外壳。