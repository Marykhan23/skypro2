from src.decorators import divide_number


def test_log_decorator_success(capsys):
    divide_number(3, 1)
    captured = capsys.readouterr()
    print(captured)
    assert "divide_number OK" in captured.out


def test_log_decorator_divide_by_zero(capsys):
    try:
        divide_number(3, 0)
    except Exception:
        captured = capsys.readouterr()
        assert "divide_number error: division by zero" in captured.out


def test_log_decorator_unsupported_operand_type(capsys):
    try:
        divide_number(3, "I")
    except Exception:
        captured = capsys.readouterr()
        assert "divide_number error: unsupported operand type" in captured.out
