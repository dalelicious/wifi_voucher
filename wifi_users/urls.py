from django.urls import path

from . import views

app_name = 'wifi_users'

urlpatterns = [
    path('vouchers/', 						views.vouchers, 		name='vouchers'),
    path('create_voucher/', 				views.create_voucher, 	name='create-voucher'),
    path('delete_voucher/<int:voucherId>', 	views.delete_voucher, 	name='delete-voucher'),
]