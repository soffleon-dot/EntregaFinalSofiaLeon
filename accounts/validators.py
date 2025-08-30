import re
from django.core.exceptions import ValidationError
class LetterNumberValidator:
    def validate(self, password, user=None):
        if not re.search(r'[A-Za-z]', password) or not re.search(r'\d', password):
            raise ValidationError('La contraseña debe incluir al menos una letra y un número.')
    def get_help_text(self):
        return 'La contraseña debe tener al menos una letra y un número.'
