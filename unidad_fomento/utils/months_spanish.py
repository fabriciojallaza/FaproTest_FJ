def month_name(month_num: int) -> str:
    """
    Given a month number (1-12), returns the corresponding name of the month in Spanish.

    Args:
        month_num (int): The month number (1-12).

    Returns:
        str: The name of the month in Spanish.
    """
    month_names = {
        1: 'Enero',
        2: 'Febrero',
        3: 'Marzo',
        4: 'Abril',
        5: 'Mayo',
        6: 'Junio',
        7: 'Julio',
        8: 'Agosto',
        9: 'Septiembre',
        10: 'Octubre',
        11: 'Noviembre',
        12: 'Diciembre'
    }
    return month_names.get(month_num, '')