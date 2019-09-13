from django.urls import path
from .views import HomePageView, BlueView, OrchidView, ManEaterView

urlpatterns = [

		path('',HomePageView.as_view(), name='home'),
		path('orchid/',OrchidView.as_view(), name='orchid'),
		path('blue/',BlueView.as_view(), name='blue'),
		path('maneater/',ManEaterView.as_view(),name='maneater'),
		


			 ]