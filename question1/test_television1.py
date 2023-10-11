import unittest
from television1 import Television_1


class TestTelevision_1(unittest.TestCase):

    def setUp(self):
        self.tv = Television_1()

    def test_turn_on(self):
        self.tv.turn_on()
        self.assertTrue(self.tv.on)

    def test_turn_off(self):
        self.tv.turn_on()
        self.tv.turn_off()
        self.assertFalse(self.tv.on)

    def test_get_channel(self):
        self.assertEqual(self.tv.get_channel(), 0)

    def test_set_channel(self):
        self.tv.turn_on()
        self.tv.set_channel(25)
        self.assertEqual(self.tv.get_channel(), 25)

    def test_get_volume(self):
        self.tv.turn_on()
        self.assertEqual(self.tv.get_volume(), 0)

    def test_set_volume(self):
        self.tv.turn_on()
        self.tv.set_volume(75)
        self.assertEqual(self.tv.get_volume(), 75)

    def test_channel_up(self):
        self.tv.turn_on()
        self.tv.set_channel(35)
        self.tv.channel_up()
        self.assertEqual(self.tv.get_channel(), 36)

    def test_channel_down(self):
        self.tv.turn_on()
        self.tv.set_channel(55)
        self.tv.channel_down()
        self.assertEqual(self.tv.get_channel(), 54)

    def test_volume_up(self):
        self.tv.turn_on()
        self.tv.set_volume(50)
        self.tv.volume_up()
        self.assertEqual(self.tv.get_volume(), 51)

    def test_volume_down(self):
        self.tv.turn_on()
        self.tv.set_volume(44)
        self.tv.volume_down()
        self.assertEqual(self.tv.get_volume(), 43)



