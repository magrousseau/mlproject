from mlproject.distance import haversine

def test_haversine():
    assert haversine(48.865070, 2.380009, 48.8412123, 2.3395144) != 0

def test_haversine_type():
    assert type(haversine(48.865070, 2.380009, 48.8412123, 2.3395144)) == float
