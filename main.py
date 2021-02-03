import FormMaker as fm

fm.create("Test")
form = fm.add()
form.select_ata("This is a test",['1','2','3'])
print(form.display())