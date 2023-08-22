模糊皮肤
====
使用模糊皮肤打印时，打印的侧表面会故意弄得粗糙。这使打印件具有各种纹理。

<!--screenshot {
"image_path": "magic_fuzzy_skin_enabled.png",
"models": [{"script": "hexasphericon.scad"}],
"camera_position": [-61, 112, 136],
"settings": {
"magic_fuzzy_skin_enabled": true
},
"colours": 32
}-->
![墙壁在Cura的图层视图中看起来颤颤巍巍](../images/magic_fuzzy_skin_enabled.png)
![打印结果呈现粗糙纹理](../images/magic_fuzzy_skin_photo.jpg)

此模式会将随机抖动添加到外壁。打印头在打印最外壁时将随机振动。这会使表面摸起来粗糙。表面仅在打印件的侧面模糊。不向顶部添加模糊度。

模糊性将所有的尺寸精度抛到了九霄云外。打印肯定会比原来的型号大。由于打印头在打印外壁时受到很大的加速度，因此，模糊皮肤也会使打印花费更长的时间。
