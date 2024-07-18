// Unit of length: Unit.MM
scale(v = [0.2, 0.2, 0.2])
{
   rotate(a = [0.0, 0.0, 90.0])
   {
      translate(v = [0.0, 0.0, -1.0])
      {
         union()
         {
            rotate_extrude(angle = 360.0, convexity = 10, $fn = 64)
            {
               scale(v = [0.25, 0.25])
               {
                  import(file = "../../super_scad_chess/include/knight_profile.svg");
               }
            }
            translate(v = [-8.0, -12.0, 54.0])
            {
               scale(v = [3.2, 3.2, 3.2])
               {
                  import(file = "../../super_scad_chess/include/horse3.stl");
               }
            }
         }
      }
   }
}
