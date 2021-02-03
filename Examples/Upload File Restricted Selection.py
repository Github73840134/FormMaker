import FormMaker as fm

fm.create("Examples-Upload File Restricted Selection")
form = fm.add()
form.uploadfile_rt("Upload File",(('Python Files','*.py'),))
print(form.display())