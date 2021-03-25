$fs = 0.2;
$fa = 1;

difference() {
	hull() {
		cube([30, 20, 3]);
		translate([-7, 10, 0]) {
			cylinder(r=3, h=3);
		}
		translate([37, 10, 0]) {
			cylinder(r=3, h=3);
		}
	}
	translate([-4, 10, -1]) {
		cylinder(r=1.5, h=5);
	}
	translate([34, 10, -1]) {
		cylinder(r=1.5, h=5);
	}
}
translate([28, -13, 3]) {
	rotate([0, -90, 0]) {
		rotate_extrude(angle=90) {
			translate([15, 0, 0]) {
				difference() {
					square([16, 26]);
					translate([1, 1, 0]) {
						square([14, 24]);
					}
				}
				translate([8, 13, 0]) {
					circle(r=1);
				}
			}
		}
	}
}
translate([15, -12.5, 18.5]) {
	cylinder(r=0.5, h=15);
}
translate([15, -13, 26]) {
	sphere(r=1);
}