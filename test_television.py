import pytest
from television import Television

def test_init():
    """Test the initialization of the Television."""
    tv = Television()
    assert str(tv) == "Power= False, Channel= 0, Volume= 0"

def test_power():
    """Test the power method."""
    tv = Television()
    tv.power()
    assert str(tv) == "Power= True, Channel= 0, Volume= 0"
    tv.power()
    assert str(tv) == "Power= False, Channel= 0, Volume= 0"

def test_mute():
    """Test the mute method."""
    tv = Television()
    tv.mute()
    assert str(tv) == "Power= False, Channel= 0, Volume= 0"  # Mute does nothing if the TV is off

    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power= True, Channel= 0, Volume= 1"  # Volume stays the same when muted

    tv.mute()
    assert str(tv) == "Power= True, Channel= 0, Volume= 1"  # Unmuting restores volume

def test_channel_up():
    """Test the channel_up method."""
    tv = Television()
    tv.channel_up()
    assert str(tv) == "Power= False, Channel= 0, Volume= 0"  # Channel does not change if the TV is off

    tv.power()
    tv.channel_up()
    assert str(tv) == "Power= True, Channel= 1, Volume= 0"

    tv.channel_up()
    tv.channel_up()
    tv.channel_up()  # Should wrap around to the minimum channel
    assert str(tv) == "Power= True, Channel= 0, Volume= 0"

def test_channel_down():
    """Test the channel_down method."""
    tv = Television()
    tv.channel_down()
    assert str(tv) == "Power= False, Channel= 0, Volume= 0"  # Channel does not change if the TV is off

    tv.power()
    tv.channel_down()
    assert str(tv) == "Power= True, Channel= 3, Volume= 0"  # Wraps around to max channel

def test_volume_up():
    """Test the volume_up method."""
    tv = Television()
    tv.volume_up()
    assert str(tv) == "Power= False, Channel= 0, Volume= 0"  # Volume does not change if the TV is off

    tv.power()
    tv.volume_up()
    assert str(tv) == "Power= True, Channel= 0, Volume= 1"

    tv.volume_up()
    tv.volume_up()  # Should stay at max volume
    assert str(tv) == "Power= True, Channel= 0, Volume= 2"

    tv.mute()
    tv.volume_up()  # Should unmute and increase volume
    assert str(tv) == "Power= True, Channel= 0, Volume= 2"

def test_volume_down():
    """Test the volume_down method."""
    tv = Television()
    tv.volume_down()
    assert str(tv) == "Power= False, Channel= 0, Volume= 0"  # Volume does not change if the TV is off

    tv.power()
    tv.volume_up()
    tv.volume_up()  # Set to max volume
    tv.volume_down()
    assert str(tv) == "Power= True, Channel= 0, Volume= 1"

    tv.volume_down()
    tv.volume_down()  # Should stay at min volume
    assert str(tv) == "Power= True, Channel= 0, Volume= 0"

    tv.mute()
    tv.volume_down()  # Should unmute and decrease volume
    assert str(tv) == "Power= True, Channel= 0, Volume= 0"
