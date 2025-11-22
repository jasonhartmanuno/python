class Television:
    """
    A simple class to represent a television device
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """Initialize default TV settings"""
        self.__muted = False
        self.__status = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL

    def power(self):
        """Turn the TV on and off"""
        self.__status = not self.__status

    def mute(self):
        """Toggle mute on and off"""
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self):
        """Increase channel or loop back to minimum channel"""
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self):
        """Decrease channel or loop back to maximum channel"""
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        """Increase volume and automatically unmute"""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        """decrease volume and automatically unmute"""
        if self.__status:
            if self.__muted:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return formatted TV status."""
        display_volume = Television.MIN_VOLUME if self.__muted else self.__volume
        return f"Power = {self.__status}, Channel = {self.__channel}, Volume = {display_volume}"