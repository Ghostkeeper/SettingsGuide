填充密度
====
此设置可配置打印件内部的体积密度，这是影响最终打印强度和表面质量的主要因素。填充密度越大，填充线被放置在一起的距离就越近。你甚至可以超过100%的密度，但这将导致挤出过度。

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
![20% 密度](../images/infill_pattern_grid.png)
![10% 密度](../images/infill_sparse_density_low.png)

不同的密度与不同的填充图案配合使用效果更佳。在填充密度很大时，具有许多拐角和交叉的填充图案将无法很好地工作。拐角是个问题，因为线材往往会随着拐角一起拖动，在拐角的外侧（材料本应沉积的地方）产生气室。交叉是一个更大的问题，因为当一条线与另一条线交叉时，它的流动将被中断，从而导致交叉后的部分挤出不足。

增加填充密度（减少走线距离实现）会对打印产生很大影响，即：
* 打印件更坚固。
* 顶部皮肤将得到更好的支撑，使其更光滑、更防水。
* 减少枕形效应，因为热窝会更小。
* 您的打印件需要更多材料，因此会更重。
* 打印时间较长。
