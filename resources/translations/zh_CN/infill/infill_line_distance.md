填充走线距离
====
除了按百分比对[填充密度](infill_sparse_density.md)进行调节外，还可通过设置相邻填充线间的距离来调节填充密度。填充线之间的距离越大，整体填充密度越低。

填充走线距离是与密度不同的观察该属性（填充密度）的方法。填充走线距离指定了顶部皮肤线从一条填充线跨越到下一条填充线所必须经过的距离。因此，减小填充走线距离可减小桥接距离并提高顶面的质量。

<!--screenshot {
"image_path": "infill_pattern_grid.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "grid"
},
"colours": 64
}-->
<!--screenshot {
"image_path": "infill_sparse_density_low.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_sparse_density": 10
},
"colours": 64
}-->
![4mm填充线间距，结果为20%密度](../images/infill_pattern_grid.png)
![8mm填充线间距，结果为10%密度](../images/infill_sparse_density_low.png)

通常，填充走线距离是根据期望的填充密度计算而来，具体取决于选取的填图案和线宽。填充走线距离是首要因素。

增加填充密度（减少走线距离实现）会对打印产生很大影响，即：
* 打印件更坚固。
* 顶部皮肤将得到更好的支撑，使其更光滑、更防水。
* 减少枕形效应，因为热窝会更小。
* 您的打印件需要更多材料，因此会更重。
* 打印时间较长。
