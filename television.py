class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initialize the Television with default settings."""
        self.__status = False  # TV is off by default
        self.__muted = False  # TV is unmuted by default
        self.__volume = Television.MIN_VOLUME  # Default volume
        self.__channel = Television.MIN_CHANNEL  # Default channel

    def power(self):
        """Toggle the power status of the TV."""
        self.__status = not self.__status

    def mute(self):
        """Mute or unmute the TV if it is on."""
        if self.__status:
            if self.__muted:
                # If unmuting, restore the previous volume
                self.__volume = self.__previous_volume
                self.__muted = False
            else:
                # If muting, save the current volume and set volume to 0
                self.__previous_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
                self.__muted = True

    def channel_up(self):
        """Increase the channel if the TV is on, cycling back to MIN_CHANNEL if MAX_CHANNEL is exceeded."""
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """Decrease the channel if the TV is on, cycling back to MAX_CHANNEL if MIN_CHANNEL is exceeded."""
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """Increase the volume if the TV is on and unmute it if muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """Decrease the volume if the TV is on and unmute it if muted."""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        """Return a string representation of the Television's current state."""
        return f"Power= {self.__status}, Channel= {self.__channel}, Volume= {self.__volume}"
