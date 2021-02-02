import PySimpleGUI as sg
global formname
formname = ''
form = [[]]
def create(name):
	form.clear()
	global formname
	formname = name
def create_pages(name,pages):
	form = [[]]
	global formname
	formname = name
class add:
	@staticmethod
	def shortans(prompt):
		form.append([sg.Text(prompt)])
		form.append([sg.Input("",key=prompt)])
	@staticmethod
	def multichoice(prompt,options):
		form.append([sg.Text(prompt)])
		for i in range(0,len(options)):
			form.append([sg.Radio(options[i],prompt,key=prompt)])
	@staticmethod
	def select_ata(prompt,options):
		form.append([sg.Text(prompt)])
		for i in range(0,len(options)):
			form.append([sg.Checkbox(options[i],key=prompt)])
	@staticmethod
	def uploadfile(prompt):
		form.append([sg.Text(prompt)])
		form.append([sg.FileBrowse(key=prompt)])
	@staticmethod
	def uploadfile_rt(prompt, ft):
		form.append([sg.Text(prompt)])
		form.append([sg.FileBrowse(file_types=ft)])
	@staticmethod
	def display():
		form.append([sg.Button("Submit")])
		global formname
		window = sg.Window(formname, form)
		while True:
			event ,values = window.read(timeout=0)
			if event == "Submit":
				window.close()
				return values
def ver():
	return [["Version","1.0"],["Name","FormMaker"]]
def brief():
	return "FormMaker Version 1.0\nNew Features\n- File uploading\n- Short answers\n- Multichoice\n- Select all that apply"
