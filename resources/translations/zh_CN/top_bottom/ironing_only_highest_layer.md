仅熨平最高层
====
开启本设置，将只在物品的最高层进行熨平。如果您的模型虽然存在很多种表面，但只有最高层是可见的，或者只有最高层需要平滑。那么开启本设定将为您节约大量的打印时间。

<!--screenshot {
"image_path": "ironing_only_highest_layer.png",
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
"ironing_only_highest_layer": true
},
"colours": 64
}-->
![较低层的弧线不会得到熨平](../images/ironing_only_highest_layer.png)

** 如果打印件有多个对象， 每个对象的最高层将被熨平。这包括多喷头打印机的每个部分。**
