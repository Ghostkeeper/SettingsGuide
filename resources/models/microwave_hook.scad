width = 10;
gap_size = 11.5;
grab_depth = 20;
thickness = 7;
radius = 10;
$fn = 360;

cube([grab_depth, gap_size, width]);
translate([grab_depth, 0, 0]) {
    cube([thickness, gap_size + radius, width]);
}
translate([grab_depth + thickness + radius, gap_size + radius, 0]) {
    difference() {
        cylinder(r = radius + thickness, h = width);
        cylinder(r = radius, h = width);
        translate([-radius - thickness, -radius - thickness, 0]) {
            cube([(radius + thickness) * 2, radius + thickness, width]);
        }
    }
}