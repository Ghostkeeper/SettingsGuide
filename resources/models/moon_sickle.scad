$fn = 360;
difference() {
	cylinder(r=10, h=4);
	translate([3, 0, -4])
		rotate([0, 10, 0])
			cylinder(r=11.5, h=12);
}