from super_scad.scad.Context import Context
from super_scad.scad.Scad import Scad
from super_scad.scad.Unit import Unit

from super_scad_chess.Bishop import Bishop
from super_scad_chess.King import King
from super_scad_chess.Knight import Knight
from super_scad_chess.Pawn import Pawn
from super_scad_chess.Queen import Queen
from super_scad_chess.Rook import Rook
from test.ScadTestCase import ScadTestCase


class ChessSetTest(ScadTestCase):
    """
    Testcases for chess pieces.
    """

    # ------------------------------------------------------------------------------------------------------------------
    def testBishop(self):
        """
        Test bishop.
        """
        path_actual, path_expected = self.paths()
        scad = Scad(context=Context())
        bishop = Bishop()
        scad.run_super_scad(bishop, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testKing(self):
        """
        Test king.
        """
        path_actual, path_expected = self.paths()
        scad = Scad(context=Context())
        king = King()
        scad.run_super_scad(king, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testKnight(self):
        """
        Test knight.
        """
        path_actual, path_expected = self.paths()
        scad = Scad(context=Context())
        knight = Knight()
        scad.run_super_scad(knight, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testPawn(self):
        """
        Test pawn.
        """
        path_actual, path_expected = self.paths()
        scad = Scad(context=Context())
        pawn = Pawn()
        scad.run_super_scad(pawn, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testQueen(self):
        """
        Test queen.
        """
        path_actual, path_expected = self.paths()
        scad = Scad(context=Context())
        queen = Queen()
        scad.run_super_scad(queen, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

    # ------------------------------------------------------------------------------------------------------------------
    def testRook(self):
        """
        Test rook.
        """
        path_actual, path_expected = self.paths()
        scad = Scad(context=Context())
        rook = Rook()
        scad.run_super_scad(rook, path_actual)
        actual = path_actual.read_text()
        expected = path_expected.read_text()
        self.assertEqual(expected, actual)

# ----------------------------------------------------------------------------------------------------------------------
