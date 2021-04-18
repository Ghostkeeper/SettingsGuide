thickness = 3;
radius = 37 / 2 + thickness;
screws = 6;
screw_distance = 31 / 2;
screw_radius = 1.5;
off_centre = 7; //How far the axis is off the centre of the motor.
hole_radius = 6.4;
$fs = 0.4;
$fa = 0.1;

difference() {
	cylinder(r=radius, h=thickness);
	translate([0, 0, -1]) {
		for(i = [1 : screws]) {
			rotate([0, 0, i * 360 / screws + 90]) {
				translate([0, screw_distance, 0]) {
					cylinder(r=screw_radius, h=thickness + 2);
				}
			}
		}
	}
	translate([0, off_centre, -1]) {
		cylinder(r=hole_radius, h=thickness + 2);
	}
}