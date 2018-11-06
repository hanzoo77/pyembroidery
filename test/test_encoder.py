from __future__ import print_function

import unittest

from pattern_for_tests import *


class TestEmbpattern(unittest.TestCase):

    def test_encoder_bookend_color_break(self):
        pattern = EmbPattern()
        pattern.add_command(COLOR_BREAK)
        pattern.add_command(COLOR_BREAK)
        pattern.add_command(COLOR_BREAK)
        pattern.add_command(COLOR_BREAK)
        pattern.stitch_abs(0, 0)
        pattern.stitch_abs(0, 100)
        pattern.stitch_abs(100, 100)
        pattern.stitch_abs(100, 0)
        pattern.stitch_abs(0, 0)
        pattern.add_thread("red")
        pattern.add_command(COLOR_BREAK)
        pattern.add_command(COLOR_BREAK)
        pattern.add_command(COLOR_BREAK)
        pattern.add_command(COLOR_BREAK)
        pattern = pattern.get_normalized_pattern()
        self.assertEqual(len(pattern.threadlist), 1)
        self.assertEqual(pattern.count_stitch_commands(COLOR_CHANGE), 0)

    def test_encoder_multiple_internal_breaks(self):
        pattern = EmbPattern()
        pattern.add_command(COLOR_BREAK)
        pattern.stitch_abs(0, 0)
        pattern.stitch_abs(0, 100)
        pattern.stitch_abs(100, 100)
        pattern.stitch_abs(100, 0)
        pattern.stitch_abs(0, 0)
        pattern.add_thread("red")
        pattern.add_command(COLOR_BREAK)
        pattern.add_command(COLOR_BREAK)
        pattern.add_command(COLOR_BREAK)
        pattern.add_command(COLOR_BREAK)
        pattern.stitch_abs(0, 0)
        pattern.stitch_abs(0, 100)
        pattern.stitch_abs(100, 100)
        pattern.stitch_abs(100, 0)
        pattern.stitch_abs(0, 0)
        pattern.add_thread("green")
        pattern.add_command(COLOR_BREAK)
        pattern = pattern.get_normalized_pattern()
        self.assertEqual(pattern.count_stitch_commands(COLOR_CHANGE), 4)
        self.assertEqual(len(pattern.threadlist), 5)

    def test_encoder_colorchange(self):
        pattern = EmbPattern()
        pattern.add_command(COLOR_BREAK)
        pattern.stitch_abs(0, 0)
        pattern.stitch_abs(0, 100)
        pattern.stitch_abs(100, 100)
        pattern.stitch_abs(100, 0)
        pattern.stitch_abs(0, 0)
        pattern.add_thread("red")
        pattern.add_command(COLOR_BREAK)
        pattern.stitch_abs(0, 0)
        pattern.stitch_abs(0, 100)
        pattern.stitch_abs(100, 100)
        pattern.stitch_abs(100, 0)
        pattern.stitch_abs(0, 0)
        pattern.add_thread("green")
        pattern.add_command(COLOR_BREAK)
        pattern.stitch_abs(0, 0)
        pattern.stitch_abs(0, 100)
        pattern.stitch_abs(100, 100)
        pattern.stitch_abs(100, 0)
        pattern.stitch_abs(0, 0)
        pattern.add_thread("blue")
        pattern.add_command(COLOR_BREAK)
        pattern = pattern.get_normalized_pattern()
        self.assertEqual(pattern.count_stitch_commands(COLOR_CHANGE) + 1, len(pattern.threadlist))

    def test_encoder_needleset(self):
        pattern = EmbPattern()
        pattern.add_command(COLOR_BREAK)
        pattern.stitch_abs(0, 0)
        pattern.stitch_abs(0, 100)
        pattern.stitch_abs(100, 100)
        pattern.stitch_abs(100, 0)
        pattern.stitch_abs(0, 0)
        pattern.add_thread("red")
        pattern.add_command(COLOR_BREAK)
        pattern.stitch_abs(0, 0)
        pattern.stitch_abs(0, 100)
        pattern.stitch_abs(100, 100)
        pattern.stitch_abs(100, 0)
        pattern.stitch_abs(0, 0)
        pattern.add_thread("green")
        pattern.add_command(COLOR_BREAK)
        pattern.stitch_abs(0, 0)
        pattern.stitch_abs(0, 100)
        pattern.stitch_abs(100, 100)
        pattern.stitch_abs(100, 0)
        pattern.stitch_abs(0, 0)
        pattern.add_thread("blue")
        pattern.add_command(COLOR_BREAK)
        pattern = pattern.get_normalized_pattern({"thread_change_command": NEEDLE_SET})
        self.assertEqual(pattern.count_stitch_commands(NEEDLE_SET), len(pattern.threadlist))

    def test_transcode_to_self(self):
        pattern = get_shift_pattern()
        from pyembroidery.EmbEncoder import Transcoder
        encoder = Transcoder()
        encoder.transcode(pattern, pattern)
        self.assertNotEquals(len(pattern.stitches), 0)
