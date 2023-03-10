# questions.py tests can be found here

import questions

# Test if conversion to ingeger works as expected


'''def test_kysy_tiedo_integer(monkeypatch):
    user_input = '100'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna kokonaisluku')
    assert question.kysy_tiedo_integer(False) == (100, 'OK', 0, 'Conversion successful')

def test_kysy_tiedo_integer2(monkeypatch):
    user_input = '100 v'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna kokonaisluku')
    assert question.kysy_tiedo_integer(False) == (0, 'Error', 1, "invalid literal for int() with base 10: '100 v'")'''

# Test static conversion method to integer

def test_static_kysy_tiedo_integer(monkeypatch):
    user_input = '100'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    assert questions.Question.kysy_tiedo_integer('Anna kokonaisluku', False) == (100, 'OK', 0, 'Conversion successful')

def test_kysy_tiedo_float(monkeypatch):
    user_input = '72.5'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna liukuluku')
    assert question.kysy_tiedo_float(False) == (72.5, 'OK', 0, 'Conversion successful')

def test_kysy_tiedo_float2(monkeypatch):
    user_input = '72.5 kg'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Anna liukuluku')
    assert question.kysy_tiedo_float(False) == (0, 'Error', 1, "could not convert string to float: '72.5 kg'")

def test_kysy_tiedo_float3(monkeypatch):
    user_input = '67,5'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Annl liukuluku')
    assert question.kysy_tiedo_float(False) == (0, 'Error', 1, "could not convert string to float: '67,5'")

def test_kysy_tiedo_boolean(monkeypatch):
    user_input = 'Y'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Y tai N ?')
    assert question.kysy_tiedo_boolean('Y', 'N', False) == (True, 'OK', 0, 'Conversion successful')


def test_kysy_tiedo_boolean2(monkeypatch):
    user_input = 'N'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Y tai N ?')
    assert question.kysy_tiedo_boolean('Y', 'N', False) == (False, 'OK', 0, 'Conversion successful')

def test_kysy_tiedo_boolean3(monkeypatch):
    user_input = 'M'
    monkeypatch.setattr('builtins.input', lambda _: user_input)
    question = questions.Question('Y tai N ?')
    assert question.kysy_tiedo_boolean('Y', 'N', False) == ('N/A', 'Error', 1, 'unable to convert boolean')

