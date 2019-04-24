# coding=utf-8
# 
from xlrd import open_workbook
from functools import partial
from itertools import takewhile
import logging
logger = logging.getLogger(__name__)



def generateHolding(ws, startRow=0):
	"""
	A generator function.

	[Worksheet] ws, [Int] startRow => 
		An iterator for values from each line in that holding section.

	"""
	def endOfHolding(value):
		if isinstance(value, str) and value.startswith('Exposure total'):
			return True
		else:
			return False


	row = startRow
	while (row < ws.nrows and not endOfHolding(cellValue(ws, row, 0))):
		yield map(partial(cellValue, ws, row), range(ws.ncols))
		row = row + 1

	# if the function arrives here, the generator will be considered empty.



def getHeaders(ws, row):
	"""
	[Worksheet] ws, [Int] row => [List] headers

	A header cannot be an empty string.
	"""
	return list(takewhile(lambda v: v != ''
						 , map(partial(cellValue, ws, row), range(ws.ncols))))



def cellValue(ws, row, col):
	"""
	[WorkSheet] ws, [Int] row, [Int] col => [Object] value
	"""
	value = ws.cell_value(row, col)
	if isinstance(value, str):
		return value.strip()
	else:
		return value



def position(headers, cellValues):
	"""
	[List] headers, [Iterator] cellValues => [Dictionary] position
	"""
	return dict(zip(headers, cellValues))



if __name__ == '__main__':
	import logging.config
	logging.config.fileConfig('logging.config', disable_existing_loggers=False)

	wb = open_workbook('samples\\Repo Exposure Trades and Collateral Position.xlsx')
	ws = wb.sheet_by_index(0)
	headers = getHeaders(ws, 11)
	# print(headers)

	for p in map(partial(position, headers), generateHolding(ws, 12)):
		print(p)