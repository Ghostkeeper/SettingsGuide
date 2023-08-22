起始层水平扩展
====
该设置仅扩展位于构造板上（或者raft上）的起始层。与[水平扩展](xy_offset.md)类似，正值会使起始层变宽，而负值会使起始层收缩。

<!--screenshot {
"image_path": "xy_offset_layer_0_original.png",
"models": [
{
"script": "d1.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 30, 0],
"camera_lookat": [0, 0, 0],
"settings": {"xy_offset_layer_0": 0},
"colours": 16
}-->
<!--screenshot {
"image_path": "xy_offset_layer_0_enabled.png",
"models": [
{
"script": "d1.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 30, 0],
"camera_lookat": [0, 0, 0],
"settings": {"xy_offset_layer_0": -0.6},
"colours": 16
}-->
![原始模型](../images/xy_offset_layer_0_original.png)
![起始层收缩后](../images/xy_offset_layer_0_enabled.png)

起始层通常被打印在加热的构造板上，热量使其略微保持液态，以提高对构造板的粘附力；起始层通常也会比其它层更厚。这使得它有足够的时间和材料从侧面下垂，形成“象脚”，即底层边缘有轻微的突出。该设置可通过提前使起始层更薄来补偿象脚现象。把水平扩展设置成一个小的负值来进行。

起始层设置成很大的值会在零件周围形成类似brim的边，便于结合其他粘附技术如raft。但是呢，这会导致皮肤膨胀，第二层的壁恐怕要打进皮肤里了。

**该设置与BRIM结合使用时无效，因为BRIM一律在起始层周围产生一个大的边界**
