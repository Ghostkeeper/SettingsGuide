构造板附着类型
====
有三种类型的构造板附着：skirt（裙边）, brim（帽檐）及raft（筏板）也可以通过将其设置为"无"（None）来轻松禁用。

<!--screenshot {
"image_path": "adhesion_type_skirt.png",
"models": [
{
"script": "stamp.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 128, 53],
"settings": {"adhesion_type": "skirt"},
"colours": 64
}-->
<!--screenshot {
"image_path": "adhesion_type_brim.png",
"models": [
{
"script": "stamp.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 128, 53],
"settings": {"adhesion_type": "brim"},
"colours": 64
}-->
<!--screenshot {
"image_path": "adhesion_type_raft.png",
"models": [
{
"script": "stamp.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [0, 128, 53],
"settings": {"adhesion_type": "raft"},
"colours": 64
}-->
![Skirt](../images/adhesion_type_skirt.png)
![Brim](../images/adhesion_type_brim.png)
![Raft](../images/adhesion_type_raft.png)

Skirt
----
Skirt是一条围绕着你的打印件的线。它不会直接对构造板粘附力有任何贡献。但是，如果您不想使用其他粘附方法，此方法仍有两个功能。
* 在开始打印实际模型之前，它会使喷嘴进行灌注，以确保材料正确流动。
* 它可以让你看到你的构造板是否被正确地调平。

Brim
----
Brim是模型底部周围的单层平坦区域。它的目的是保持打印件的边缘向下（不翘边），并使其与构造板间的接触面积更大。
* 更大的表面积使您的打印件更好的附着在构造板上。这对于几乎所有大于几厘米的打印都很有用。
* 这个边缘也会保持打印件的边缘向下。冷却时收缩很大的材料（如ABS）在打印时往往会翘曲很大。有一个足够宽的边缘可以保持角落在适当的位置，防止这种翘曲。

Raft
----
Raft是模型与构造板之间的厚板。这个Raft可以保护你的打印件不受构造板热量的影响。它也将有很大的表面积与构造板粘附。打印件被放在这个Raft的顶部，在那里它可能会粘得更好。很薄的打印件要小心，因为它可能很难无损取下Raft。
