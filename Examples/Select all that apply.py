import FormMaker as fm

fm.create("Example-Select all that apply")
form = fm.add()
form.select_ata("Select Any Options",['Item1','Item2','Item3'])
print(form.display())