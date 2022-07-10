from app.calculations import add

def test_add():
    print("Testing Add Function")
    sum = add(5,3)
    assert sum == 8

