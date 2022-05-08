difference() {
	cube([40, 40, 5]);
	translate([0, 0, -1]) {
		rotate([0, 0, -5]) {
			cube([400, 400, 400]);
		}
	}
}