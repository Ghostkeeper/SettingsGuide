main_r = 40;
foot_r = 12;
$fs = 0.4;
$fa = 1;

module screw_hole() {
	shaft_r = 3;
	tip_r = 4;
	cylinder(r=tip_r, h=100);
	translate([0, 0, -100]) {
		cylinder(r=shaft_r, h=101);
	}
}

difference() {
	union() {
		//Main body.
		intersection() {
			translate([20, 0, 10 - main_r]) {
				rotate([-90, 0, 0]) {
					cylinder(r=main_r, h=20);
				}
			}
			cube([main_r * 2, 20, 10]);
		}
		translate([20, 0, 0]) {
			cube([50, 20, 10]);
			hull() {
				cube([40, 20, 10]);
				translate([5, 0, 0]) {
					cube([30, 25, 10]);
				}
			}
		}
		translate([20, -10, 0]) {
			cube(10);
		}
		translate([40, -15, 0]) {
			hull() {
				translate([0, 5, 0]) {
					cube([20, 10, 10]);
				}
				translate([10, 0, 0]) {
					cube(10);
				}
			}
		}

		//Left foot.
		intersection() {
			translate([0, 0, -foot_r - 10]) {
				rotate([0, 90, 0]) {
					cylinder(r=foot_r, h=10);
				}
			}
			translate([0, -10, -20]) {
				cube(10);
			}
		}
		translate([0, 0, -20]) {
			cube([10, 20, 20]);
		}

		//Right foot.
		translate([60, 0, -20]) {
			cube([10, 20, 20]);
		}
		translate([60, -5, -20]) {
			cube([20, 30, 5]);
		}
	}

	//Top fitting.
	translate([40, 25, -1]) {
		cylinder(r=6, h=12);
	}
	translate([40, 25, 2]) {
		cylinder(r=13, h=9);
	}
	hull() {
		translate([35, 10, 6]) {
			cube(10);
		}
		translate([40, 8, 6]) {
			cylinder(r=3, h=5);
		}
	}

	translate([50, -8, 5]) {
		screw_hole();
	}
	translate([70, 0, -17.5]) {
		screw_hole();
	}
	translate([70, 20, -17.5]) {
		screw_hole();
	}
	translate([5, -5, -15]) {
		screw_hole();
	}
}