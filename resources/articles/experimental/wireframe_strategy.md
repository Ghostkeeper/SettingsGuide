The most critical concern for the reliability of Wire Printing is the connection points where the layers of the frame connect to each other. There are several strategies available for making these connections stronger. This setting allows you to choose the strategy that the printer will be using.

Compensate
----
When using this strategy, the printer will try to compensate for sagging factors in the material. Because the material comes molten out the nozzle, it will fall down a bit before it's solidified and will be dragged along with the motions of the nozzle. This strategy deforms the saw-tooth pattern that connects the layers of the frame such that it hopefully ends up in the correct location again.

Two compensation factors are available: One that deforms the saw-tooth pattern only vertically to [compensate for sagging](wireframe_fall_down.md), and one that deforms the saw-tooth pattern in a diagonal direction to [compensate for the material being dragged along](wireframe_drag_along.md) with the nozzle.

Knot
----
When this strategy is selected, a little upwards and backwards motion will be made at the top of each saw tooth to form a "knot" of material there. The purpose of the knot is to give the horizontal ring on top of it some area to attach to the saw-tooth pattern. The knot will vary a little bit from side to side, so if the horizontal ring is not placed down very accurately there is still a bigger chance that they attach to each other. Also, the knot will make the upward line extend slightly further upwards, causing the horizontal ring to be pushed on top of it. And lastly, the knot will also produce some oozing due to the lack of retraction in this travel move. This produces a blob on which the horizontal ring can rest better.

![Where the knot is drawn and what its size entails](images/wireframe_top_jump.svg)

The motion for this "knot" is a series of travel moves:
1. First, the nozzle will move upwards and backwards slightly.
2. If there is any [delay](wireframe_top_delay.md) in the top, the nozzle will pause for the set amount of delay. This pause is done in the tip of the knot's motion.
3. Third, the nozzle will move back down to the ordinary height. At the same time, the nozzle will move forward and away from the vertical line.

Retract
----
When this strategy is selected, the material will be retracted after every upwards motion while printing the saw-tooth pattern. The idea is that by retracting the material, the wire is broken off. This reduces the effect that the material is dragged along with the movement of the nozzle, because the previous line is no longer attached to the nozzle. Afterwards, the nozzle makes a small hop of 1 millimetre and continues with the diagonal movement down towards the lower layer.

One major disadvantage of this strategy is that the diagonal downwards line is also not attached any more. This effectively makes the extrusion during that line useless. The material simply ends up as a blob on the lower layer. The material is also subject to more grinding as the material is retracted back and forth without much extrusion in between. That all takes a lot of time as well.