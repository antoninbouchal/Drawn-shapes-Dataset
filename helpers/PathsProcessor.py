import numpy as np
import cv2


class PathsProcessor:
    def __init__(self, output_size=28, padding=2, path_thickness=1):
        """

        :param output_size: int - size of out matrix (image or binary)
        :param padding: padding of matrix
        :param path_thickness: thickness of output path on image or matrix
        """
        self.output_size = output_size
        self.padding = padding
        self.path_thickness = path_thickness

    def image_from_paths(self, raw_paths):
        """
        Return image matrix with drawn paths

        :param raw_paths: [float, float][][] - Array of Array with points [x, y]
        :return: np.uint8[][]
        """
        out = np.zeros((self.output_size, self.output_size), np.uint8)
        cv2.polylines(out, self.normalize_paths(raw_paths), False, 255, self.path_thickness)
        return out

    def normalize_paths(self, raw_paths):
        """
        Transform paths to fit to out size.

        :param raw_paths: [float, float][][] - Array of Array with points [x, y]
        :return: [float, float][][]
        """
        out = []

        x_max, x_min, y_max, y_min = None, None, None, None

        for path in raw_paths:
            for point in path:
                x = float(point[0])
                y = float(point[1])

                if not x_max or x > x_max:
                    x_max = x

                if not y_max or y > y_max:
                    y_max = y

                if not x_min or x < x_min:
                    x_min = x

                if not y_min or y < y_min:
                    y_min = y

        try:
            x_ratio = (self.output_size - self.padding * 2) / (x_max - x_min)
        except ZeroDivisionError:
            x_ratio = 1

        try:
            y_ratio = (self.output_size - self.padding * 2) / (y_max - y_min)
        except ZeroDivisionError:
            y_ratio = 1

        ratio = x_ratio if x_ratio < y_ratio else y_ratio

        for path in raw_paths:
            out_path = []
            for point in path:
                x = float(point[0]) - x_min
                y = float(point[1]) - y_min

                out_path.append([self.padding + x * ratio, self.padding + y * ratio])

            out.append(np.array(out_path, np.int32))

        return out

    def binary_matrix_from_paths(self, raw_paths):
        """
        Return binary matrix with "drawn" paths.

        :param raw_paths: [float, float][][] - Array of Array with points [x, y]
        :return: bool[][]
        """
        img = self.image_from_paths(raw_paths)

        out = []
        for img_row in img:
            out_row = []

            for pixel in img_row:
                if pixel > 0:
                    out_row.append(True)
                else:
                    out_row.append(False)

            out.append(out_row)

        return out
