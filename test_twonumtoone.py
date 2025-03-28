from twonumtoone import *

def test_two2one():
    assert two2one([3],[[0,2,4]]) == 1
    assert two2one([3,9],[[0,2,4],[0,5,17]]) == 9
    assert two2one([1],[[1,0.5,1.5]]) == 5
    assert two2one([3,9],[[1,1.2,4.7],[1,5.4,17.4]]) == 1278
