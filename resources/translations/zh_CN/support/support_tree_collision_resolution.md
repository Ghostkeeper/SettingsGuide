树形支撑碰撞分辨率
====
树形支撑的一个主要缺点是，当它被激活时，需要很长时间来切片。树形支撑所需的大多数计算都是针对树的分支进行的，以避免与网格发生碰撞。此设置决定了这些避免碰撞计算的精度。增加此分辨率（较低的精度）将节省大量计算时间，但也会使支持面在网格附近出现锯齿状。

<!--screenshot {
"image_path": "support_tree_collision_resolution_lo.png",
"models": [{"script": "castle_low.scad"}],
"camera_position": [-128, -63, 30],
"settings": {
"z_seam_position": "backright",
"support_enable": true,
"support_structure": "tree",
"support_tree_collision_resolution": 0.2
},
"colours": 32
}-->
<!--screenshot {
"image_path": "support_tree_collision_resolution_hi.png",
"models": [{"script": "castle_low.scad"}],
"camera_position": [-128, -63, 30],
"settings": {
"z_seam_position": "backright",
"support_enable": true,
"support_structure": "tree",
"support_tree_collision_resolution": 0.02
},
"colours": 32
}-->
![低分辨率（0.2毫米）会导致分支出现锯齿状](../images/support_tree_collision_resolution_lo.png)
![高分辨率（0.02毫米）可创建平滑的分支](../images/support_tree_collision_resolution_hi.png)

本设置的技术背景如下。为避免在启用树形支撑时与打印对象发生冲突，Cura将计算不允许树的分支中心进入的三维体积。一个这样的体积是为树的分支的每个可能的直径计算的，这需要很多时间。随着树变得更高，并且[树形支撑分支直径角度](support_tree_branch_diameter_angle.md)的值较大，可能的分支直径数会显著增加。因此，直径将舍入为此分辨率设置的最接近倍数。但是，在树高度上的某些点，分支需要避免的碰撞体积会捕捉到分支直径的下一个采样，从而突然为分支提供更多的移动空间。这将使树显示为锯齿状。

增加此设置将使切片在Cura中花费的时间更少。它还将使支撑件更加锯齿状，这损害了其强度，增加了支撑件在打印期间断裂的可能性，这可能导致打印失败。
