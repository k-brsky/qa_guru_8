import dataclasses
import datetime


@dataclasses.dataclass
class User:
    name: str
    last_name: str
    email: str
    gender: str
    phone_number: str
    date_of_birth: datetime.date
    subject: str
    hobby: str
    photo: str
    current_addres: str
    state: str
    city: str