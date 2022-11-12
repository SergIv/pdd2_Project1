# module for regular strictly convex polygon RSCPolygon class and custom sequence for polygons
import numbers
from math import pi, sin, cos


class RSCPolygon:
    """
    class for a regular strictly convex polygon with
      n edges ( = n vertices)
      R circumradius
    """

    def __init__(self, n: int, circumradius):
        self.edges = n
        self.circumradius = circumradius
        self._reset_lazy()

    def _reset_lazy(self):
        # helper function to reset all precalculated lazy properties

        # self._interior_angle, self._edge_length, self._apothem, self._area, self._perimeter = \
        # None,                 None,              None,          None,       None
        self._interior_angle = None
        self._edge_length = None
        self._apothem = None
        self._area = None
        self._perimeter = None

    @property
    def edges(self):
        """edges property means number of edges (and number of vertices) in Polygon"""
        return self._n

    @edges.setter
    def edges(self, value):
        if value < 3:
            raise ValueError('Value for n (edges and vertices) should be int type and > 2 ')
        self._n = int(value)
        self._reset_lazy()

    @property
    def vertices(self):
        """vertices property means number of edges (and number of vertices) in Polygon"""
        return self._n

    @vertices.setter
    def vertices(self, value):
        self.edges = value

    # @property
    # def n(self):
    #     return self._n
    #
    # @n.setter
    # def n(self, value):
    #     if value < 3:
    #         raise ValueError('Value for n, edges and vertices should be int type and > 2 ')
    #     self._n = int(value)
    #     self._reset_lazy()

    @property
    def circumradius(self):
        """The circumradius property"""
        return self._circumradius

    @circumradius.setter
    def circumradius(self, value):
        if not isinstance(value, numbers.Real) or value < 0:
            raise ValueError('Value for Circumradius should be a Real number and > 0 ')
        self._circumradius = value
        self._reset_lazy()

    @property
    def interior_angle(self):
        """interior_angle calculated property calculated as (n−2)×180/n """
        if self._interior_angle is None:
            self._interior_angle = (self._n - 2) * 180 / self._n  # 𝑛−2×180𝑛
        return self._interior_angle

    @property
    def edge_length(self):
        """edge_length calculated property calculated as 2𝑅 sin(𝜋/𝑛) """
        if self._edge_length is None:
            self._edge_length = 2 * self.circumradius * sin(pi / self._n)  # edge length s = 2𝑅sin(𝜋/𝑛)
        return self._edge_length

    @property
    def apothem(self):
        if self._apothem is None:
            self._apothem = self.circumradius * cos(pi / self._n)  # apothem   a = 𝑅𝑐𝑜𝑠(𝜋/𝑛)
        return self._apothem

    @property
    def area(self):
        if self._area is None:
            self._area = (self._n * self.edge_length * self.apothem) / 2  # area = 1/2 𝑛𝑠𝑎
        return self._area

    @property
    def perimeter(self):
        if self._perimeter is None:
            self._perimeter = self._n * self.edge_length
        return self._perimeter

    def __repr__(self):
        return f'{self.__class__.__name__}(n={self._n}, circumradius={self.circumradius})'

    def __eq__(self, other):
        # implements equality (==) based on # of vertices and circumradius (__eq__)
        if isinstance(other, self.__class__):
            return (self._n == other._n
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented

    def __gt__(self, other):
        # implements > based on number of vertices only (__gt__)
        if isinstance(other, self.__class__):
            return self._n > other._n
        else:
            return NotImplemented


class RSCPolygons:
    """
    Implements a Polygons sequence type and Polygons Iterable and Iterator
    """

    def __init__(self, largest_n, circumradius):
        # Initializer
        # • number of vertices for largest polygon in the sequence
        # • common circumradius for all polygons
        if int(largest_n) < 3:
            raise ValueError('largest_n should be an integer number and >= 3')
        else:
            self._largest_n = int(largest_n)
        if not isinstance(circumradius, numbers.Real):
            raise TypeError('circumradius should be a Real number')
        if circumradius <= 0:
            raise ValueError('circumradius should be > 0')

        # self.largest_n = largest_n
        self.circumradius = circumradius

        # TODO remove this
        # if largest_n > 2:
        #     self._pls = [RSCPolygon(n, circumradius) for n in range(3, largest_n+1)]
        # else:
        #     self._pls = []

    @property
    def max_eff_polygon(self):
        # • max efficiency polygon: returns the Polygon with the highest area : perimeter ratio
        return max(self, key=lambda pl: pl.area / pl.perimeter)

    def __len__(self):
        # • supports the len function (__len__)
        return self._largest_n - 2

    def __getitem__(self, item):
        print("RSCPolygons.__getitem__ called")
        # • functions as a sequence type (__getitem__)
        # return self._pls[item]
        if isinstance(item, int):
            if item < 0 and self._largest_n - 2 + item > 0:
                item = self._largest_n - 2 + item
            elif item < 0:
                raise ValueError('index is out of range')
            return RSCPolygon(item+3, self.circumradius)
        elif isinstance(item, slice):
            ind = item.indices(self._largest_n - 2)
            return [RSCPolygon(n, self.circumradius) for n in range(ind[0]+3, ind[1]+3)]

    def __repr__(self):
        # • has a proper representation (__repr__)
        return f'{self.__class__.__name__}(largest_n={self._largest_n}, circumradius={self.circumradius})'

    # TODO Iterable methods
    def __iter__(self):
        return self.RSCPIter(self._largest_n, self.circumradius)

    # TODO Iterator class Functionality
    class RSCPIter:
        def __init__(self, largest_n, circumradius):
            self._largest_n = largest_n
            self._circumradius = circumradius
            self._i = 3

        def __iter__(self):
            return self

        def __next__(self):
            print('RSCPIter.__next__ called')
            if self._i > self._largest_n:
                raise StopIteration
            else:
                result = RSCPolygon(self._i, self._circumradius)
                self._i += 1
                return result
