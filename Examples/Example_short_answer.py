import FormMaker as fm

fm.create("Short Answer example")
form = fm.add()
form.shortans("Whats your name?")
print(form.display())