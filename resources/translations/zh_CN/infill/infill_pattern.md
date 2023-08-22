填充图案
====
填充图案定义了用于填充对象体积的结构。有多种模式可供选择，每种模式都有各自的优点。有些专门用于非常特殊的应用。

<!--screenshot {
"image_path": "infill_pattern_grid.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "grid"
},
"colours": 64
}-->
网格
----
![网格](../images/infill_pattern_grid.png)

网格填充图案创建两组垂直的线。这一起形成了一个正方形的图案。
* 垂直方向上强度最高的模式。
* 两个方向的线条强度相当。
* 对角线上就没那么结实了。
* 可以非常好的支撑顶面。表面看起来非常光滑。

<!--screenshot {
"image_path": "infill_pattern_lines.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "lines"
},
"colours": 64
}-->
直线
----
![直线](../images/infill_pattern_lines.png)

直线图案会建立平行线。依预设，线条图案会在各层之间垂直地交替其方向，乍一看像是网格图案。但是，这可以使用[填充走线方向](infill_angles.md)进行更改。
<!--if cura_version<4.12:* 由于线间距离最小，所以和锯齿图案一样是确保表面平滑的最佳图案-->
* 在垂直方向上往往较弱，因为各层只有很小的点结合在一起。
* 在水平方向上将是极弱的，除了在线所定向的一个方向上。但即使在那个方向上，它也不能抵抗剪切，所以它在负载下会相当快地失效。

<!--screenshot {
"image_path": "infill_pattern_triangles.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "triangles"
},
"colours": 64
}-->
三角形
----
![Triangles](../images/infill_pattern_triangles.png)

三角形样式会在三个不同的方向上建立三组线。它们一起形成了三角形的图案。
* 非常耐剪切。
* 在每个水平方向上的强度大致相等。
* 顶线必须桥接相当长的距离，需要许多顶层皮肤才能获得平坦的顶面。
* 在交叉口处，流量被严重中断，导致在高填充率下强度相对较低。

<!--screenshot {
"image_path": "infill_pattern_trihexagon.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "trihexagon"
},
"colours": 64
}-->
内六角
----
![内六角](../images/infill_pattern_trihexagon.png)

与三角形图案类似，内六角图案在三个不同的方向上创建三组线，但它们彼此偏移，因此它们不会在同一位置相交。
* 水平方向上的最强模式。
* 在每个水平方向上的强度大致相等。
* 非常耐剪切。
* 顶线必须桥接很长，需要许顶层皮肤以获得平坦的顶面。

<!--screenshot {
"image_path": "infill_pattern_cubic.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "cubic",
"infill_sparse_density": 19
},
"colours": 64
}-->
立方体
----
![Cubic](../images/infill_pattern_cubic.png)

立方体图案创建立方体，即三维图案。立方体的朝向总是对着一个角落，这允许他们无需突出的内表面即可打印。
* 在每个方向（包括垂直方向）上的强度大致相等。
* 在各个方向强度相当。
* 枕头效应降低，因为它不会产生很长的垂直热袋（空气）。

<!--screenshot {
"image_path": "infill_pattern_cubic_subdivision.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "cubicsubdiv",
"infill_sparse_density": 50
},
"layer": 240,
"colours": 64
}-->
立方体分区
----
![立方体分区](../images/infill_pattern_cubic_subdivision.png)

立方体分区填充图案创建立方体，即三维填充图案。立方体的朝向总是对着一个角落，这允许他们无需突出的内表面即可打印。然而，这种模式将产生朝向内部体积的更大立方体，从而节省材料。它会在填充线最没用的地方省略填充线。

此样式可能会产生低于所需的填充密度。使用此样式时，建议您大幅增加填充密度。在高填充率下，优化效果最佳。

从算法上讲，这种模式是通过在整个体积周围创建一个巨大的立方体，然后在立方体碰到任何墙壁时将其细分为8个子立方体来生成的。这是递归的，因此，子立方体击中任何墙壁会被一次又一次的细分。重复此操作，直到达到填充走线距离的设置。
* 按重量和印刷时间计算，是最坚固的图案。
* 在每个方向（包括垂直方向）上的强度大致相等。
* 薄片部分会浓缩填充。
* 枕头效应降低，因为它不会产生很长的垂直热袋（空气）。
* 如果使用增加的填充密度，填充物不会透过墙壁发出太多的光，从而在相同的打印时间内产生更好的表面质量。
* 引入了回抽，这对弹性或流动的材质效果不佳。
* 需要更长的时间来切片。

<!--screenshot {
"image_path": "infill_pattern_octet.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "tetrahedral",
"infill_sparse_density": 21
},
"colours": 64
}-->
八角形
----
![八角形](../images/infill_pattern_octet.png)

八角形图案创建了规则四面体和立方体的组合，即三维图案。多条填充线将经常彼此相邻放置。
* 在多条平行线接触的位置创建坚固的内部框架。载荷迅速向该内部框架消散。
* 适用于中等厚度（约1厘米）的模型。
* 枕头效应降低，因为它不会产生很长的垂直热袋（空气）。
* 导致顶部皮肤的桥接距离非常长，这降低了顶部表面质量。

<!--screenshot {
"image_path": "infill_pattern_quarter_cubic.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "quarter_cubic",
"infill_sparse_density": 21
},
"colours": 64
}-->
四面体
----
![四面体](../images/infill_pattern_quarter_cubic.png)

四面体创建由四面体和截断四面体组成的三维镶嵌。多条填充线将经常彼此相邻放置。
* 创建两个分离的内部框架，类似于八角形，其中多条平行线接触。载荷迅速向该内部框架消散。框架朝向两个不同的方向，使它们各自较弱，但减少了将载荷分布到这些框架的距离。
* 适用于厚度较薄（仅几毫米）的模型。
* 枕头效应降低，因为它不会产生很长的垂直热袋（空气）。
* 导致顶部皮肤的桥接距离非常长，这降低了顶部表面质量。

<!--screenshot {
"image_path": "infill_pattern_concentric.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "concentric"
},
"colours": 64
}-->
同心圆
----
![同心圆](../images/infill_pattern_concentric.png)

同心填充图案将创建与壁平行的环。
* 使用100%填充时的填充图案最强，因为不仅没有线相交，而且线的方向也会使线的各向异性强度分散负载。
* 产生最柔软的印刷品，在所有水平方向上的强度非常弱且均匀。
* 在垂直方向上比在水平方向上强。
* 在100%填充密度的情况下，材料可能在中间结块，从而降低了打印圆形形状的可靠性，尤其是同心圆聚集在一个点的地方。
* 对于一些形状，一些填充线可以悬在半空中，不增加额外的材料成本和印刷时间的强度。
* 如果未使用100%填充，则这是水平方向上最弱的填充图案。它一点力量也没有。

<!--screenshot {
"image_path": "infill_pattern_zigzag.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "zigzag"
},
"colours": 64
}-->
锯齿形
----
![锯齿状](../images/infill_pattern_zigzag.png)

锯齿状填充图案使喷嘴以之字形方式绘制填充线。这与直线类似，但各填充线连接成一条长线，这可防止流量中断。
* 使用100%填充时，是第二强的填实图案。但是，它比使用圆形的同心图案更可靠地打印。
* 锯齿状是实现光滑表面的最好模式，因为线之间的距离是最小的。
* 在垂直方向上往往相当弱，因为各层连接的部分只是一些小点。
* 在水平方向上将是极弱的，除了在线所定向的一个方向上。但即使在那个方向上，它也不能抵抗剪切，所以它在负载下会相当快地失效。

<!--screenshot {
"image_path": "infill_pattern_cross.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "cross"
},
"colours": 64
}-->
交叉
----
![交叉](../images/infill_pattern_cross.png)

交叉填充图案制造出一个空间填充曲线，像是延内部体积生成的十字架。
* 在所有水平方向上均匀地软化，这对于打印柔软和有弹性的对象非常有用。
* 在水平方向上不产生长直线，使其沿整个周长均匀地变软。没有什么亮点。
* 完全不发生回抽，更易于使用柔性材料打印。
* 将在垂直方向上比在水平方向上更强。
* 要花很长时间完成切片。
* 在所有的水平方向上都会非常弱。

<!--screenshot {
"image_path": "infill_pattern_cross_3d.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "cross_3d"
},
"colours": 64
}-->
交叉3D
----
![交叉3D](../images/infill_pattern_cross_3d.png)

交叉3D填充图案会产生一个空间填充曲线，该曲线会产生类似于沿体积内部生成的十字架状的结构。该图案沿Z轴脉动，以使其在垂直方向上较弱。
* 在所有方向（水平和垂直方向）上近似均匀的软化，使其成为打印柔软和有弹性物体的最有用的图案。
* 不生成长直线，使其沿整个曲面均匀地软化。
* 完全不发生回抽，更易于使用柔性材料打印。
* 要花很长时间完成切片。
* 四面八方都将十分的薄弱。

<!--screenshot {
"image_path": "infill_pattern_gyroid.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "gyroid"
},
"colours": 64
}-->
螺旋二十四面体
----
![螺旋二十四面体](../images/infill_pattern_gyroid.png)

螺旋二十四面体回填充图案会产生方向交替的波浪样式。
* 产生一个可完全透过液体的体积，使其成为可溶解材料的有用图案。
* 各个方向都一样结实，但不是很僵硬。这使其对于弹性材料非常有用，但结果会比交叉3D填充图案稍硬，不太软。
* 在这种图案中没有重叠的线条，这使得使用具有更高表面张力的材料更容易打印，并使填充非常可靠和一致。
* 抗剪切。
* 需要很长时间进行切片，并生成较大的g代码文件。对于某些打印机，可能很难跟上每秒许多g代码命令的速度，并可能很难在低比特率下跟上串行连接的速度。

<!--screenshot {
"image_path": "infill_pattern_lightning.png",
"models": [{"script": "hexagonal_prism.scad"}],
"camera_position": [0, 0, 180],
"settings": {
"top_layers": 0,
"infill_pattern": "lightning"
},
"colours": 64
}-->
<!--screenshot {
"image_path": "infill_pattern_lightning_side.png",
"models": [{"script": "three_cylinders.scad"}],
"camera_position": [148, 23, 126],
"settings": {
"top_layers": 0,
"wall_line_count": 0,
"infill_pattern": "lightning",
"infill_sparse_density": 30
},
"colours": 32
}-->
<!--if cura_version>=4.12-->
闪电形
----
![闪电形](../images/infill_pattern_lightning.png)
![闪电图案从侧面开始构建](../images/infill_pattern_lightning_side.png)

闪电形填充图案是锯齿状的最小样式，仅用于支撑顶部曲面。指定的填充密度仅会在填充体积顶部的正下方达到。
* 通过只在表面下进行填充，节省了大量的时间和材料。
* 增加填充密度可在所有填充图案中获得最佳的顶面质量，同时无需花费更多的时间和材料。
* 通过不使用内嵌，可以防止内嵌在许多地方透过壁（而被看到）。
* 不会以任何显著的方式增加部件的强度。
<!--endif-->
