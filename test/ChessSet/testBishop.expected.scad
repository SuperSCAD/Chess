// Unit of length: Unit.MM
translate(v = [0.0, 0.0, 34.0])
{
   scale(v = [0.18, 0.18, 0.2])
   {
      translate(v = [0.0, 0.0, 54.0])
      {
         difference()
         {
            rotate_extrude(angle = 360.0, convexity = 10, $fn = 64)
            {
               import(file = "../../super_scad_chess/include/bishop_profile.dxf");
            }
            rotate(a = [0.0, -45.0, 0.0])
            {
               translate(v = [-30.0, 0.0, 0.0])
               {
                  cube(size = [10.0, 80.0, 80.0], center = true);
               }
            }
         }
      }
   }
}
