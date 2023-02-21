# author: Dabana Intenque
from PySide6.QtWidgets import QLabel, QLineEdit


def prefix(self):
    pfx_label = QLabel('Prefix:', self)
    pfx_field = QLineEdit(self)

    # pfx_label.resize(100, 200)
    pfx_label.move(700, 50)

    pfx_field.resize(200, 25)
    pfx_field.move(750, 45)


def first_name(self):
    first_name_label = QLabel('First Name:', self)
    first_name_field = QLineEdit(self)

    first_name_label.move(670, 100)

    first_name_field.resize(200, 25)
    first_name_field.move(750, 95)


def last_name(self):
    last_name_label = QLabel('Last Name:', self)
    last_name_field = QLineEdit(self)

    last_name_label.move(670, 150)

    last_name_field.resize(200, 25)
    last_name_field.move(750, 145)


def title(self):
    title_label = QLabel('title:', self)
    title_field = QLineEdit(self)

    title_label.move(710, 200)

    title_field.resize(200, 25)
    title_field.move(750, 195)


def organization_name(self):
    organization_name_label = QLabel('Organization Name:', self)
    organization_name_field = QLineEdit(self)

    organization_name_label.move(620, 250)

    organization_name_field.resize(200, 25)
    organization_name_field.move(750, 245)
