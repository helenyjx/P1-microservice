from app import change
def test_change():
    assert [{5: 'Quarters'}, {1: 'Nickels'}, {4: 'Pennies'}] == change(1.34)