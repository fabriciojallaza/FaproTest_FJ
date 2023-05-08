from datetime import datetime


class ValidationsUF:
    def validar_fecha(self, fecha):
        if not fecha:
            raise ValueError('Fecha no especificada.')
        try:
            fecha = datetime.strptime(fecha, '%Y-%m-%d').date()
        except ValueError:
            raise ValueError('Formato de fecha inválido.')
        if fecha < datetime(2013, 1, 1).date():
            raise ValueError('La fecha mínima permitida es 01-01-2013.')
        return fecha
