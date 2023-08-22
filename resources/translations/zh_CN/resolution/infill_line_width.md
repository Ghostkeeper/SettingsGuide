走线宽度（填充）
====
该设置定义正在绘制的每一条填充线条的宽度。通过略微增加或减少材料的挤出，线的宽度可以与喷嘴直径不同。多挤出一些会让材料流向侧面，线条变粗。少挤出一些会让材料在其表面张力的作用下被拉向喷嘴路径的中心线。

<!--screenshot {
"image_path": "infill_line_width.png",
"models": [{"script": "material_calibration.scad"}],
"camera_position": [35, 92, 122],
"settings": {"infill_line_width": 1},
"layer": 111,
"colours": 64
}-->
![填充线条的宽度明显大于其他线条](../images/infill_line_width.png)

增加填充线条的宽度将打造强度更高的零件，还省时。然而过多的增加会造成挤出波动，打印填充时挤出不足，紧随其后的其他部分挤出过度。当然，这个问题依然是由“流量调整延时”导致。

**如果设置了[填充层厚度](../infill/infill_sparse_thickness.md) ，实际的填充线宽可能比这里设置的更宽**
