Support Brim Line Count
====
This setting adjusts the number of contours that will be drawn inside the support area for the support brim. With more lines, the brim will become wider.

<!--screenshot {
"image_path": "support_brim_2mm.png",
"models": [{"script": "gazebo2.scad"}],
"camera_position": [-74, 38, -137],
"settings": {
    "support_enable": true,
    "support_use_towers": false,
    "support_brim_enable": true,
    "support_brim_width": 2
},
"colours": 64
}-->
<!--screenshot {
"image_path": "support_brim_4mm.png",
"models": [{"script": "gazebo2.scad"}],
"camera_position": [-74, 38, -137],
"settings": {
    "support_enable": true,
    "support_use_towers": false,
    "support_brim_enable": true,
    "support_brim_width": 4
},
"colours": 64
}-->
![5 brim lines](../images/support_brim_2mm.png)
![10 brim lines](../images/support_brim_4mm.png)

More brim lines will increase the adhesion of the support to the build plate and reduce warping of support. As a result, the support will stand more sturdily, which improves reliability of the print.