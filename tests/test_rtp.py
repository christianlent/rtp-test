from rtpdir.rtpmodule import raisetopower

def test_rtp_2_to_10():
    assert raisetopower(2, 10) == 1024

def test_rtp_10_to_10():
    assert raisetopower(10, 10) == 10000000000