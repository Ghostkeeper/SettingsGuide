额外皮肤壁计数
====
当使用直线图案打印顶和底时，皮肤区域的外沿也可以使用若干条同心线打印。这与打印额外壁不同，额外皮肤壁也被放置在皮肤和填充之间。

<!--screenshot {
"image_path": "skin_outline_count_0.png",
"models": [
{
"script": "stamp.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [38, 38, 99],
"settings": {"skin_outline_count": 0},
"layer": 115,
"colours": 64
}-->
<!--screenshot {
"image_path": "skin_outline_count_2.png",
"models": [
{
"script": "stamp.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [38, 38, 99],
"settings": {"skin_outline_count": 2},
"layer": 115,
"colours": 64
}-->
![没有额外的皮肤壁](../images/skin_outline_count_0.png)
![两条额外的皮肤壁](../images/skin_outline_count_2.png)

通常皮肤线条可以在稀疏填充内结束。届时它们的结束点会稍微下沉一点儿。如果存在额外皮肤壁，皮肤的轮廓会先得到打印，然后打印普通皮肤线条并结合到轮廓上。这样，皮肤就不会下沉很多。最终会略微提高表面质量。
