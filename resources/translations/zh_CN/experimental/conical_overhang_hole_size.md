最大悬垂孔面积
====
因为[使悬垂可打印](conical_overhang_enabled.md) 会移除任何类型的悬垂，所以任何桥都会自动降低，并关闭其下方的悬垂。然而，如果悬垂的所有边都被封闭，它将不断降低，直到封闭的悬垂被完全填满。实际上，任何朝下的洞都将被完全填满，即使需要移除的悬垂物只是顶部的一个小点。

若要防止此效果，如果悬垂的所有边都封闭且小于特定区域，则此设定可让悬垂保持开放。这仅适用于孔。模型外部的常规悬垂仍将向下延伸，以保持合理的可打印角度。

<!--screenshot {
"image_path": "conical_overhang_hole_size.png",
"models": [{"script": "plopper.scad"}],
"camera_position": [-86, 29, -85],
"settings": {
"conical_overhang_enabled": true,
"conical_overhang_hole_size": 20
},
"colours": 64
}-->
![允许顶部的一个小点保持悬垂，因此该孔不会被填满](../images/conical_overhang_hole_size.png)

对于大多数模型，此设置的值设为几十平方毫米是相当安全的。如果设置得太低，模型将被修改的更多，实际上太小而不需要任何支撑的悬垂也将获得支撑。但是，如果设置得太高，则会有很大的悬垂区域，可能难以桥接。

如果由于此设置产生了大面积的悬垂，则最好先查看[启用连桥设置](bridge_settings_enabled.md)，然后再尝试修改模型以删除悬垂。
