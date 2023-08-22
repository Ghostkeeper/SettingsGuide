顶部皮肤挤出机
====
对于有多个挤出机的打印机，该设置确定哪个挤出机用来打印顶层。

<!--screenshot {
"image_path": "roofing_extruder_nr.png",
"models": [
{
"script": "question_stick_clip.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, -90, 60],
"settings": {
"wall_line_count": 0,
"skin_outline_count": 0,
"roofing_layer_count": 1,
"roofing_extruder_nr": 1
},
"colour_scheme": "material_colour",
"colours": 32
}-->
![该模型只在打印顶部皮肤层使用不同的颜色](../images/roofing_extruder_nr.png)

通过这种方式可以使用不同的颜色或材料打印顶层皮肤。需要注意的是：壁的挤出机不受此设置调节，所以顶部周围仍会有一个边缘。

除了使用不同的颜色外，还可以通过此设置选择不同的材料。效果如下：
* 在使用更具刚性的材料打印时，顶层和外壁使用PLA。可以使成品坚固且美观。
* 使用TPU打印顶层，更坚硬的材料打印其余部分，可以获得柔软，且具高摩擦力的表面。
* 如果需要良好的表面滑动，则可以使用比内部更光滑的材料打印顶层。

**如果两种材料不能很好的粘附在一起，打印后会容易脱落。所以请特别注意收缩率高的材料。**
