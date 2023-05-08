from django.http import JsonResponse

from unidad_fomento.uf_scrapper import UFScrapper
from unidad_fomento.validations import ValidationsUF


def get_uf_values(request):
    fecha_uf = request.GET.get('fecha')
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

    return JsonResponse({'uf': uf_value}, status=200)
