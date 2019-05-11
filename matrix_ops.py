import numpy as np


class MatrixOps:
    """
    Experimental operations for two-dimensional arrays.
    """

    def __init__(self, dim):
        self.dim = dim


    def randomized_matrix(self, a=0, b=255):
        """
        Creates and returns a two-dimensional square array of dimension
        `self.dim`, with elements as random numbers between `a` and `b`, defaulting from 0 to 255.
        """
        matrix = []
        for _ in range(self.dim):
            row = []
            for _ in range(self.dim):
                row.append(np.random.randint(a, b))
            matrix.append(row)
        return matrix


    def vertical_ascending_matrix(self,
                                 a=0,
                                 b=255):
        """
        Creates and returns a two-dimensional square array of dimension
        `self.dim`, with elements increasing for each row, all in a row being constant.

        The output array when rendered as an image, gives a grayscale gradient,
        ranging default from black to white.
        """
        matrix = []
        layers = np.linspace(a, b, self.dim)
        for color in layers:
            row = []
            for _ in range(self.dim):
                row.append(color)
            matrix.append(row)
        return matrix


    def random_RGB_matrix(self,
                          a=0,
                          b=255):
        """
        Creates and returns a two-dimensional square array of dimension
        `self.dim`, with elements of each row being an array of random
        RGB values.
        """
        matrix = []
        for _ in range(self.dim):
           row = []
           for _ in range(self.dim):
               pixel = [x for x in np.random.randint(a, b, 3)]
               row.append(pixel)
           matrix.append(row)
        return matrix


    @staticmethod
    def clean_print(arr_2D):
        for row in arr_2D:
            for elem in row:
                print(elem)
            print('\n')
