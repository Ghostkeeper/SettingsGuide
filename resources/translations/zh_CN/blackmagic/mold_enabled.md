模具
====
取代打印模型本身，这个功能会导致打印机创建一个模型的负像，一个模具，你可以使用不同的材料来铸造一个模型。该模具具有几个特定的特性，使其既可用于铸造，又可用于FFF打印。这允许进行[快速铸造](https://en.wikipedia.org/wiki/Rapid_casting)过程。

<!--screenshot {
"image_path": "mold_enabled_shell.png",
"models": [{"script": "stature.scad"}],
"camera_position": [-78, 160, 228],
"layer": -1
}-->
<!--screenshot {
"image_path": "mold_enabled_mould.png",
"models": [{"script": "stature.scad"}],
"camera_position": [-78, 160, 228],
"settings": {
"mold_enabled": "True"
},
"colours": 32
}-->
![您想要铸造的模型](../images/mold_enabled_shell.png)
![该模型的模具](../images/mold_enabled_mould.png)

Cura的模具生成将创建一个具有您想要铸造的确切形状的中空体。在这个空心周围，将生成一个具有特定宽度的壳，可通过[最小模具宽度](mold_width.md)进行配置。在模具的上方和下方，将生成具有特定高度的皮肤，可通过[模具顶板高度](mold_roof_height.md)设置进行配置。然而，这个皮肤不会在模型的顶部生成，这样你就可以在那里浇注材料。它也不会在模型的最底部生成。也就是说，你将在铸造过程中将它保持在构造板上。

设计您的模具
----
Cura的模具生成并不完美。少了几样东西。这里有一些技巧来解决它们。
* Cura不会为模型中的所有局部最大值创建浇口。需要在模型中需要浇口位置添加垂直杆。
* Cura不允许额外的材料被铸造，以防你的材料在冷却时收缩。如果使用的材料收缩很大，甚至需要在模型的最高点添加额外的浇口。
* Cura的模具总是完整的。对于许多形状，这意味着模具需要被破坏以便移除它。模具可以用各种方法破坏；如果里面的材料允许的话，可以直接使用外力或通过加热，或者通过使用像PVA这样的水溶材料。
* Cura不允许放入杆或线来加强模具。要实现这一点，请在模型中放入额外的杆，以便Cura为它们留下空腔，然后插入杆或线。
* 在模具中生成底切时没有任何警告。如果你的铸件需要大量的底切，你将需要一些浇口或其他渠道，让材料正确地流入那里，并使空气出来。此外，要知道，一旦材料凝固模具可能需要被摧毁来获得铸造件。

用于打印模具的材料
----
理想的模具是：
* 非常僵硬
* 耐高温
* 化学惰性，这样就不会粘到你的铸造材料上
* 由不会收缩的材料制成

此外，一些模具需要被破坏，以获得模型。为此，您可以选择脆性材料或可以用水或其他化学品溶解的材料，如PVA。

铸造材料
----
有许多不同类型的材料可用来铸造模具。有些比其他人更适合3D打印模具。以下是一些可能有效的材料示例：
* ** 硅胶 **。硅树脂不会与塑料结合，因此很容易去除。硅树脂也是非常灵活的，这使得它宽容底切。更重要的是，有机硅是热固性和耐热的，所以你也可以考虑在模具凝固后将其熔化。但是需要一些特殊的工具来铸造硅树脂。特别是，你需要一个真空室来抽出硅胶中的气泡。
* ** 沙子 **。沙子是制作模具的行业标准，因为它非常耐热，但不需要加热就可以铸造。铸造后，你可以用混凝土或胶水将其粘合起来，以防止它散架。然后你可以用它来制作另一个更耐热的材料。
* ** 灰泥 **。类似于沙子，但通常由更细的颗粒组成。这具有的优点是，结合剂已经包括在材料中，因此不需要粘合它。但是，这可能导致更脆的最终结果。
* **蜡**。为了制作定制蜡烛或小雕像，您可以用蜡铸造模型。蜡的熔化温度低，所以它不会熔化模具。它也不会与塑料结合，使其更容易从模具中释放。蜡的延展性很好，从模具中取出后很容易修改。如果用这个制作定制蜡烛，别忘了在它设置之前插入灯芯。
* ** 巧克力 **，作为特别定制的款待或礼物。要浇铸巧克力，先将其融化到略高于熔点，然后倒入模具中，稍微振动一下以排除气泡，然后立即放入冰箱。你甚至可以把模具放在冰箱里的冷水浴中，以更快地减少热量。5分钟后，将巧克力小心地从模具中取出。

FFF打印只能与热塑性塑料一起工作。热塑性塑料是在高温下固有地变软的塑料。这与铸造时是热的铸造材料不兼容。一些通常与3D打印模具不兼容的材料：
* ** 金属 **，需要加热到塑料的熔点以上才能变成足够的液体以进行铸造。金属的热量会使模具熔化。
* ** 塑料粘合 ** 到制作模具的材料。铸造后你无法将模具与模型分离。你可以喷一些脱模剂进去，但如果材料太相似，它仍然会永久地粘在模具上。
* ** 材料收缩 ** 凝固后收缩过多。只要你有足够长的浇口让新的材料填充腔体，材料在凝固前收缩是可以的。
* ** 环氧树脂 ** 是不合适的，因为树脂在浇铸时是冷的，两种成分的化学反应释放出足够的热量会将塑料熔化。环氧树脂也倾向于非常好地粘在塑料上。

如果您需要在与3D打印不直接兼容的材料中创建对象，则需要在多个铸造阶段中工作。每个阶段都创建前一阶段的负像。例如，您可以正常打印对象的形状（禁用此设置），然后通过将模具放入灰泥浴中来创建负像。由于灰泥更耐热，因此您可以使用需要加热到更高温度才能熔化的材料，如青铜，或与塑料结合的材料，如环氧树脂。

铸造工艺
----
使用3D打印模具铸造在很大程度上与任何其他模具相同，并且在很大程度上取决于所涉及的材料。不过，在3D打印模具方面有几点需要特别注意。

您打印模具所用的热塑性塑料具有较低的热容量，并且可能具有相当低的玻璃化转变温度。这意味着在模具铸造之后，时间是至关重要的。如果材料冷却得太慢，模具可能会变软。这可能导致模具变形，并使其更难脱模。为了加速铸件的凝固，你可以把它浸在冰浴中。

由于层之间的边界，3D打印模具还沿着其侧面具有更多的脊。这使得从铸件中释放模具变得更加困难。如果你在模具和铸件之间使用脱模剂，使用一些可以填充这些间隙的东西。薄的润滑剂是不够的。更合适的界面层是蜡或更厚的润滑剂。