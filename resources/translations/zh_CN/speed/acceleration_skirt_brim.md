Skirt/Brim 加速度
====
此设置控制打印Skirt/Brim时喷嘴加速到不同方向的速度。brim/skirt期间的加速度可以被设置为与其他部分不同的速率。即使Skirt和brim始终是初始层独有的，此设置也会覆盖[起始层打印加速度](acceleration_print_layer_0.md)设置。它们是使用通过此设置确定的加速度打印的，而不是通常使用初始层的设置。

Brim对于床粘附是至关重要的，因此在Brim的打印期间降低加速度速率可以在Brim被打印时减少振动，并且对构造板的粘附更好，以较小的打印时间成本增加Brim的有效性。

加速度对Skirt/Brim的影响通常非常小，因为它们由具有平滑曲线的线条组成。加速度通常完全由[Skirt/Brim抖动速度](jerk_skirt_brim.md)控制。
