screw_distance = 14;
screw_radius = 1.5;
calendar_radius = 15.2; //Has 0.2mm play!

width = screw_distance + 10;
height = 20;
thickness = 2;
$fs = 0.1;
$fa = 1;

//Base plate with screw holes.
difference() {
	cube([width, height, thickness]);
	translate([width / 2 - screw_distance / 2, height / 2, 0]) {
		cylinder(r=screw_radius, h=thickness);
	}
	translate([width / 2 + screw_distance / 2, height / 2, 0]) {
		cylinder(r=screw_radius, h=thickness);
	}
}

//Side struts.
translate([0, 0, thickness]) {
	intersection() {
		rotate([-45, 0, 0]) {
			cube([thickness, height * sqrt(2), height * sqrt(2)]);
		}
		cube([thickness, height, height]);
	}
}
translate([width - thickness, 0, thickness]) {
	intersection() {
		rotate([-45, 0, 0]) {
			cube([thickness, height * sqrt(2), height * sqrt(2)]);
		}
		cube([thickness, height, height]);
	}
}

//Resting plate.
translate([width / 2 - calendar_radius - thickness, height, 0]) {
	difference() {
		union() {
			cube([(calendar_radius + thickness) * 2, thickness * 2, calendar_radius + thickness]);
			translate([calendar_radius + thickness, 0, calendar_radius + thickness]) {
				rotate([-90, 0, 0]) {
					difference() {
						cylinder(r=calendar_radius + thickness, h=thickness * 2);
					}
				}
			}
		}
		translate([calendar_radius + thickness, thickness, calendar_radius + thickness]) {
			rotate([-90, 0, 0]) {
				cylinder(r=calendar_radius, h=thickness + 1);
			}
		}
	}
}