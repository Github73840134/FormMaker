# FormMaker
A form maker built with PySimpleGUI
# A quick note
If you want to see a demo of the program you can call FormMaker.demo() to see a demo form with all elements  
Also the way the code is structred when you have more than one multichoice or select all that apply, Duplicate layout messages may appear in the terminal, This is normal. When you recive your response from the form it sometimes looks like this:
```python
'This is a testx': False
```
# Commands
### create()
Clears any existing forms and creates a new one or just creates a new form
### add()
add is a object, add any other commands execpt display to add to the form
#### shortans(prompt)
shortans is a Short answer object- adds a short answer object to the form  
prompt is to be str or int, when making use the appropriate command to convert str->int or int->str  
Example:
```python
 import FormMaker as fm
 form.create("Short answer")
 fm = form.add()
 fm.shortans("hi")
 form.display()
```
Output  
![Image](image/shortans.png)
```python
{'This is a test': 'hi'}
```
#### multichoice(prompt,options)
multichoice is a multiple choice answer object- adds a multiple choice answer object to the form  
prompt is to be str or int, when making use the appropriate command to convert str->int or int->str  
options is to be list, when making use the appropriate command to convert str->int or int->str when adding to the options list  
Example:
```python
 import FormMaker as fm
 form.create("Multi-Choice")
 fm = form.add()
 fm.mutichoice("Multiple Choice",['1','2','3'])
 form.display()
```
Output
```python
{'This is a test': True, 'This is a test0': False, 'This is a test1': False}
```
#### select_ata(prompt,options)
select_ata is a select all that apply object- adds a select all that apply object to the form  
prompt is to be str or int, when making use the appropriate command to convert str->int or int->str  
options is to be list, when making use the appropriate command to convert str->int or int->str when adding to the options list (if needed)  
Example:
```python
 import FormMaker as fm
 form.create("Select all that apply")
 fm = form.add()
 fm.select_ata("Select all that aplpy",['1','2','3'])
 form.display()
```
Output
```python
{'This is a test': True, 'This is a test0': True, 'This is a test1': False}
```
#### 
