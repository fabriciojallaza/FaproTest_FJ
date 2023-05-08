import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from unidad_fomento.utils.months_spanish import month_name


class UFScrapper:
    def __init__(self):
        self.BASE_URL = "https://www.sii.cl/valores_y_fechas/uf/"

    def get_uf_value(self, fecha):
        """
            Obtiene el valor de la Unidad de Fomento (UF) para una fecha específica.

            Args:
                fecha (datetime.date or str): Fecha para la que se quiere obtener el valor de la UF. Si se entrega como str, debe
                estar en formato YYYY-MM-DD.

            Returns:
                float: Valor de la UF para la fecha especificada.

            Raises:
                ValueError: Si la respuesta del request no es 200 o si no se encuentra el valor de la UF para la fecha indicada.
            """

        # Si fecha es str convertir a datetime.date
        if isinstance(fecha, str):
            fecha = datetime.strptime(fecha, '%Y-%m-%d').date()

        # Realización del request
        url = f"{self.BASE_URL}uf{fecha.year}.htm"
        response = requests.get(url)

        # Validación de la respuesta
        if response.status_code != 200:
            raise ValueError('No se pudo obtener la UF para la fecha especificada.')
        uf_value = self.find_values_uf(response.content, fecha)
        if not uf_value:
            raise ValueError('No se pudo obtener la UF para la fecha especificada.')
        return uf_value

    def find_values_uf(self, html, fecha):
        """
            Encuentra el valor de la UF correspondiente a una fecha específica en el HTML de la página de valores de la UF.

            Args:
                html (bytes): HTML de la página de valores de la UF.
                fecha (datetime.date): Fecha para la que se quiere encontrar el valor de la UF.

            Returns:
                float: Valor de la UF para la fecha especificada.

            Raises:
                ValueError: Si no se encuentra el valor de la UF para la fecha indicada.
            """

        soup = BeautifulSoup(html, 'html.parser')

        # Obtener el tag correspondiente al mes requerido
        meses_div = soup.find("div", {"class": "meses", "id": f"mes_{month_name(fecha.month).lower()}"})

        # Buscar en la tabla el valor correspondiente al día requerido
        for tr in meses_div.find_all("tr"):
            th_list = tr.find_all("th")
            td_list = tr.find_all("td")
            # iterate over th_list and check if element is equal to fecha.day
            for x, th in enumerate(th_list):
                if th.text.strip() == str(fecha.day):
                    # Se encontró el valor de la UF y se retorna el valor de la lsita td_list
                    uf_value = td_list[x].text.strip().replace(".", "").replace(",", ".")
                    return float(uf_value)

        # Si no se encuentra el valor, levantar una excepción
        raise ValueError("No se encontró el valor de la UF para la fecha indicada.")
