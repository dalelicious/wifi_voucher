# Wifi Users
from . models import Voucher


class VoucherViewModel():


	def get_voucher_id(self, voucherId):
		""" Get voucher by id
		"""

		voucher = Voucher.objects.get(id=voucherId)

		return voucher


	def get_voucher_list(self):
		""" Get all vouchers
		"""

		voucher_list = Voucher.objects.all()

		return voucher_list


	def create_new_voucher(self, code, quantity, max_device, voucher_format, length, duration, price, purge_after):
		""" Create new voucher
		"""

		voucher = Voucher()
		voucher.code = code
		voucher.quantity = quantity
		voucher.max_device = max_device
		voucher.voucher_format = voucher_format
		voucher.length = length
		voucher.duration = duration
		voucher.price = price
		voucher.purge_after = purge_after

		self.save_to_voucher(voucher)		


	def save_to_voucher(self, voucher):
		""" Save voucher to database
		"""

		voucher.save()


	def delete_from_voucher(self, voucherId):
		""" Delete voucher from database
		"""

		voucher = Voucher.objects.get(id=voucherId)
		voucher.delete()