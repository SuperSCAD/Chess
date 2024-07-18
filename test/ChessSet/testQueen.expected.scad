// Unit of length: Unit.MM
scale(v = [0.185, 0.185, 0.185])
{
   union()
   {
      rotate_extrude(angle = 360.0, convexity = 10, $fn = 64)
      {
         scale(v = [0.25, 0.25])
         {
            import(file = "../../super_scad_chess/include/queen_profile.svg");
         }
      }
      translate(v = [0.0, 0.0, 210.0])
      {
         scale(v = [6.7, 6.7, 7.5])
         {
            import(file = "../../super_scad_chess/include/queen_crown2.stl");
         }
      }
   }
}
