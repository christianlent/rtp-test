from rtpdir.rtpmodule import raisetopower

def test_rtp_2_to_10():
    assert raisetopower(2, 10) == 1024

def test_rtp_10_to_10():
    assert raisetopower(10, 10) == 10000000000

def test_rtp_0_to_0():
    assert raisetopower(0,0) == 1