# Django
from django.http 		import HttpResponse
from django.shortcuts 	import render
from django.shortcuts 	import redirect

# Wifi Users
from . viewmodels 		import VoucherViewModel


voucher = VoucherViewModel()


def vouchers(request):

    voucher_list = voucher.get_voucher_list()

    return render(request, 'wifi_users/vouchers.html',
                 {'voucher_list' : voucher_list})


def create_voucher(request):

	if request.method == "GET":

		return render(request, 'wifi_users/create_voucher.html')

	else:

		code = request.POST['code']
		quantity = request.POST['quantity']
		max_device = request.POST['max_device']
		voucher_format = request.POST['voucher_format']
		length = request.POST['length']
		duration = request.POST['duration']
		price = request.POST['price']
		purge_after = request.POST['purge_after']

		voucher.create_new_voucher(code, quantity, max_device, voucher_format, length, duration, price, purge_after)

		return redirect('wifi_users:vouchers')


def delete_voucher(request, voucherId):

	voucher.delete_from_voucher(voucherId)

	return redirect('wifi_users:vouchers')