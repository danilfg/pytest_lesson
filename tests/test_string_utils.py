from contextlib import nullcontext

import pytest

from src.string_utils import StringUtils


class TestStringUtils:
    @pytest.mark.parametrize(
        ("input_str", "expected"),
        [
            ("abc", "cba"),
            ("", ""),
            ("123", "321"),
        ],
    )
    def test_reverse_string(self, input_str, expected):
        utils = StringUtils()
        assert utils.reverse_string(input_str) == expected

    class TestStringUtils:
        @pytest.mark.parametrize(
            ("input_str", "expected"),
            [
                ("abc", nullcontext()),
                (12345, pytest.raises(TypeError)),
                (None, pytest.raises(TypeError)),
            ],
        )
        def test_reverse_string_errors(self, input_str, expected):
            utils = StringUtils()
            with expected:
                utils.reverse_string(input_str)

    @pytest.mark.parametrize(
        ("full_name", "expected"),
        [
            ("Daniil Nikolaev", "DN"),
            ("Ivan Ivanov", "II"),
            ("", pytest.raises(ValueError)),
        ],
    )
    def test_get_initials(self, full_name, expected):
        utils = StringUtils()
        if isinstance(expected, str):
            assert utils.get_initials(full_name) == expected
        else:
            with expected:
                utils.get_initials(full_name)
