from dsml_ai.bayes import beta_posterior, expected_beta


def test_beta_posterior() -> None:
    a, b = beta_posterior(1.0, 1.0, successes=3, failures=2)
    assert a == 4.0 and b == 3.0


def test_expected_beta() -> None:
    assert expected_beta(2.0, 3.0) == 2.0 / 5.0
