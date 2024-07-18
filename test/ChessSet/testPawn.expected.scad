// Unit of length: Unit.MM
translate(v = [0.0, 0.0, -28.0])
{
   scale(v = [0.2, 0.2, 0.2])
   {
      translate(v = [0.0, 0.0, 140.0])
      {
         rotate_extrude(angle = 360.0, convexity = 10, $fn = 64)
         {
            scale(v = [0.25, 0.25])
            {
               import(file = "../../super_scad_chess/include/pawn_profile.svg");
            }
         }
      }
   }
}
