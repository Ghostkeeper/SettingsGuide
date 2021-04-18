//Settings
prongs = 7;
stakes = 4;
line_width = 0.9;
radius = 20;
height = 0.9;

//Calculations.
riblength = 2 * radius * sin(180 / prongs);

for(prong = [0:prongs]) {
	rotate([0, 0, prong / prongs * 360]) {
		translate([-line_width / 2, -line_width / 2, 0]) {
			cube([radius, line_width, height]);
			for(stake = [1:stakes]) {
				translate([radius * stake / stakes - line_width / 2, 0, 0]) {
					rotate([0, 0, 180 / prongs]) {
						cube([line_width, riblength * stake / stakes, height]);
					}
				}
			}
		}
	}
}