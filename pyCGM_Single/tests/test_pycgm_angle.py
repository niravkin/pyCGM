import unittest
import pyCGM_Single.pyCGM as pyCGM
import numpy as np
import pytest

rounding_precision = 6

class TestPycgmAngle():
    """
    This class tests the functions used for getting angles in pyCGM.py:
    getangle_sho
    getangle_spi
    getangle
    getHeadangle
    getPelangle
    """

    @pytest.mark.parametrize(["xRot", "yRot", "zRot", "expected"], [
        (0, 0, 0, [0, 0, 0]),
        # X rotations
        (90, 0, 0, [0, 90, 0]), (30, 0, 0, [0, 30, 0]), (-30, 0, 0, [0, -30, 0]), (120, 0, 0, [0, 120, 0]),
        (-120, 0, 0, [0, -120, 0]), (180, 0, 0, [0, 180, 0]),
        # Y rotations
        (0, 90, 0, [90, 0, 0]), (0, 30, 0, [30, 0, 0]), (0, -30, 0, [-30, 0, 0]), (0, 120, 0, [60, -180, -180]),
        (0, -120, 0, [-60, -180, -180]), (0, 180, 0, [0, -180, -180]),
        # Z rotations
        (0, 0, 90, [0, 0, 90]), (0, 0, 30, [0, 0, 30]), (0, 0, -30, [0, 0, -30]), (0, 0, 120, [0, 0, 120]),
        (0, 0, -120, [0, 0, -120]), (0, 0, 180, [0, 0, 180]),
        # Multiple Rotations
        (150, 30, 0, [30, 150, 0]), (45, 0, 60, [0, 45, 60]), (0, 90, 120, [90, 0, 120]), (135, 45, 90, [45, 135, 90])
    ])
    def test_getangle_sho(self, xRot, yRot, zRot, expected):
        """
        This test provides coverage of the getangle_sho function in pyCGM.py,
        defined as getangle_sho(axisP,axisD) where axisP is the proximal axis and axisD is the dorsal axis

        This test takes 3 parameters. The first 3 parameters are angles, representing the x, y, and z dimensional rotations,
        used to create a rotational matrix. The last parameter is the expected resulting list for calling the function
        getangle_sho on the created rotational matrix and one with no rotation.
        """
        # Create axisP as a rotatinal matrix using the x, y, and z rotations given in testcase
        axisP = pyCGM.rotmat(xRot, yRot, zRot)
        axisD = pyCGM.rotmat(0, 0, 0)
        result = pyCGM.getangle_sho(axisP, axisD)
        np.testing.assert_almost_equal(result, expected, rounding_precision)

    def test_getangle_sho_datatypes(self):
        axisD = pyCGM.rotmat(0, 0, 0)
        axisP_floats = pyCGM.rotmat(90, 0, 90)
        axisP_ints = [[int(y) for y in x] for x in axisP_floats]
        expected = [0, 90, 90]

        # Check that calling getangle_sho on a list of ints yields the expected results
        result_int_list = pyCGM.getangle_sho(axisP_ints, axisD)
        np.testing.assert_almost_equal(result_int_list, expected, rounding_precision)

        # Check that calling getangle_sho on a numpy array of ints yields the expected results
        result_int_nparray = pyCGM.getangle_sho(np.array(axisP_ints, dtype='int'), np.array(axisD, dtype='int'))
        np.testing.assert_almost_equal(result_int_nparray, expected, rounding_precision)

        # Check that calling getangle_sho on a list of floats yields the expected results
        result_float_list = pyCGM.getangle_sho(axisP_floats, axisD)
        np.testing.assert_almost_equal(result_float_list, expected, rounding_precision)

        # Check that calling getangle_sho on a numpy array of floats yields the expected results
        result_float_nparray = pyCGM.getangle_sho(np.array(axisP_floats, dtype='float'), np.array(axisD, dtype='float'))
        np.testing.assert_almost_equal(result_float_nparray, expected, rounding_precision)

    @pytest.mark.parametrize(["xRot", "yRot", "zRot", "expected"], [
        (0, 0, 0, [0, 0, 0]),
        # X rotations
        (90, 0, 0, [0, 0, 90]), (30, 0, 0, [0, 0, 30]), (-30, 0, 0, [0, 0, -30]), (120, 0, 0, [0, 0, 60]), (-120, 0, 0, [0, 0, -60]), (180, 0, 0, [0, 0, 0]),
        # Y rotations
        (0, 90, 0, [90, 0, 0]), (0, 30, 0, [30, 0, 0]), (0, -30, 0, [-30, 0, 0]), (0, 120, 0, [60, 0, 0]), (0, -120, 0, [-60, 0, 0]), (0, 180, 0, [0, 0, 0]),
        # Z rotations
        (0, 0, 90, [0, 90, 0]), (0, 0, 30, [0, 30, 0]), (0, 0, -30, [0, -30, 0]), (0, 0, 120, [0, 60, 0]), (0, 0, -120, [0, -60, 0]), (0, 0, 180, [0, 0, 0]),
        # Multiple Rotations
        (150, 30, 0, [-30, 0, 30]), (45, 0, 60, [-40.89339465, 67.7923457, 20.70481105]), (0, 90, 120, [-90, 0, 60]), (135, 45, 90, [-54.73561032, 54.73561032, -30])
    ])
    def test_getangle_spi(self, xRot, yRot, zRot, expected):
        """
        This test provides coverage of the getangle_spi function in pyCGM.py,
        defined as getangle_spi(axisP,axisD) where axisP is the proximal axis and axisD is the dorsal axis

        This test takes 3 parameters. The first 3 parameters are angles, representing the x, y, and z dimensional rotations,
        used to create a rotational matrix. The last parameter is the expected resulting list for calling the function
        getangle_spi on the created rotational matrix and one with no rotation.
        """
        # Create axisP as a rotatinal matrix using the x, y, and z rotations given in testcase
        axisP = pyCGM.rotmat(xRot, yRot, zRot)
        axisD = pyCGM.rotmat(0, 0, 0)
        result = pyCGM.getangle_spi(axisP, axisD)
        np.testing.assert_almost_equal(result, expected, rounding_precision)

    def test_getangle_spi_datatypes(self):
        axisD = pyCGM.rotmat(0, 0, 0)
        axisP_floats = pyCGM.rotmat(90, 0, 90)
        axisP_ints = [[int(y) for y in x] for x in axisP_floats]
        expected = [-90, 90, 0]

        # Check that calling getangle_spi on a list of ints yields the expected results
        result_int_list = pyCGM.getangle_spi(axisP_ints, axisD)
        np.testing.assert_almost_equal(result_int_list, expected, rounding_precision)

        # Check that calling getangle_spi on a numpy array of ints yields the expected results
        result_int_nparray = pyCGM.getangle_spi(np.array(axisP_ints, dtype='int'), np.array(axisD, dtype='int'))
        np.testing.assert_almost_equal(result_int_nparray, expected, rounding_precision)

        # Check that calling getangle_spi on a list of floats yields the expected results
        result_float_list = pyCGM.getangle_spi(axisP_floats, axisD)
        np.testing.assert_almost_equal(result_float_list, expected, rounding_precision)

        # Check that calling getangle_spi on a numpy array of floats yields the expected results
        result_float_nparray = pyCGM.getangle_spi(np.array(axisP_floats, dtype='float'), np.array(axisD, dtype='float'))
        np.testing.assert_almost_equal(result_float_nparray, expected, rounding_precision)

    @pytest.mark.parametrize(["xRot", "yRot", "zRot", "expected"], [
        (0, 0, 0, [0, 0, 90]),
        # X rotations
        (90, 0, 0, [0, 90, 90]), (30, 0, 0, [0, 30, 90]), (-30, 0, 0, [0, -30, 90]), (120, 0, 0, [180, 60, -90]), (-120, 0, 0, [180, -60, -90]), (180, 0, 0, [180, 0, -90]),
        # Y rotations
        (0, 90, 0, [90, 0, 90]), (0, 30, 0, [30, 0, 90]), (0, -30, 0, [-30, 0, 90]), (0, 120, 0, [120, 0, 90]), (0, -120, 0, [-120, 0, 90]), (0, 180, 0, [180, 0, 90]),
        # Z rotations
        (0, 0, 90, [0, 0, 0]), (0, 0, 30, [0, 0, 60]), (0, 0, -30, [0, 0, 120]), (0, 0, 120, [0, 0, -30]), (0, 0, -120, [0, 0, -150]), (0, 0, 180, [0, 0, -90]),
        # Multiple Rotations
        (150, 30, 0, [146.30993247, 25.65890627, -73.89788625]), (45, 0, 60, [0, 45, 30]), (0, 90, 120, [90, 0, -30]), (135, 45, 90, [125.26438968, 30, -144.73561032])
    ])
    def test_getangle(self, xRot, yRot, zRot, expected):
        """
        This test provides coverage of the getangle function in pyCGM.py,
        defined as getangle(axisP,axisD) where axisP is the proximal axis and axisD is the dorsal axis

        This test takes 3 parameters. The first 3 parameters are angles, representing the x, y, and z dimensional rotations,
        used to create a rotational matrix. The last parameter is the expected resulting list for calling the function
        getangle on the created rotational matrix and one with no rotation.
        """
        # Create axisP as a rotatinal matrix using the x, y, and z rotations given in testcase
        axisP = pyCGM.rotmat(xRot, yRot, zRot)
        axisD = pyCGM.rotmat(0, 0, 0)
        result = pyCGM.getangle(axisP, axisD)
        np.testing.assert_almost_equal(result, expected, rounding_precision)

    def test_getangle_datatypes(self):
        axisD = pyCGM.rotmat(0, 0, 0)
        axisP_floats = pyCGM.rotmat(90, 0, 90)
        axisP_ints = [[int(y) for y in x] for x in axisP_floats]
        expected = [0, 90, 0]

        # Check that calling getangle on a list of ints yields the expected results
        result_int_list = pyCGM.getangle(axisP_ints, axisD)
        np.testing.assert_almost_equal(result_int_list, expected, rounding_precision)

        # Check that calling getangle on a numpy array of ints yields the expected results
        result_int_nparray = pyCGM.getangle(np.array(axisP_ints, dtype='int'), np.array(axisD, dtype='int'))
        np.testing.assert_almost_equal(result_int_nparray, expected, rounding_precision)

        # Check that calling getangle on a list of floats yields the expected results
        result_float_list = pyCGM.getangle(axisP_floats, axisD)
        np.testing.assert_almost_equal(result_float_list, expected, rounding_precision)

        # Check that calling getangle on a numpy array of floats yields the expected results
        result_float_nparray = pyCGM.getangle(np.array(axisP_floats, dtype='float'), np.array(axisD, dtype='float'))
        np.testing.assert_almost_equal(result_float_nparray, expected, rounding_precision)

    @pytest.mark.parametrize(["xRot", "yRot", "zRot", "expected"], [
        (0, 0, 0, [0, 0, -180]),
        # X rotations
        (90, 0, 0, [0, 90, -180]), (30, 0, 0, [0, 30, -180]), (-30, 0, 0, [0, -30, -180]), (120, 0, 0, [180, 60, 0]), (-120, 0, 0, [180, -60, 0]), (180, 0, 0, [180, 0, 0]),
        # Y rotations
        (0, 90, 0, [90, 0, -180]), (0, 30, 0, [30, 0, -180]), (0, -30, 0, [330, 0, -180]), (0, 120, 0, [120, 0, -180]), (0, -120, 0, [240, 0, -180]), (0, 180, 0, [180, 0, -180]),
        # Z rotations
        (0, 0, 90, [0, 0, -90]), (0, 0, 30, [0, 0, -150]), (0, 0, -30, [0, 0, -210]), (0, 0, 120, [0, 0, -60]), (0, 0, -120, [0, 0, -300]), (0, 0, 180, [0, 0, 0]),
        # Multiple Rotations
        (150, 30, 0, [146.30993247, 25.65890627, -16.10211375]), (45, 0, 60, [0, 45, -120]), (0, 90, 120, [90, 0, -60]), (135, 45, 90, [125.26438968, 30, 54.73561032])
    ])
    def test_getHeadangle(self, xRot, yRot, zRot, expected):
        """
        This test provides coverage of the getHeadangle function in pyCGM.py,
        defined as getHeadangle(axisP,axisD) where axisP is the proximal axis and axisD is the dorsal axis

        This test takes 3 parameters. The first 3 parameters are angles, representing the x, y, and z dimensional rotations,
        used to create a rotational matrix. The last parameter is the expected resulting list for calling the function
        getHeadangle on the created rotational matrix and one with no rotation.
        """
        # Create axisP as a rotatinal matrix using the x, y, and z rotations given in testcase
        axisP = pyCGM.rotmat(xRot, yRot, zRot)
        axisD = pyCGM.rotmat(0, 0, 0)
        result = pyCGM.getHeadangle(axisP, axisD)
        np.testing.assert_almost_equal(result, expected, rounding_precision)

    def test_getHeadangle_datatypes(self):
        axisD = pyCGM.rotmat(0, 0, 0)
        axisP_floats = pyCGM.rotmat(90, 90, 90)
        axisP_ints = [[int(y) for y in x] for x in axisP_floats]
        expected = [90, 0, 0]

        # Check that calling getHeadangle on a list of ints yields the expected results
        result_int_list = pyCGM.getHeadangle(axisP_ints, axisD)
        np.testing.assert_almost_equal(result_int_list, expected, rounding_precision)

        # Check that calling getHeadangle on a numpy array of ints yields the expected results
        result_int_nparray = pyCGM.getHeadangle(np.array(axisP_ints, dtype='int'), np.array(axisD, dtype='int'))
        np.testing.assert_almost_equal(result_int_nparray, expected, rounding_precision)

        # Check that calling getHeadangle on a list of floats yields the expected results
        result_float_list = pyCGM.getHeadangle(axisP_floats, axisD)
        np.testing.assert_almost_equal(result_float_list, expected, rounding_precision)

        # Check that calling getHeadangle on a numpy array of floats yields the expected results
        result_float_nparray = pyCGM.getHeadangle(np.array(axisP_floats, dtype='float'), np.array(axisD, dtype='float'))
        np.testing.assert_almost_equal(result_float_nparray, expected, rounding_precision)

    @pytest.mark.parametrize(["xRot", "yRot", "zRot", "expected"], [
        (0, 0, 0, [0, 0, 0]),
        # X rotations
        (90, 0, 0, [0, -90, 0]), (30, 0, 0, [0, -30, 0]), (-30, 0, 0, [0, 30, 0]), (120, 0, 0, [180, -60, 180]), (-120, 0, 0, [180, 60, 180]), (180, 0, 0, [180, 0, 180]),
        # Y rotations
        (0, 90, 0, [90, 0, 0]), (0, 30, 0, [30, 0, 0]), (0, -30, 0, [-30, 0, 0]), (0, 120, 0, [120, 0, 0]), (0, -120, 0, [-120, 0, -0]), (0, 180, 0, [180, 0, 0]),
        # Z rotations
        (0, 0, 90, [0, 0, 90]), (0, 0, 30, [0, 0, 30]), (0, 0, -30, [0, 0, -30]), (0, 0, 120, [0, 0, 120]), (0, 0, -120, [0, 0, -120]), (0, 0, 180, [0, 0, 180]),
        # Multiple Rotations
        (150, 30, 0, [146.30993247, -25.65890627, 163.89788625]), (45, 0, 60, [0, -45, 60]), (0, 90, 120, [90, 0, 120]), (135, 45, 90, [125.26438968, -30, -125.26438968])
    ])
    def test_getPelangle(self, xRot, yRot, zRot, expected):
        """
        This test provides coverage of the getPelangle function in pyCGM.py,
        defined as getPelangle(axisP,axisD) where axisP is the proximal axis and axisD is the dorsal axis

        This test takes 3 parameters. The first 3 parameters are angles, representing the x, y, and z dimensional rotations,
        used to create a rotational matrix. The last parameter is the expected resulting list for calling the function
        getPelangle on the created rotational matrix and one with no rotation.
        """
        # Create axisP as a rotatinal matrix using the x, y, and z rotations given in testcase
        axisP = pyCGM.rotmat(xRot, yRot, zRot)
        axisD = pyCGM.rotmat(0, 0, 0)
        result = pyCGM.getPelangle(axisP, axisD)
        np.testing.assert_almost_equal(result, expected, rounding_precision)

    def test_getPelangle_datatypes(self):
        axisD = pyCGM.rotmat(0, 0, 0)
        axisP_floats = pyCGM.rotmat(90, 90, 90)
        axisP_ints = [[int(y) for y in x] for x in axisP_floats]
        expected = [90, 0, 180]

        # Check that calling getPelangle on a list of ints yields the expected results
        result_int_list = pyCGM.getPelangle(axisP_ints, axisD)
        np.testing.assert_almost_equal(result_int_list, expected, rounding_precision)

        # Check that calling getPelangle on a numpy array of ints yields the expected results
        result_int_nparray = pyCGM.getPelangle(np.array(axisP_ints, dtype='int'), np.array(axisD, dtype='int'))
        np.testing.assert_almost_equal(result_int_nparray, expected, rounding_precision)

        # Check that calling getPelangle on a list of floats yields the expected results
        result_float_list = pyCGM.getPelangle(axisP_floats, axisD)
        np.testing.assert_almost_equal(result_float_list, expected, rounding_precision)

        # Check that calling getPelangle on a numpy array of floats yields the expected results
        result_float_nparray = pyCGM.getPelangle(np.array(axisP_floats, dtype='float'), np.array(axisD, dtype='float'))
        np.testing.assert_almost_equal(result_float_nparray, expected, rounding_precision)