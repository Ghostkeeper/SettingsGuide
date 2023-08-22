装填塔Brim
====
装填塔Brim是一个附加brim，类似于[打印平台附着类型](../platform_adhesion/adhesion_type.md)中的brim选项。此brim可与普通粘附分开启用和禁用。激活后，将在装填塔周围打印一个额外的brim。该brim是围绕主塔仅一层的平坦圆盘，其提高了装填塔与构造板的附着力。

<!--screenshot {
"image_path": "prime_tower_brim_enable.png",
"models": [
{
"script": "cube.scad",
"object_settings": {
"extruder_nr": 0
}
},
{
"script": "cube.scad",
"object_settings": {
"extruder_nr": 1
},
"transformation": ["translateX(40)"]
}
],
"camera_position": [50, -32, 133],
"camera_lookat": [93, -122, 5],
"settings": {
"prime_tower_enable": true,
"prime_tower_brim_enable": true,
"prime_tower_position_x": 600,
"prime_tower_position_y": 600,
"adhesion_type": "skirt"
},
"colours": 16
}-->
![附着类型选择skirt, 但依然有brim围绕装填塔](../images/prime_tower_brim_enable.png)

启用装填塔Brim将为塔提供更多的表面积，以连接到构造板。由于装填塔可以相当的高和薄，它可能会翻到。装填塔Brim在打印时间、用料量和构造板占用方面以较小的代价避免上述问题。

装填塔将brim获得 [Brim 宽度](../platform_adhesion/brim_width.md)中定义的宽度。如果打印平台附着类型设置为Brim，则此设置会有效地使装填塔周围Brim的宽度加倍.

装填塔Brim不能与raft结合。
