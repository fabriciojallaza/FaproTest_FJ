from django.http import JsonResponse

from unidad_fomento.lib.uf_scrapper import UFScrapper
from unidad_fomento.lib.validations import ValidationsUF


def get_uf_values(request):
    """
        Obtiene el valor de la UF para una fecha determinada a través de una solicitud HTTP GET.

        Args:
            request: objeto HttpRequest que contiene los parámetros de la solicitud HTTP GET.

        Returns:
            Un objeto JsonResponse con el valor de la UF para la fecha especificada, o un mensaje de error en caso de que
            ocurra alguna excepción.

        Raises:
            ValueError: si la fecha proporcionada no es válida o si no se puede obtener el valor de la UF para la fecha especificada.
        """
    # Obtener la fecha de la solicitud HTTP GET
    fecha_uf = request.GET.get('fecha')

    # Crear instancias de las clases ValidationsUF y UFScrapper
    uf_scrapper = UFScrapper()
    validations_uf = ValidationsUF()

    # Validación de fecha
    try:
        fecha_uf = validations_uf.validar_fecha(fecha_uf)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=400)

    # Obtención de la UF
    try:
        uf_value = uf_scrapper.get_uf_value(fecha_uf)
    except ValueError as e:
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'uf_value': uf_value}, status=200)
