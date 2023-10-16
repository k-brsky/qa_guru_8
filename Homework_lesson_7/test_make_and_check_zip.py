from zipfile import ZipFile, ZIP_DEFLATED
import os
from os.path import basename
import glob
from openpyxl import load_workbook

def test_make_zip():
    path = 'resources'
    file_dir = os.listdir(path)
    os.mkdir('tmp')
    with ZipFile('tmp/homework.zip', mode='w', compression=ZIP_DEFLATED) as zf:
        # тут в архиве создается папка resources, в ней нужные файлы
        for file in file_dir:
            add_file = os.path.join(path, file)
            zf.write(add_file, basename(add_file))

            # тут тоже сначала resources
        for root, dirs, files in os.walk(path):
            for file in files:
                zf.write(os.path.join(root, file))

        # тут сначала создает папку homework(мб по названию архива), а уже в ней нужные файлы
        zf.write('resources/file_pdf.pdf', basename('resources/file_pdf.pdf'))
        zf.write('resources/file_txt.txt', basename('resources/file_txt.txt'))
        zf.write('resources/test_sheet_xls.xls', basename('resources/test_sheet_xls.xls'))
        zf.write('resources/test_sheet_xlsx.xlsx', basename('resources/test_sheet_xlsx.xlsx'))

def test_check_zip():
    with ZipFile('tmp/homework.zip') as zf:
        text = zf.read('file_txt.txt')
        assert "текстовый файлик" in text

        wb = load_workbook('test_sheet_xlsx.xlsx')
        sheets = wb.sheetnames

