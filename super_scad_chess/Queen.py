from super_scad.boolean.Union import Union
from super_scad.d0.Import import Import
from super_scad.d3.RotateExtrude import RotateExtrude
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.transformation.Scale2D import Scale2D
from super_scad.transformation.Scale3D import Scale3D
from super_scad.transformation.Translate3D import Translate3D


class Queen(ScadWidget):
    """
    Generates OpenSCAD code for a queen.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        path1 = context.resolve_path('include/queen_profile.svg')
        path2 = context.resolve_path('include/queen_crown2.stl')

        body = RotateExtrude(convexity=10,
                             fn=64,
                             child=Scale2D(factor=0.25,
                                           child=Import(path=path1)))

        crown = Translate3D(z=210.0,
                            child=Scale3D(factor_x=6.7,
                                          factor_y=6.7,
                                          factor_z=7.5,
                                          child=Import(path=path2)))

        return Scale3D(factor=0.185, child=Union(children=[body, crown]))

# ----------------------------------------------------------------------------------------------------------------------
