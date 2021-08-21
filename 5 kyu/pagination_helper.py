class PaginationHelper:
	def __init__(self, collection, items_per_page):
		self.collection = collection
		self.items_per_page = items_per_page
		
	def item_count(self):
		return sum(self.collection)		

	def page_count(self):
		if len(self.collection) % self.items_per_page == 0:
			return len(self.collection) / self.items_per_page
		else:
			return len(self.collection) / self.items_per_page + 1

	def page_item_count(self, page_index):
		if page_index >= self.page_count():
			return -1
		elif page_index == self.page_count() - 1:
			return len(self.collection) % self.items_per_page or self.items_per_page
		else:
			return self.items_per_page 

	def page_index(self, item_index):
		if item_index >= len(self.collection) or item_index < 0:
			return -1
		else:
			return item_index / self.items_per_page 

