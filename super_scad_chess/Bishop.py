from super_scad.boolean.Difference import Difference
from super_scad.d0.Import import Import
from super_scad.d3.Cuboid import Cuboid
from super_scad.d3.RotateExtrude import RotateExtrude
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.transformation.Rotate3D import Rotate3D
from super_scad.transformation.Scale3D import Scale3D
from super_scad.transformation.Translate3D import Translate3D


class Bishop(ScadWidget):
    """
    Generates OpenSCAD code for a bishop.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        path = context.resolve_path('include/bishop_profile.dxf')

        body = Translate3D(z=54, child=Difference(children=[RotateExtrude(convexity=10,
                                                                          fn=64,
                                                                          child=Import(path=path)),
                                                            Rotate3D(angle_y=-45.0,
                                                                     child=Translate3D(x=-30.0,
                                                                                       child=Cuboid(width=10,
                                                                                                    depth=80,
                                                                                                    height=80,
                                                                                                    center=True)))]))

        return Translate3D(z=34.0,
                           child=Scale3D(factor_x=0.18,
                                         factor_y=0.18,
                                         factor_z=0.2,
                                         child=body))

# ----------------------------------------------------------------------------------------------------------------------
