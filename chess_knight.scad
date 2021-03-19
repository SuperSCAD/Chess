segments = 64;

module knight() {
    scale(0.2)
    rotate([0, 0, 0])
    translate([0, 0, 0]) {

    translate([0, 0, 30])
    union () {
        rotate_extrude(convexity = 10, $fn = 64) {
            scale(.25)
        import(file = "profiles/knight_profile.svg");
        }
        // Import STL for the knight
        translate([-8, -12, 54])
        scale(3.2)
        import(file = "horse3.stl");
    }

    }
}

knight();