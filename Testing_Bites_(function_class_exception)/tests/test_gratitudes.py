from lib.gratitudes import Gratitudes

def test_add_adds_one_item():
    gratitudes = Gratitudes()
    gratitudes.add("the newts in my pond")
    assert gratitudes.gratitudes == ["the newts in my pond"]

def test_add_adds_two_items():
    gratitudes = Gratitudes()
    gratitudes.add("the newts in my pond")
    gratitudes.add("Greggs' sausage bean and cheese melt")
    assert gratitudes.gratitudes == ["the newts in my pond", "Greggs' sausage bean and cheese melt"]

def test_format_returns_formatted_single_gratitude():
    gratitudes = Gratitudes()
    gratitudes.add("the newts in my pond")
    assert gratitudes.format() == "Be grateful for: the newts in my pond"

def test_format_returns_formatted_two_gratitudes():
    gratitudes = Gratitudes()
    gratitudes.add("the newts in my pond")
    gratitudes.add("Greggs' sausage bean and cheese melt")
    assert gratitudes.format() == "Be grateful for: the newts in my pond, Greggs' sausage bean and cheese melt"


