$fs = 0.3;
$fa = 1;

difference() {
	intersection() {
		cylinder(r=20, h=50);
		cylinder(r1=30, r2=13, h=50);
	}
	rotate([-90, 0, 0]) {
		translate([0, -20, -20]) {
			translate([35, 0, 0]) {
				cylinder(r=20, h=40);
			}
			translate([-35, 0, 0]) {
				cylinder(r=20, h=40);
			}
		}
	}
	translate([0, 0, 13]) {
		translate([-1, -21, 0]) {
			cube([2, 42, 100]);
		}
		hull() {
			translate([-10, -21, 0]) {
				cube([20, 42, 28]);
			}
			translate([0, -21, 30]) {
				rotate([-90, 0, 0]) {
					cylinder(r=3, h=42);
				}
			}
		}
		cylinder(r=5, h=100);
	}
}