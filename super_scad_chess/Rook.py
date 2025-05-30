from super_scad.boolean.Difference import Difference
from super_scad.boolean.Union import Union
from super_scad.d0.Import import Import
from super_scad.d2.Polygon import Polygon
from super_scad.d3.LinearExtrude import LinearExtrude
from super_scad.d3.RotateExtrude import RotateExtrude
from super_scad.scad.Context import Context
from super_scad.scad.ScadWidget import ScadWidget
from super_scad.transformation.Rotate3D import Rotate3D
from super_scad.transformation.Scale2D import Scale2D
from super_scad.transformation.Scale3D import Scale3D
from super_scad.transformation.Translate3D import Translate3D
from super_scad.type.Vector2 import Vector2


class Rook(ScadWidget):
    """
    Generates OpenSCAD code for a rook.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def build(self, context: Context) -> ScadWidget:
        """
        Builds a SuperSCAD object.

        :param context: The build context.
        """
        path = context.resolve_path('include/rook_profile.svg')

        extrude = RotateExtrude(convexity=10,
                                fn=64,
                                child=Scale2D(factor=0.25,
                                              child=Import(path=path)))

        points = [Vector2(0.0, 0.0), Vector2(60.0, 50.0), Vector2(50.0, 60.0)]
        cutout = LinearExtrude(height=40.0, child=Polygon(points=points))
        children = []
        for i in range(0, 360, 90):
            children.append(Rotate3D(angle_z=i, child=cutout))
        cutouts = Translate3D(z=170.0, child=Union(children=children))

        return Scale3D(factor=0.2, child=Difference(children=[extrude, cutouts]))

# ----------------------------------------------------------------------------------------------------------------------
