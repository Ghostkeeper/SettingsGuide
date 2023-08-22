走线宽度（支撑结构）
====
绘制支撑的线条宽度可以与其余部分的宽度不同。（

<!--screenshot {
"image_path": "support_line_width.png",
"models": [
{
"script": "clamp.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [28, 57, 90],
"settings": {
"support_enable": true,
"support_line_width": 0.8
},
"layer": 350,
"colours": 128
}-->
![支撑部分的线宽远大于其他部分](../images/support_line_width.png)

支撑通常不需要太精确，所以使用更大的线宽既节省时间，又不影响强度。需要注意的是：为了从整体上达到支撑的密度，线条之间会隔得较远，这会降低悬垂表面的质量。
