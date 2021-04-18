fillet = 2;
$fs = 0.3;
$fa = 1;

difference() {
	minkowski() {
		union() {
			translate([fillet, fillet, 0]) {
				cube([30 - fillet, 30 - fillet * 2, 10 - fillet]);
			}
			translate([30, 15, 0]) {
				cylinder(r=15 - fillet, h=10 - fillet);
			}
			hull() {
				translate([fillet, fillet, 0]) {
					cube([25 - fillet * 2, 10 - fillet * 2, 10 - fillet]);
				}
				translate([10, fillet, 20]) {
					rotate([-90, 0, 0]) {
						cylinder(r=10 - fillet, h=10 - fillet * 2);
					}
				}
			}
			hull() {
				translate([fillet, 20 + fillet, 0]) {
					cube([25 - fillet * 2, 10 - fillet * 2, 10 - fillet]);
				}
				translate([10, 20 + fillet, 20]) {
					rotate([-90, 0, 0]) {
						cylinder(r=10 - fillet, h=10 - fillet * 2);
					}
				}
			}
		}
		sphere(r=fillet);
	}
	translate([0, 0, -fillet - 1]) {
		cube([45, 30, fillet + 1]); //Cut off the fillet from the bottom side, making it flat.
	}
	translate([10, -1, 20]) {
		rotate([-90, 0, 0]) {
			cylinder(r=5, h=6, $fn=6);
			translate([0, 0, 26]) {
				cylinder(r=5, h=6, $fn=6);
			}
			cylinder(r=2.5, h=32);
		}
	}
	translate([30, 15, -1]) {
		cylinder(r=2.5, h=12);
		translate([0, 0, 6]) {
			cylinder(r1=2.5, r2=5, h=5);
		}
	}
}