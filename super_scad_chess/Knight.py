from super_scad.boolean.Union import Union
from super_scad.d0.Import import Import
from super_scad.d3.RotateExtrude import RotateExtrude
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.transformation.Rotate3D import Rotate3D
from super_scad.transformation.Scale2D import Scale2D
from super_scad.transformation.Scale3D import Scale3D
from super_scad.transformation.Translate3D import Translate3D


class Knight(ScadWidget):
    """
    Generates OpenSCAD code for a knight.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        path1 = context.resolve_path('include/knight_profile.svg')
        path2 = context.resolve_path('include/horse3.stl')

        body = RotateExtrude(convexity=10,
                             fn=64,
                             child=Scale2D(factor=0.25,
                                           child=Import(path=path1)))

        knight = Translate3D(x=-8.0,
                             y=-12.0,
                             z=54.0,
                             child=Scale3D(factor=3.2,
                                           child=Import(path=path2)))

        return Scale3D(factor=0.2,
                       child=Rotate3D(angle_z=90.0,
                                      child=Translate3D(z=-1.0,
                                                        child=Union(children=[body, knight]))))

# ----------------------------------------------------------------------------------------------------------------------
