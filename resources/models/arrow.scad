intersection() {
	union() {
		rotate([-45, 0, 0]) {
			cube([50, 20, 20]);
		}
		translate([70, 20 / sqrt(2),0]) {
			mirror([1, 0, 0]) {
				rotate([90, 45, 0]) {
					rotate([0, 45, 0]) {
						cube([60, 30, 60]);
					}
				}
			}
		}
	}
	translate([0, -50, 0]) { //Whole arrow.
		cube([100, 100, 100]);
	}
}