启用支撑接触面
====
"支撑接触面"是位于常规支撑和模型之间的中间结构。此结构可以调整支撑与模型的接触面的属性，而不会对支撑的大部分产生太大影响。

<!--screenshot {
"image_path": "support_interface_enable.png",
"models": [{"script": "trash_bin_lid.scad"}],
"camera_position": [93, 188, 87],
"settings": {
"support_enable": true,
"support_interface_enable": true
},
"colours": 64
}-->
![支持接触面以深蓝色显示](../images/support_interface_enable.png)

默认情况下，接触面层的密度大于普通支撑。这就实现了一个更好的悬垂表面，而不需要那么多额外的材料和打印时间。但是，移除支撑会更难。

也可以用与支撑件的其余部分不同的挤出机来打印支撑件接触面。一些旨在专门用于支撑的材料可能非常昂贵，并且打印缓慢。这样，大多数支撑件仍然用更便宜或更快的材料印刷，但是支撑界面则如愿使用更漂亮的材料完成。
