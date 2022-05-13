include <fillet.scad>

difference() {
	union() {
		fillet(r=2, steps=30) {
			difference() {
				cylinder(h=9, r=14, $fn=30);
				translate([0, 0, -1]) {
					cylinder(h=11, r=12.85, $fn=29);
				}
				translate([0, -15, 24]) {
					rotate([-90, 90, 0]) {
						cylinder(h=30, r=20);
					}
				}
				translate([0, -15, 4]) {
					cube([15, 30, 10]);
				}
			}
			translate([-10.9, -9.1, 0]) {
				cylinder(h=9, r=1.5, $fn=30);
			}
			translate([-10.9, 9.1, 0]) {
				cylinder(h=9, r=1.5, $fn=30);
			}
		}
		translate([-13.5, 0, 0]) {
			scale([1, 3, 1]) {
				cylinder(h=9, r=5, $fn=60);
			}
		}
	}
	translate([-13.5, -10, -1]) {
		cylinder(h=11, r=1, $fn=6);
	}
	translate([-13.5, 10, -1]) {
		cylinder(h=11, r=1, $fn=6);
	}
	translate([-10.5, 0, -1]) {
		cylinder(h=11, r=1, $fn=6);
	}
}