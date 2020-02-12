from .views import (
    GastoSegmentoListView, gastosPorMesView, AutoCompleteView,
    SegmentoCRUD, GastoCRUD, HoraTrabalhadaCRUD, RabbiitCRUD,
    CityCRUD, ComercioCRUD, guiaBolsoView, PecasListView,
    PecasCreateView, PecasEditView
)

from django.urls import path, include

segmento_view = SegmentoCRUD()
rabbiit_view = RabbiitCRUD()
gasto_view = GastoCRUD()
horatrabalhada_view = HoraTrabalhadaCRUD()
localidade_view = CityCRUD()
# pecas_view = PecasCRUD()
comercio_view = ComercioCRUD()

urlpatterns = [
    path('', include(segmento_view.get_urls())),
    path('', include(rabbiit_view.get_urls())),
    path('', include(gasto_view.get_urls())),
    path('', include(horatrabalhada_view.get_urls())),
    path('', include(localidade_view.get_urls())),
    path('website/pecas/list/', PecasListView.as_view(), name="website_pecas_list"),
    path('website/pecas/create/', PecasCreateView.as_view(), name="website_pecas_create"),
    path(r'website/pecas/edit/<pk>/', PecasEditView.as_view(), name="website_pecas_edit"),
    path('', include(comercio_view.get_urls())),
    path('gasto/autocomplete/', AutoCompleteView.as_view()),
    path('gastosPorSegmento/', GastoSegmentoListView.as_view(), name="gastosPorSegmento"),
    path('gastosPorMes/', gastosPorMesView, name="gastosPorMes"),
    path('guiaBolso/', guiaBolsoView, name="guiaBolso"),
    path('select2/', include('django_select2.urls')),
]
