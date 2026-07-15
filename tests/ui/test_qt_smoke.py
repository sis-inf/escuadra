from PySide6.QtWidgets import QWidget


def test_qwidget_can_be_created(qtbot):
    widget = QWidget()

    qtbot.addWidget(widget)

    assert widget is not None
