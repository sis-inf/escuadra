from escuadra.modulos.geometria.coordenadas import (
    cartesiana_a_cilindrica,
    cartesiana_a_esferica,
    cartesiana_a_polar,
    polar_a_cartesiana,
)


def test_cartesiana_a_polar_triangulo_3_4_5():
    resultado = cartesiana_a_polar(3, 4)

    assert resultado == {"r": 5.0, "theta_grados": 53.13}


def test_cartesiana_a_polar_origen():
    resultado = cartesiana_a_polar(0, 0)

    assert resultado == {"r": 0.0, "theta_grados": 0.0}


def test_cartesiana_a_polar_cuadrante_negativo_normaliza_angulo():
    resultado = cartesiana_a_polar(0, -2)

    assert resultado == {"r": 2.0, "theta_grados": 270.0}


def test_polar_a_cartesiana_eje_y_positivo():
    resultado = polar_a_cartesiana(2, 90)

    assert resultado == {"x": 0.0, "y": 2.0}


def test_cartesiana_a_cilindrica_conserva_z():
    resultado = cartesiana_a_cilindrica(3, 4, 7.125)

    assert resultado == {"r": 5.0, "theta_grados": 53.13, "z": 7.12}


def test_cartesiana_a_esferica_eje_z_positivo():
    resultado = cartesiana_a_esferica(0, 0, 5)

    assert resultado == {"rho": 5.0, "theta_grados": 0.0, "phi_grados": 0.0}


def test_cartesiana_a_esferica_origen():
    resultado = cartesiana_a_esferica(0, 0, 0)

    assert resultado == {"rho": 0.0, "theta_grados": 0.0, "phi_grados": 0.0}
