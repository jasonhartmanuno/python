from television import Television


def test_init_defaults():
    tv = Television()
    assert str(tv) == "Power = False, Channel = 0, Volume = 0"

def test_power_on_off():
    tv = Television()
    tv.power()
    assert "Power = True" in str(tv)
    tv.power()
    assert "Power = False" in str(tv)

def test_mute_when_on_with_volume():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 0"

def test_unmute_when_on_restores_display_volume():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.mute()
    assert str(tv) == "Power = True, Channel = 0, Volume = 1"

def test_mute_when_off_does_nothing():
    tv = Television()
    before = str(tv)
    tv.mute()
    after = str(tv)
    assert before == after == "Power = False, Channel = 0, Volume = 0"

def test_channel_up_when_off_does_nothing():
    tv = Television()
    tv.channel_up()
    assert "Channel = 0" in str(tv)

def test_channel_up_when_on_increases_channel():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert "Channel = 1" in str(tv)

def test_channel_up_wraps_past_max():
    tv = Television()
    tv.power()
    for _ in range(Television.MAX_CHANNEL + 1):
        tv.channel_up()
    assert "Channel = 0" in str(tv)

def test_channel_down_when_off_does_nothing():
    tv = Television()
    tv.channel_down()
    assert "Channel = 0" in str(tv)

def test_channel_down_when_on_decreases_channel():
    tv = Television()
    tv.power()
    tv.channel_up()
    tv.channel_down()
    assert "Channel = 0" in str(tv)

def test_channel_down_wraps_below_min():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert f"Channel = {Television.MAX_CHANNEL}" in str(tv)

def test_volume_up_when_off_does_nothing():
    tv = Television()
    tv.volume_up()
    assert "Volume = 0" in str(tv)

def test_volume_up_when_on_increases_volume():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert "Volume = 1" in str(tv)

def test_volume_up_when_muted_unmutes_and_increases():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    tv.volume_up()
    assert "Power = True, Channel = 0, Volume = 2" in str(tv)

def test_volume_up_stops_at_max():
    tv = Television()
    tv.power()
    for _ in range(5):
        tv.volume_up()
    assert f"Volume = {Television.MAX_VOLUME}" in str(tv)

def test_volume_down_when_off_does_nothing():
    tv = Television()
    tv.volume_down()
    assert "Volume = 0" in str(tv)


def test_volume_down_when_on_decreases_volume():
    tv = Television()
    tv.power()
    for _ in range(3):
        tv.volume_up()
    tv.volume_down()
    assert f"Volume = {Television.MAX_VOLUME - 1}" in str(tv)

def test_volume_down_when_muted_unmutes_and_decreases():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.mute()
    tv.volume_down()
    assert "Power = True, Channel = 0, Volume = 1" in str(tv)

def test_volume_down_stops_at_min():
    tv = Television()
    tv.power()
    tv.volume_down()
    assert f"Volume = {Television.MIN_VOLUME}" in str(tv)