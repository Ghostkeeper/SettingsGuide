熨平嵌入
====
熨平通常不会一直平滑到外边缘。如果这样做，喷嘴室中的持续压力将导致材料溢过边缘，这将导致一种波纹效应。此设置确定熨烫将与边缘保持多远的距离。

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
<!--screenshot {
"image_path": "ironing_inset.png",
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
"ironing_inset": 1.2
},
"colours": 64
}-->
![以走线宽度的一半进行的默认嵌入](../images/ironing_enabled_enabled.png)
![以1.2mm进行的较大嵌入](../images/ironing_inset.png)

此设置有两种主要的使用情况：
*确保材料不会沉积在边缘上。
*过滤掉通常会被熨烫的细线的一种方法。如果有一个缓坡，您可能并不想让它上面的每一层都被熨烫。增大此值可以过滤掉最薄的线条，但也会导致较大的部分无法一直熨烫到边缘。
