from unittest import TestCase
from polygons import *
import math


class TestRSCPolygon(TestCase):
    def setUp(self):
        # check out:
        # https://www.calculatorsoup.com/calculators/geometry-plane/polygon.php
        self.float_precision = 10

        self._circumradius = 1

        self._n3 = 3
        self.p3 = RSCPolygon(self._n3, self._circumradius)
        self.p3_angle = 60

        self._n4 = 4
        self.p4 = RSCPolygon(self._n4, self._circumradius)
        self.p4_angle = 90
        self.p4_area = 2.0
        self.p4_edge_length = math.sqrt(2)
        self.p4_apothem = 0.707

    #     def test_n(self):
    #         self.fail()
    #
    def test_circumradius(self):
        self.assertEqual(self._circumradius, self.p3.circumradius)

    def test_edges(self):
        self.assertEqual(self._n3, self.p3.edges)

    def test_vertices(self):
        self.assertEqual(self._n3, self.p3.vertices)

    def test_interior_angle(self):
        self.assertEqual(self.p3_angle, self.p3.interior_angle)
        self.assertEqual(self.p4_angle, self.p4.interior_angle)

    def test_edge_length(self):
        # AssertionError: 1.4142135623730951 != 1.414213562373095
        #   self.assertEqual(self.p4_edge_length, self.p4.edge_length)
        self.assertAlmostEqual(self.p4_edge_length, self.p4.edge_length, places=self.float_precision)

    def test_apothem(self):
        self.assertAlmostEqual(self.p4_apothem, self.p4.apothem, places=3)

    def test_area(self):
        self.assertEqual(self.p4_area, self.p4.area)

    def test_perimeter(self):
        self.assertAlmostEqual(self.p4_edge_length * 4, self.p4.perimeter, places=self.float_precision)

    def test_repr(self):
        self.assertEqual(f'RSCPolygon(n=3, circumradius={self._circumradius})', str(self.p3),
                         'Wrong representation. Check __repr__ method')

    def test_lazy_reset(self):
        # helper funcs
        def check_cash_is_none():
            # check cashed values are set to None
            self.assertIsNone(p1._interior_angle)
            self.assertIsNone(p1._edge_length)
            self.assertIsNone(p1._apothem)
            self.assertIsNone(p1._area)
            self.assertIsNone(p1._perimeter)

        def calc_lazy_props(pl: RSCPolygon):
            # calculate lazy props
            ia = pl.interior_angle
            el = pl.edge_length
            ap = pl.apothem
            ar = pl.area
            pr = pl.perimeter
            return ia, el, ap, ar, pr

        # tests
        p1 = RSCPolygon(7, 10)
        check_cash_is_none()
        # ia, el, ap, ar, pr = calc_lazy_props(p1)
        _ = calc_lazy_props(p1)
        # ToDo verify calculated lazy props

        # verify reset if change n
        p1.edges = 6
        check_cash_is_none()
        _ = calc_lazy_props(p1)

        # verify reset if change n
        p1.edges = 6
        check_cash_is_none()
        _ = calc_lazy_props(p1)

    def test_eq(self):
        p1 = RSCPolygon(10, 11)
        p2 = RSCPolygon(8, 12)
        p3 = RSCPolygon(10, 22)
        p4 = RSCPolygon(8, 12)
        self.assertNotEqual(self.p3, self.p4)
        self.assertNotEqual(p1, p3)
        self.assertEqual(p2, p4)

    def test_gt(self):
        p1 = RSCPolygon(3, 10)
        p2 = RSCPolygon(10, 10)
        p3 = RSCPolygon(15, 10)

        self.assertGreater(p2, p1)
        self.assertLess(p2, p3)

    def test_exceptions(self):
        self.assertRaises(ValueError, RSCPolygon, 2, 12)
        self.assertRaises(ValueError, RSCPolygon, 5, -12)
        self.assertRaises(TypeError, RSCPolygon, 'a', 12)
        self.assertRaises(TypeError, RSCPolygon, 5+5j, 12)


class TestRSCPolygons(TestCase):
    def setUp(self):
        # check out:
        # https://www.calculatorsoup.com/calculators/geometry-plane/polygon.php
        self.float_precision = 10
        self._circumradius = 1
        self._max_n = 20
        self.ps = RSCPolygons(self._max_n, self._circumradius)

    def test_max_eff(self):
        max_eff_pl = self.ps.max_eff_polygon
        self.assertEqual(RSCPolygon(n=20, circumradius=1), max_eff_pl)
        self.assertEqual(0.49384417029756883, max_eff_pl.area/max_eff_pl.perimeter)

    def test_repr(self):
        self.assertEqual(f'RSCPolygons(largest_n={self._max_n}, circumradius={self._circumradius})', str(self.ps),
                         'Wrong representation. Check __repr__ method')

    def test_len(self):
        self.assertEqual(self._max_n - 2, len(self.ps))

    def test_getitem(self):
        # by index
        self.assertEqual(RSCPolygon(3, self._circumradius), self.ps[0])
        self.assertEqual(RSCPolygon(7, self._circumradius), self.ps[4])
        self.assertEqual(RSCPolygon(20, self._circumradius), self.ps[-1])

        # by slice
        self.assertEqual(
            [RSCPolygon(3, self._circumradius), RSCPolygon(4, self._circumradius)],
            self.ps[:2])
