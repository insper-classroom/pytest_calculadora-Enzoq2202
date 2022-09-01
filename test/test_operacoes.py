from matematica.Calculadora import soma, sub, multiplicacao, divisao, media_lista_valores
import pytest
import numpy as np

@pytest.mark.op_simples
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    assert 12 == soma(v1, v2)



@pytest.mark.op_simples
def test_subtracao_dois_valores():
    v1 = 10.0
    v2 = 7.0
    assert 3 == sub(v1, v2)


@pytest.mark.op_simples
def test_multiplicacao_dois_valores():
    v1 = 10.0
    v2 = 7.0
    assert 70 == multiplicacao(v1, v2)


@pytest.mark.op_simples
def test_divisao_dois_valores():
    v1 = 10.0
    v2 = 5.0
    assert 2 == divisao(v1, v2)


@pytest.mark.exercicio_1
@pytest.mark.op_complexas
def test_media_lista_valores():
    v = [1, 2, 3, 4, 5]
    assert 3 == media_lista_valores(v)


@pytest.mark.exercicio_1
@pytest.mark.op_complexas
def test_media_lista_valores_vazia():
    v = []
    assert 0 == media_lista_valores(v)


@pytest.mark.exercicio_1
@pytest.mark.op_complexas
def test_divisao_por_zero():
    v1 = 10.0
    v2 = 0.0
    assert np.inf == divisao(v1, v2)