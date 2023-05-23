import xlrd


def getExcelData(sheet_index, start, end, payload_col, expect_col):
    file_path = './data/比赛测试用例.xls'

    work_book = xlrd.open_workbook(file_path)

    sheet = work_book.sheet_by_index(sheet_index)
    dataList = []
    for i in range(start, end):
        payload = sheet.cell_value(i, payload_col)
        expect = sheet.cell_value(i, expect_col)
        dataList.append((payload, expect))
    return dataList