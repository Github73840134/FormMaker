import FormMaker as fm

fm.create("Test")
form = fm.add()
form.uploadfile("Upload File")
print(form.display())