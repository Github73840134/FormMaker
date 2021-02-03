import FormMaker as fm

fm.create("Example-Multichoice")
form = fm.add()
form.multichoice("Choose any option",[''])
print(form.display())