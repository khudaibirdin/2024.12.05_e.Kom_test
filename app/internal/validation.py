import datetime
import re


class Validation():
    def validate(self, data:str) -> bool:
        if self._is_date(data):
            return "date"
        if self._is_phone_number(data):
            return "phone"
        if self._is_email(data):
            return "email"
        return "text"
    
    def _is_email(self, data:str) -> bool:
        "ilnurjick@mail.ru"
        email_temp = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(email_temp, data)
    
    def _is_phone_number(self, data:str) -> bool:
        phone_number_temp = r'^\+\d{11}$'
        return re.match(phone_number_temp, data)
    
    def _is_date(self, data:str) -> bool:
        date_temps = ["%d.%m.%Y", "%Y-%m-%d"]
        for temp in date_temps:
            try:
                datetime.datetime.strptime(data, temp) 
                return True
            except ValueError:
                continue
        return False
        