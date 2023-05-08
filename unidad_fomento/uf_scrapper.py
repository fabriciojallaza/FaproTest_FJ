import requests
from bs4 import BeautifulSoup


class UFScrapper:
    def __init__(self):
        self.BASE_URL = "https://www.sii.cl/valores_y_fechas/uf/"

    def get_uf_value(self, fecha):
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
        soup = BeautifulSoup(html, 'html.parser')
        table = soup.find('table', {'class': 'hoja'})
        rows = table.find_all('tr')

        for row in rows:
            cols = row.find_all('td')
            if len(cols) == 3:
                row_fecha = cols[0].text.strip()
                if row_fecha == fecha:
                    uf_value = cols[1].text.strip()
                    return uf_value

        return None
