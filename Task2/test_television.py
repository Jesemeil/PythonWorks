import unittest
from television import Television


class TestTelevision(unittest.TestCase):

    def setUp(self):
        self.tv = Television()

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
        self.tv.set_channel(5)
        self.assertEqual(self.tv.get_channel(), 5)

    def test_get_volume(self):
        self.tv.turn_on()
        self.assertEqual(self.tv.get_volume(), 0)

    def test_set_volume(self):
        self.tv.turn_on()
        self.tv.set_volume(50)
        self.assertEqual(self.tv.get_volume(), 50)

    def test_channel_up(self):
        self.tv.turn_on()
        self.tv.set_channel(3)
        self.tv.channel_up()
        self.assertEqual(self.tv.get_channel(), 4)

    def test_channel_down(self):
        self.tv.turn_on()
        self.tv.set_channel(7)
        self.tv.channel_down()
        self.assertEqual(self.tv.get_channel(), 6)

    def test_volume_up(self):
        self.tv.turn_on()
        self.tv.set_volume(10)
        self.tv.volume_up()
        self.assertEqual(self.tv.get_volume(), 11)

    def test_volume_down(self):
        self.tv.turn_on()
        self.tv.set_volume(4)
        self.tv.volume_down()
        self.assertEqual(self.tv.get_volume(), 3)


if __name__ == '__main__':
    unittest.main()
