import FormMaker as fm

fm.create("Test")
form = fm.add()
form.uploadfile_rt("Upload File",(('Python Files','*.py'),))
print(form.display())