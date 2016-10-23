from __future__ import absolute_import

from unittest import TestCase

import utils


class WindowIndiciesTestCase(TestCase):

    def test_window_indices_with_gapped_bounds_check_results(self):
        data = [1, 3, 5, 7]
        window = [2, 6]
        self.assertEqual(
            utils.window_indices(data, window),
            (1, 2)
        )