# questions.py tests can be found here

import questions

# Test if conversion to ingeger works as expected


def test_kysy_tiedo_integer(monkeypatch):
    user_input = '100'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna kokonais luku')
    assert question.kysy_tiedo_integer(False) == (100, 'OK', 0, 'Conversion successful')
