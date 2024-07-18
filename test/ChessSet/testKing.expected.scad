// Unit of length: Unit.MM
scale(v = [0.2, 0.2, 0.2])
{
   union()
   {
      translate(v = [-21.0, 8.0, 270.0])
      {
         rotate(a = [90.0, 0.0, 0.0])
         {
            linear_extrude(height = 16.0, center = false, twist = 0.0, scale = 1.0)
            {
               scale(v = [0.22, 0.22])
               {
                  import(file = "../../super_scad_chess/include/cross_profile.svg");
               }
            }
         }
      }
      scale(v = [0.25, 0.25, 0.25])
      {
         rotate_extrude(angle = 360.0, convexity = 10, $fn = 64)
         {
            import(file = "../../super_scad_chess/include/king_profile.svg");
         }
      }
   }
}
