length = 60;
width = 20;
height = 40;
thickness = 6;
leg_thickness = 1;
arc_height = 9; //Extra height at which the bottom arc starts.
arc_radius = length * 2;
arc_thickness = 22;
curve_radius = height / 2;
$fs = 0.4;
$fa = 1;

difference() {
	//Main volume we're carving from.
	cube([length, width, height]);

	intersection() {
		union() {
			//Top arc.
			translate([length / 2, -1, arc_radius + arc_height + arc_thickness - (1 - cos(asin((length / 2 - thickness) / arc_radius))) * arc_radius]) {
				rotate([-90, 0, 0]) {
					cylinder(r=arc_radius, h=width + 2);
				}
			}
		}
		translate([thickness, -2, -1]) {
			cube([length - thickness * 2, width + 4, height + 2]);
		}
	}

	//Arc sides.
	translate([thickness, -1, 0]) {
		cube([length - thickness * 2, (width - thickness) / 2 + 1, height]);
	}
	translate([thickness, (width + thickness) / 2, 0]) {
		cube([length - thickness * 2, (width - thickness) / 2 + 1, height]);
	}

	//Side legs.
	translate([-1, width / 2, 0]) {
		rotate([45, 0, 0]) {
			rotate([0, 90, 0]) {
				cylinder(r=width / 2 - leg_thickness, h=length + 2, $fn=4);
			}
		}
	}
	translate([-1, width / 2, height]) {
		rotate([0, 90, 0]) {
			cylinder(r=width / 2 - leg_thickness, h=length + 2);
		}
	}

	//Curves.
	translate([-1, -curve_radius + (1 - cos(asin((height / 2 - thickness) / curve_radius))) * curve_radius, height / 2]) {
		rotate([0, 90, 0]) {
			cylinder(r=curve_radius, h=length + 2);
		}
	}
	translate([-1, width + curve_radius - (1 - cos(asin((height / 2 - thickness) / curve_radius))) * curve_radius, height / 2]) {
		rotate([0, 90, 0]) {
			cylinder(r=curve_radius, h=length + 2);
		}
	}
}