微小特征最大长度
====
打印件的小细节通常对尺寸要求很高。此设定会使打印中的小孔打印速度变慢，以达到更高的精确度。

如果打印件中孔的周长小于此设置所指示的值，则打印该孔的周长的速度将乘以 [微小特征速度](small_feature_speed_factor.md) （通常是减小的）的系数。此设置是处理[小孔最大尺寸](small_hole_max_size.md) 设置的另一种方法，该设置比仅用于圆孔的设置更通用。

此功能的一个常见使用案例是以非常精确的尺寸打印螺孔。在打印小孔的过程中，液滴倾向于与喷嘴一起被拉入角落。如果拐角非常尖锐（例如小孔），则这会使孔变小。当打印更慢时，由于材料有更多的时间来稳定，并且由于机械拉力更低，所以该拉力减小。

增加此设置会导致更多的轮廓被标记为"小要素"。打印中的孔的较大部分将打印较慢。这会使这些孔打印得更精确，但会增加打印时间。