构造板温度
====
一些打印机有可加热的构造板。此设置确定构造板的温度。

加热构造板将略微的保持材料的粘性和流动性。一些材料在冷却时将形成晶体，这导致材料在冷却中显著收缩。热床使材料保持在略高于冻结温度，以防止这种收缩并保持液体塑料的粘性。这都是为了改善打印件对构造板的粘附性。

然而，如果构造板温度太高，则打印件在其接触构造板的地方很容易流动。这会导致材料略微下垂，从而在打印的底面产生[象脚](../troubleshooting/elephants_foot.md)。可以通过[起始层水平扩展](../shell/xy_offset_layer_0.md)进行补偿，但会影响尺寸精度。加热构造板还将在其上的材料与模型中较高的材料之间产生温差，当较高的材料开始收缩时，这会导致[翘曲](../troubleshooting/warping.md)。

如果设置为0度，Cura将不会输出任何命令来变更构造板温度，没有构造板的机器可能会混淆固件。

**在材料配置文件中调整构造板温度时，将调整[构造板默认温度](default_material_bed_temperature.md)的设置。通常，“构造板温度”等于“构造板默认温度”，但有时选择不同的质量可以对构造板温度进行轻微调整。此构造板温度设置实际上用于打印。**