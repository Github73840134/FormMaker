import FormMaker as fm

fm.create("Hello")
form = fm.add()
form.shortans("This is a test")
form.multichoice('Pick one',['1','2','3'])
form.select_ata("Select All that apply",['a','b'])
form.uploadfile_rt("Upload",(("Python Files", "*.py"),))
print(form.display())