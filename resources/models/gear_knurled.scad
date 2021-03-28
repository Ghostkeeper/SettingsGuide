$fs = 0.3;
$fa = 1;

module gear(height, radius, teeth_depth, teeth=30) {
	cylinder(h=height, r=radius + 0.1, $fn=teeth);
	for(tooth = [0:teeth]) {
		rotate([0, 0, tooth * 360 / teeth]) {
			linear_extrude(height=height, twist=30 + 180 / teeth) {
				polygon(points=[[radius, 0], [cos(360 / teeth) * radius, sin(360 / teeth) * radius], [cos(180 / teeth) * (radius + teeth_depth), sin(180 / teeth) * (radius + teeth_depth)]], convexity=1);
			}
		}
	}
}

difference() {
	gear(height=30, radius=20, teeth_depth=3);
	union() {
		cube([10, 10, 31]);
		cylinder(r=10, h=31);
	}
}