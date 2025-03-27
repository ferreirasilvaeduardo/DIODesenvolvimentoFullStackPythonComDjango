from contacts.forms import NameForm


# Give
# When
# Then
def test_name_form_sucess():
    # Give
    data = {}
    data["your_name"] = "Jonh"
    form = NameForm(data=data)

    # When
    result = form.is_valid()

    # Then
    assert result is True


def test_name_form_fail():
    ...
    # Give
    data = {}
    # data["your_name"] = "Jonh"
    form = NameForm(data=data)

    # When
    is_valid = form.is_valid()
    is_bound = form.is_bound

    # Then
    assert is_valid is False
    assert is_bound is True


def test_name_form_your_name_max_length():
    # Give
    data = {}
    data["your_name"] = "Jonh" * 50
    form = NameForm(data=data)
    # When
    is_valid = form.is_valid()
    # Then
    assert is_valid is False
    assert "100" in "".join(form.errors["your_name"])
