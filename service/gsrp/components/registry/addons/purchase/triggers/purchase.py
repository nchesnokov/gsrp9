from orm.trigger import Trigger 

class PurchaseOrder(Trigger):
	def _onCreateBeforeForEachRow(self, r1,context):
		print('Triger For Each Row Before Create')

	def _onCreateAfterForEachRow(self, r1,context):
		print('Triger For Each Row After Create')


	def _onCreateBeforeAll(self, r1,context):
		print('Triger Before Create All')

	def _onCreateAfterAll(self, r1,context):
		print('Triger After Create All')



	def _onWriteBeforeForEachRow(self, r1,r2,context):
		print('Triger For Each Row Before Write')

	def _onWriteAfterForEachRow(self, r1,r2,context):
		print('Triger For Each Row After Write')


	def _onWriteBeforeAll(self, r1,r2,context):
		print('Triger Before Write All')

	def _onWriteAfterAll(self, r1,r2,context):
		print('Triger After Write All')

	def _onUnlinkforeForEachRow(self, r2,context):
		print('Triger For Each Row Before Unlink')

	def _onUnlinkAfterForEachRow(self, r2,context):
		print('Triger For Each Row After Unlink')


	def _onUnlinkBeforeAll(self, r2,context):
		print('Triger Before Unlink All')

	def _onUnlinkAfterAll(self, r2,context):
		print('Triger After Unlink All')


	def _onReadBeforeForEachRow(self, r1,context):
		print('Triger For Each Row Before Read')

	def _onReadAfterForEachRow(self, r1,context):
		print('Triger For Each Row After Read')


	def _onReadBeforeAll(self, r1,context):
		print('Triger Before Read All')

	def _onReadAfterAll(self, r1,context):
		print('Triger After Read All')

