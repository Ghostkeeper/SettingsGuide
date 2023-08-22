冲洗清除速度
====
如果打印机需要切换线材通过某个喷嘴，它需要先冲洗掉仍在喷嘴室中的剩余材料。此设置确定线材通过进料器以清除旧材料的速度。

这仅适用于切换到不同类型的材料之后。如果重新装载相同类型的材料（例如因为前一个线轴是空的），则使用[不同的速度](material_end_of_filament_purge_speed.md)。

**此设置目前在Cura的界面中不可见。它只能由配置文件设置。Cura在切片期间也不使用它。但是，了解Cura材料文件格式的打印机可以使用它来正确配置线材切换程序。**通过后处理脚本，可以在打印中插入`M600`命令，这将触发线材切换。