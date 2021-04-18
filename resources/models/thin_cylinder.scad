thickness = 1.05;
$fn=40;

difference() {
	cylinder(r=20, h=5);
	cylinder(r=20 - thickness, h=5);
}