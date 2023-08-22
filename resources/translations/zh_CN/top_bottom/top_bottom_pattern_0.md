底层图案起始层
====
该设置用来配置构造板上（或raft上）的模型底部用何种图案打印。这些层的图案与其余底层的将分别配置。

<!--screenshot {
"image_path": "top_bottom_pattern_0.gif",
"models": [
{
"script": "gear_hollow.scad",
"transformation": ["scale(0.5)"]
}
],
"camera_position": [40, -40, 110],
"settings": {"top_bottom_pattern_0": "concentric"},
"layer": [1, 2, 3],
"colours": 64
}-->
![起始层使用同心圆图案，但其余部分使用直线图案](../images/top_bottom_pattern_0.gif)

同心圆图案可以比其图案更好的粘附在构造板上，因为线条收缩时的张力会向所有方向分散。这避免了翘曲，并改善了部件的可靠性。其他图案都只向一个方向收缩。

在raft上打印时，直线图案会使部件稍强。这些线也是定向的，使得它们很好地桥接raft线条的间隙，从而形成更平滑的底面。
