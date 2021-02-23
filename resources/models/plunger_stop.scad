//This is a simpler re-implementation of a block that was originally designed to
//stop a plunger in a pinball machine while still passing on the momentum to the
//pinball.
//The original design had a lot of globals and overly complex file structure which
//is useful for a big project like that. This file is greatly simplified to be
//standalone.

width = 40;
height = 25;
depth = 25;
inner_curve = 10;
$fs = 0.2;
$fa = 1;

difference() {
	translate([-width / 2, 0, 0]) {
		cube([width, depth, height]);
	}
	translate([0, -1, height / 2 - 1]) {
		rotate([-90, 0, 0]) {
			cylinder(r=height / 2 - 1, h=depth / 5 + 1);
			translate([0, 0, depth / 5 + 1]) {
				cylinder(r1=height / 2 - 1, r2=height / 6, h=depth * 4 / 5 + 1);
			}
		}
	}
	hull() {
		translate([-width / 2, depth + inner_curve, -1]) {
			cylinder(r=inner_curve, h=depth + 2);
		}
		translate([width / 2, depth + inner_curve, -1]) {
			cylinder(r=inner_curve, h=depth + 2);
		}
		translate([0, depth * 2/3 + inner_curve, -1]) {
			cylinder(r=inner_curve, h=depth + 2);
		}
	}
	translate([-width - 1, 0, depth]) {
		rotate([-5, 0, 0]) {
			cube([width * 2, depth * 2, height]);
		}
	}
}