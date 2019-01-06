import unittest

from com.sbk.tag.calc_tag import calc_tag


class TestCalcTag(unittest.TestCase):

    PATH_TO_FILE_1 = "/home/sobik/PycharmProjects/test_data/video/6.1.intro.mp4_download"
    PATH_TO_FILE_2 = "/home/sobik/PycharmProjects/test_data/video/6.2.birthday.mp4_download"

    def test_calc_tag_1(self):
        tag = calc_tag(self.PATH_TO_FILE_1)
        self.assertEqual(tag.hexdigest(), '5b96aece304a1422224f9a41b228416028f9ba26b0d1058f400200f06a589949')

    def test_calc_tag_2(self):
        tag = calc_tag(self.PATH_TO_FILE_2)
        self.assertEqual(tag.hexdigest(), '03c08f4ee0b576fe319338139c045c89c3e8e9409633bea29442e21425006ea8')