// Unit of length: Unit.MM
scale(v = [0.2, 0.2, 0.2])
{
   difference()
   {
      rotate_extrude(angle = 360.0, convexity = 10, $fn = 64)
      {
         scale(v = [0.25, 0.25])
         {
            import(file = "../../super_scad_chess/include/rook_profile.svg");
         }
      }
      translate(v = [0.0, 0.0, 170.0])
      {
         union()
         {
            rotate(a = [0.0, 0.0, 0.0])
            {
               linear_extrude(height = 40.0, center = false, twist = 0.0, scale = 1.0)
               {
                  polygon(points = [[0.0, 0.0], [60.0, 50.0], [50.0, 60.0]]);
               }
            }
            rotate(a = [0.0, 0.0, 90.0])
            {
               linear_extrude(height = 40.0, center = false, twist = 0.0, scale = 1.0)
               {
                  polygon(points = [[0.0, 0.0], [60.0, 50.0], [50.0, 60.0]]);
               }
            }
            rotate(a = [0.0, 0.0, 180.0])
            {
               linear_extrude(height = 40.0, center = false, twist = 0.0, scale = 1.0)
               {
                  polygon(points = [[0.0, 0.0], [60.0, 50.0], [50.0, 60.0]]);
               }
            }
            rotate(a = [0.0, 0.0, 270.0])
            {
               linear_extrude(height = 40.0, center = false, twist = 0.0, scale = 1.0)
               {
                  polygon(points = [[0.0, 0.0], [60.0, 50.0], [50.0, 60.0]]);
               }
            }
         }
      }
   }
}
