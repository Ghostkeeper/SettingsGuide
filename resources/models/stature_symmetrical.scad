$fs = 0.4;
$fa = 1;

difference() {
	//Tube shape to start with.
	cylinder(r=20, h=20);
	translate([0, 0, -1]) {
		cylinder(r=17, h=22);
	}

	//Cut off two cylinders at the bottom, axis-aligned.
	translate([-21, 0, 0]) {
		rotate([0, 90, 0]) {
			cylinder(r=11, h=42);
		}
	}
	translate([0, -21, 0]) {
		rotate([-90, 0, 0]) {
			cylinder(r=11, h=42);
		}
	}
	//And two cylinders at the top, diagonally.
	translate([-20, -20, 20]) {
		rotate([0, 90, 45]) {
			cylinder(r=11, h=60);
		}
	}
	translate([20, -20, 20]) {
		rotate([-90, 0, 45]) {
			cylinder(r=11, h=60);
		}
	}
}