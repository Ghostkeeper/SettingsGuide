height = 4;
radius = 20;
inner_radius = radius / 2;
teeth_depth = 3;
teeth = 30;
$fs = 0.3;
$fa = 1;

difference() {
	union() {
		cylinder(h=height, r=radius, $fn=teeth);
		for(tooth = [0:teeth]) {
			rotate([0, 0, tooth * 360 / teeth]) {
				linear_extrude(height=height) {
					polygon(points=[[radius, 0], [cos(360 / teeth) * radius, sin(360 / teeth) * radius], [cos(180 / teeth) * (radius + teeth_depth), sin(180 / teeth) * (radius + teeth_depth)]], convexity=1);
				}
			}
		}
	}
	translate([0, 0, -1]) {
		cylinder(r=inner_radius, h=6);
	}
}