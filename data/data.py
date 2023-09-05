from dataclasses import dataclass


@dataclass
class Person:
    full_name: str = None
    firstname: str = None
    lastname: str = None
    salary: int = None
    age: int = None
    department: str = None
    email: str = None
    current_address: str = None
    permanent_address: str = None
    mobile: str = None

@dataclass
class Color:
    color_name: list = None


@dataclass
class Date:
    day: str = None
    month: str = None
    year: str = None
    time: str = None


@dataclass
class Value:
    value_name: str = None


@dataclass
class Select:
    select_one_name: str = None

@dataclass
class Product:
    product_name: list = None


@dataclass
class Type:
    type_name: list = None

@dataclass
class Kyc:
    kyc_name: list = None