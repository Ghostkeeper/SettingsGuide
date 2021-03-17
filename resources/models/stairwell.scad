thickness = 5;
steps = 10;
height = 30;
width = 20;
$fs = 0.2;
$fa = 1;

translate([thickness / 2, thickness / 2, 0]) {
	cylinder(r=thickness / 2, h=height);
}

intersection() {
	union() {
		translate([thickness / 2, thickness / 2, 0]) {
			for(step = [0:steps]) {
				rotate([0, 0, 90 / steps * step]) {
					translate([0, -thickness / 2, height / (steps + 2) * (step + 1)]) {
						cube([width + thickness, thickness, height / (steps + 2)]);
					}
					translate([width, -thickness / 2, 0]) {
						cube([thickness, thickness, height / (steps + 2) * (step + 2)]);
					}
				}
			}
		}
	}
	cylinder(r=width + thickness * 1.5, h=height);
}