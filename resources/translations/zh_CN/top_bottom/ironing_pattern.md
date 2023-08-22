熨平图案
====
熨平会使用某一图案来覆盖顶面。该设置定义这个图案的类型。

选择图案的目的是为了形成光滑、连续的表面。如果图案存在中断，会在顶面上生成可见的边框。有两种图案可供选择。

<!--screenshot {
"image_path": "ironing_enabled_enabled.png",
"models": [
{
"script": "dial_brace.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 14, 83],
"settings": {
"layer_height": 0.2,
"ironing_enabled": true
},
"colours": 64
}-->
锯齿形
----
![锯齿形熨平图案](../images/ironing_enabled_enabled.png)

喷嘴在表面上来回移动。对大多数表面效果都可靠、良好，缺点是有时会产生超出预期的边框。

<!--screenshot {
"image_path": "ironing_pattern.png",
"models": [
{
"script": "dial_brace.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 14, 83],
"settings": {
"layer_height": 0.2,
"ironing_enabled": true,
"ironing_pattern": "concentric"
},
"colours": 64
}-->
同心圆
----
![同心圆熨平图案](../images/ironing_pattern.png)

该图案使喷嘴从里向外画圆。这会使边框降至最低，缺点是在中心位置同心圆变得非常小时，由于喷嘴在同一位置停留过久，造成了材料劣化。于是会在表面上留下了一个可见的点。所以呢，又细又长的表面相比长宽相等的表面更适合这个图案。
