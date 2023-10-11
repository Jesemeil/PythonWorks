class Television_1:

    def __init__(self):
        self.on = False
        self.channel = 0
        self.volume = 0

    def turn_on(self):
        self.on = True

    def turn_off(self):
        self.on = False

    def get_channel(self):
        return self.channel

    def set_channel(self, channel):
        if self.on:
            self.channel = channel

    def get_volume(self):
        return self.volume

    def set_volume(self, volume_level):
        if self.on:
            self.volume = volume_level

    def channel_up(self):
        if self.on:
            self.channel += 1

    def channel_down(self):
        if self.on:
            self.channel -= 1

    def volume_up(self):
        if self.on:
            self.volume += 1

    def volume_down(self):
        if self.on:
            self.volume -= 1




