class Television:
    """
    A class to represent a Television with basic functionalities like power, mute, volume, and channel control.
    """

    # Class variables
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initialize the Television with default settings.
        The TV starts off, unmuted, at minimum volume, and on the minimum channel.
        """
        self.__status: bool = False  # TV is off by default
        self.__muted: bool = False  # TV is unmuted by default
        self.__volume: int = Television.MIN_VOLUME  # Default volume
        self.__channel: int = Television.MIN_CHANNEL  # Default channel
        self.__previous_volume: int = Television.MIN_VOLUME  # To store volume before muting

    def power(self) -> None:
        """
        Toggle the power status of the TV.
        If the TV is off, turn it on. If it is on, turn it off.
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mute or unmute the TV if it is on.
        - When muting, the current volume is stored, and the volume is set to 0.
        - When unmuting, the volume is restored to its previous value.
        """
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

    def channel_up(self) -> None:
        """
        Increase the channel if the TV is on.
        - If the TV is at the maximum channel, wrap around to the minimum channel.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        Decrease the channel if the TV is on.
        - If the TV is at the minimum channel, wrap around to the maximum channel.
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """
        Increase the volume if the TV is on.
        - If the TV is muted, it will be unmuted and the volume restored before increasing.
        - The volume will not exceed the maximum volume.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decrease the volume if the TV is on.
        - If the TV is muted, it will be unmuted and the volume restored before decreasing.
        - The volume will not go below the minimum volume.
        """
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """
        Return a string representation of the Television's current state.
        Example: "Power= True, Channel= 3, Volume= 1"
        """
        return f"Power= {self.__status}, Channel= {self.__channel}, Volume= {self.__volume}"
