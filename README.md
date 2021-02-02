# FormMaker
A form maker built with PySimpleGUI
# A quick note
If you want to see a demo of the program you can call FormMaker.demo() to see a demo form with all elements
# Commands
### create()
Clears any existing forms and creates a new one or just creates a new form
### add()
add is a object, add any other commands execpt display to add to the form
#### shortans(prompt)
shortans is a Short answer object- adds a short answer object to the form
prompt is to be str or int, when miking use the appropriate commadn to convert str->int or int->str
Example:
```python
 import FormMaker as fm
 form.create("Short answer")
 fm = form.add()
 fm.shortans("hi")
 
```
