radius = 20;
$fn = 360;

module hexacone() {
	cylinder(r1=radius, r2=cos(60) * radius, h=sin(60) * radius);
	translate([0, 0, -sin(60) * radius])
		cylinder(r1=cos(60) * radius, r2=radius, h=sin(60) * radius);
}

difference() {
	hexacone();
	translate([0, -radius, -sin(60) * radius])
		cube([radius, radius * 2, sin(60) * radius * 2]);
}
rotate([60, 0, 0]) {
	difference() {
		hexacone();
		translate([-radius, -radius, -sin(60) * radius])
			cube([radius, radius * 2, sin(60) * radius * 2]);
	}
}