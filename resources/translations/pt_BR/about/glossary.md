Glossário
====
Esta página explica alguns dos termos do setor empregados pela Cura.O Cura nem sempre é o mais consistente quando se trata de uso da terminologia; portanto, alguns termos são sinônimos.

* **Adaptive layers:** A technique that varies the layer height across the print to reduce the visibility of topology while still printing reasonably fast.
* **Aliasing:** A print defect where the resolution limit of the stepper motors is visible on the outside of the print.
* **Anti-overhang mesh:** A model that will prevent support from being generated to support any overhang that the model overlaps with. Synonym of "support blocker".
* **Bead:** A strand of material after it's been placed down by the extruder train. The term "bead" is used in science where it's important to consider the actual shape of the strand of filament after it's been solidified. Similar to "line".
* **Blob:** A dot of excess material on the outside of the print.
* **Bowden tube:** A hollow, flexible tube used to guide the filament through the extruder train.
* **Bridging:** A technique to print overhanging lines in mid-air, by stretching straight lines between two resting points. Cura can adjust the parameters of bridging lines and will adjust the direction of some lines to create bridges.
* **Brim:** A rim of material, attached to the print, that acts like a skirt but also attaches the print better to the build plate by providing more surface area for the material to stick.
* **Build plate:** The plate where the print is being placed on while it's being constructed. Some build plates are heated to make the material stick better while the print is ongoing.
* **Build volume:** The 3D space where the printer can reach to extrude material.
* **Coasting:** A technique where the last part of an extrusion path is printed with 0% flow, draining the nozzle from its overpressure.
* **Combing:** A movement that tries to avoid crossing walls during travels, to prevent creating a visible scar on the outside of the print.
* **Coordinate origin:** The location on the build plate where a nozzle would move if instructed to move to coordinates [0, 0, 0].
* **CuraEngine:** A program that Cura uses to do the heavy lifting of the slicing process. Converts 3D models into g-code.
* **Cutting mesh:** A model on the build plate that can change settings for the part of its volume that overlaps with actual printed models. The model itself is not printed, but it cuts out pieces of other models and can then change the settings or extruder with which those parts are printed.
* **Disallowed area:** A location on the build plate where you're not allowed to place a model for printing. For instance, because it would hit clips holding down the bed, the prime tower, or because your print would have auxiliary parts that would go out of the build volume.
* **Draft shield:** A shell of material being printed around the object that keeps the temperature around the print consistent.
* **Elephant's foot:** A print defect where the bottom side of the print is slightly wider than desired.
* **Extruder:** The feeder, optional Bowden tube, heat zone, hot end and nozzle together. Some printers have multiple extruders or have more than one of some parts of the extruder train. Short for "extruder train".
* **Extruder switch:** Typically only one of the extruders is active at a time. An extruder switch is when it changes the active extruder from one extruder to another.
* **Extruder train:** The feeder, optional Bowden tube, heat zone, hot end and nozzle together. Some printers have multiple extruder trains or have more than one of some parts of the extruder train.
* **Extrusion:** The act of pushing filament through the extruder train such that material comes out of the nozzle, which is hopefully deposited in the correct place to form the print.
* **Face:** A flat surface of a 3D mesh. With triangular meshes (the only kind Cura can process), all faces are triangles in 3D space.
* **Fan:** Not just any fan of the printer, but specifically the fan(s) attached to the print head that cool down the print just after the material has been extruded.
* **FDM printing:** Fused Deposition Modelling. A type of 3D printing done by extruding lines of plastic in a certain shape. This is the only technique of 3D printing that Cura supports. Synonym of "FFF printing".
* **Feeder:** A motor and gearbox that pushes or pulls the filament through the extrusion train.
* **Feedrate:** The speed at which filament is fed into the extruder train.
* **FFF printing:** Fused Filament Fabrication. A type of 3D printing done by extruding lines of plastic in a certain shape. This is the only technique of 3D printing that Cura supports. Synonym of "FDM printing".
* **Filament:** A rope of plastic being fed into the 3D printer. Comes on spools. Once it's been extruded, it's not filament any more but just material.
* **Flow:** The rate of extruding material as ratio of its normal rate. More than 100% flow theoretically extrudes more material than would fit in the allotted volume. Less than 100% flow theoretically extrudes too little material.
* **Gantry:** The mechanical frame that moves the print head around the build volume.
* **Gap filling:** A technique used by Cura to fill small gaps in the print with material using very tiny line segments.
* **Gradual infill:** A technique where the amount of material is reduced in lower parts of a volume, but still high in higher parts to support the material above it properly. This is not only used for material but also for support.
* **Hardness:** A measure of a print to how much it can resist elastic deformation or puncturing.
* **Heater:** A heating element that brings the filament to the temperature required for 3D printing.
* **Heat zone:** The zone where the filament is heating up while going towards the nozzle. At the beginning of the heat zone the filament is at room temperature. At the end it is at printing temperature.
* **Hop:** A technique where the nozzle is moved up (+Z) in order to travel over the print with a bit of clearance. Synonym of "Z hop".
* **Hot end:** The hot metal or ceramic bit containing the nozzle, heating element and temperature sensor.
* **Infill:** A structure created on the inside of a print that holds up the top skin and provides additional strength to the print.
* **Infill mesh:** Similar to "cutting mesh", but only applies where it overlaps with the infill volume of another model. This is a model that adjusts settings for infill of another model.
* **Inner walls:** All of the walls except the outermost wall. While a part on a layer has only one outer wall, it may have any number of inner walls.
* **Inset:** An operation on polygons that produces a smaller/thinner polygon, whose contour keeps a certain distance from the contour of the original polygon. An inset with a negative distance is called an "offset".
* **Ironing:** A technique that passes over the top surface an additional time to make it extra smooth.
* **Jerk:** A limit on the amount of instantaneous change in velocity applied at the start of every move. This is not the same as the common definition of "jerk" in physics!
* **Layer:** 3D printing is done in thin layers of material. These layers are 2D shapes with a certain thickness, which when stacked vertically form a 3D print.
* **Layer shift:** A print defect where the horizontal position of a layer is unintentionally shifted, typically shifting the rest of the print too.
* **Layer split:** A print defect where the layers don't stick together well enough and crack open.
* **Line:** A strand of material after it's been placed down by the extruder train. In Cura, lines are modelled as being rectangular blocks with a certain width, thickness (layer height) and length. Similar to "bead".
* **Line segment:** To disambiguate with the 3D printing term "line", when referring to a line segment in a mathematical sense Cura will always use the full term "line segment" to indicate a straight geometrical line of limited length.
* **Material:** The material that your 3D print consists of. Typically a thermoplastic in FFF printing.
* **Mesh:** A collection of triangles that together forms a model. Although sometimes used as synonym of "object" and "model", typically this is used in the context of a piece of data rather than something you'd want to print.
* **Model:** A 3D model loaded into the 3D scene of Cura (before slicing). Synonym of "object".
* **Nozzle:** The opening where the printing material exits the extruder train.
* **Object:** A 3D model loaded into the 3D scene of Cura (before slicing). Synonym of "model".
* **Offset:** An operation on polygons that produces a larger/fatter polygon, whose contour keeps a certain distance from the contour of the original polygon. An offset with a negative distance is called an "inset".
* **One-at-a-time mode:** A mode of printing multiple objects where each object is completed fully before continuing with the next object, whereas normally it prints a layer for each object before continuing with the next layer.
* **Ooze shield:** A shell of material being printed around the print that catches any oozed material when a travel moves the nozzle towards the print.
* **Oozing:** Leaking material out the nozzle while it's not intended to. Typically this leaves a string of material along the travel path.
* **Outer wall:** The outermost wall. There is only one outer wall per part per layer.
* **Overextrusion:** Extruding too much material in a limited volume, causing the material to spill over to where it's not supposed to go.
* **Overhang:** A part of the print that is not (or not completely) supported by material in the layers below it. If the overhang is too extreme to print well, support or bridging is necessary.
* **Overpressure:** While printing, the nozzle chamber is kept at great pressure to ensure that the material is extruded consistently.
* **Parking:** The act of pausing the print for a moment while the nozzle is away from the print, to allow the material some time to cool down.
* **Part:** A continuous shape (polygon) on a single layer. A single model may split up into multiple parts on certain layers, when sliced.
* **Pattern:** A technique of filling a volume with material, although not necessarily at 100% density. Cura provides choice between several patterns such as lines, grid, concentric, tetrahedral, etc.
* **Pillowing:** A print defect where the top skin bulges or breaks up in between where it rests on the infill lines below.
* **Polygon:** A 2D shape or closed loop consisting of a series of points with straight line segments between them.
* **Prime blob:** A blob of material being purged at the start of a print to prime an extruder.
* **Prime tower:** A structure created besides the print that allows the printer to prime its nozzles on higher layers without the excess material ending up on the side of the actual print. Used for prints where multiple extruders are involved to prime an extruder after being on stand-by for a while.
* **Priming:** The act of purging some material to ensure that the filament is aligned to the nozzle tip and the nozzle chamber is filled and pressurised correctly. Usually done at the start of a print or after an extruder switch.
* **Purging:** The act of extruding some material as waste. A common reason for purging is "priming".
* **Raft:** A technique to improve build plate adhesion by printing a solid plate underneath your print that is later discarded. The plate has a lot of surface area and is printed with thick lines that stick well, and catches any irregularities in the flatness of the build plate.
* **Retraction:** The act of using the feeder to pull the material back into the nozzle chamber. Usually done to temporarily stop the material from flowing out the nozzle to make a clean travel.
* **Ringing:** A print defect where the surface wobbles due to inconsistent extrusion or wobbling of the nozzle. Typically happens after making sharp corners too fast.
* **Scar:** A spot of damage on the outside of the print where the nozzle melted down the material in passing.
* **Seam:** The location where a closed loop starts and stops. This spot is usually visible on the final print, so you'd like to position it in a spot where it's not very visible.
* **Shell:** Both the walls and the skin.
* **Skin:** The top and bottom sides of the print. These are always printed at 100% density, typically with the lines pattern. Synonym of "top/bottom".
* **Skirt:** A contour drawn around the print on the first layer to both prime the material and to allow the user to see whether the build plate is completely level.
* **Slicing:** The process of converting a 3D model into instructions for a 3D printer to print it. Within the context of CuraEngine, this is also sometimes used for the process of creating cross-sections of the model, which is one of the stages of the complete slicing process.
* **Spiralise mode:** A mode to print only the outline of the models, typically while gradually increasing the Z coordinate throughout the layer to eliminate the Z seam by printing the model in one great spiral. Outside of Cura this is also known as "vase mode".
* **Stand-by:** When printing with multiple extruders, typically only one of the extruders is active at a time. The other extruders will be on stand-by.
* **Stitching:** A part of the slicing process. Creating cross sections of a group of triangles results in a bunch of line segments on each layer. Stitching combines those line segments into polygons and determines what the inside of the layer is.
* **Strength:** Encompassing term indicating various measures of resistance to movement, including hardness, stiffness and toughness when various types of force are being applied.
* **Stringing:** When travelling while oozing material, this creates thin strands of material called "stringing". The strands don't necessarily span all the way across the length of a travel move. A less extreme form of this results in "blobs".
* **Support:** A part of the print that is removed after printing, but was necessary to keep parts of the print in place while the print was still ongoing, to prevent material from falling down or wobbling too much.
* **Support blocker:** A model that will prevent support from being generated to support any overhang that the model overlaps with. Synonym of "anti-overhang mesh".
* **Support floor:** The bottom side of the support, used where the support rests on the model. This part of support can optionally be printed with different settings. There is no support floor where the support rests on the build plate.
* **Support infill:** The main component of support. If there is no support interface, the support consists only of support infill.
* **Support interface:** The support roof and floor, where the model rests on the support and where the support rests on the model. The bottom side of support where the support rests on the build plate does not get support interface.
* **Support mesh:** A model that is being filled with support structure, instead of printing as a normal print. Can be used to customise the shape of your support.
* **Support roof:** The top side of the support, used where the model rests on the support. This part of support can optionally be printed with different settings.
* **Support towers:** A technique to support very thin or small parts of the print. The part is supported by the tip of a tower that gets wider further down so that the support doesn't topple while being printed.
* **Thermoplastic:** A type of plastic that becomes soft when melting. Only thermoplastics can be used for FFF Printing.
* **Thickness:** The size of some structure in the vertical direction (Z). Compare with "width".
* **Top/bottom:** The top and bottom sides of the print. These are always printed at 100% density, typically with the lines pattern. Synonym of "skin".
* **Top surface:** The highest part of the top skin. Rarely more than 1 layer, this top surface can be printed with separate settings to achieve greater quality without costing a lot of extra printing time.
* **Topography:** The effect where the limited layer height turns an almost-flat surface into something that resembles a geographical height map with rings where the layers end.
* **Toughness:** A measure of a print as to how much it can resist plastic deformation.
* **Transition (of walls):** The place where different number of walls come together to make the part thinner or thicker using a different number of walls in some parts than in others.
* **Travel (move):** Moving the nozzle from one place to another without extruding material.
* **Underextrusion:** Extruding too little material to properly fill a volume or to properly create strong and continuous beads.
* **Underpressure:** While retracted, the nozzle chamber is kept at a negative pressure, to suck the material inside, preventing oozing.
* **Vase mode:** A mode to print only the outline of the models, typically while gradually increasing the Z coordinate throughout the layer to eliminate the Z seam. Cura always calls this "spiralise mode".
* **Walls:** The sides of the print. They loop around the model horizontally.
* **Warping:** Deformation of the print after printing, due to the material shrinking or due to internal stresses pulling on the material while it's not yet solidified.
* **Width:** The size of some structure in the horizontal direction (X/Y). Compare with "thickness".
* **Winding order:** The order of points forming a polygon. Either clockwise or counter-clockwise. In Cura, a counter-clockwise winding order indicates a positive shape while a clockwise winding order indicates a hole. The input 3D models must have triangles with counter-clockwise winding order when seen from the outside.
* **Wiping:** A technique to make the nozzle cross a previously printed structure on purpose to wipe off any dangling oozed material from the nozzle tip, to prevent that material from being placed on the outside of the print.
* **Wire printing:** A technique to print a model by only printing a wireframe around its shell. Highly experimental.
* **Z seam:** A visible spot on the outer wall where the nozzle moved from one layer to the next. Often incorrectly used instead of just "seam".
* **Z hop:** A technique where the nozzle is moved up (+Z) in order to travel over the print with a bit of clearance. Synonym of "hop".