import numpy as np
import pytest

from pyk4a import PyK4A


class TestCapture:
    @staticmethod
    @pytest.mark.device
    def test_device_capture_images(device: PyK4A):
        device.open()
        device._start_cameras()
        capture = device.get_capture()
        color = capture.color
        assert color is not None
        depth = capture.depth
        assert depth is not None
        ir = capture.ir
        assert ir is not None
        assert np.array_equal(color, depth) is False
        assert np.array_equal(depth, ir) is False
        assert np.array_equal(ir, color) is False
