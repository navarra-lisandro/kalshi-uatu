import uatu


def test_package_exposes_version() -> None:
    assert uatu.__version__ == "0.0.1"
