$fs = 0.5;
$fa = 1;

difference() {
	cylinder(r1=45, r2=0, h=90);
	translate([0.5, 0, 0]) {
		cylinder(r1=42, r2=0, h=93);
	}
}