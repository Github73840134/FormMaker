import PySimpleGUI as sg
import time
global formname
formname = ''
form = [[]]
def create(name):
	form.clear()
	global formname
	formname = name
class add:
	"""
	Class add: call this and any other function to add to the form
	"""
	@staticmethod
	def shortans(prompt):
		"""
		Adds a multichoice part to form
		:param prompt (str): Question Text
		"""
		form.append([sg.Text(prompt)])
		form.append([sg.Input("",key=prompt)])
	@staticmethod
	def multichoice(prompt,options):
		"""
		Adds a multichoice part to form.\n
		:param prompt (str): Question Text\n 
		:param options (list) (str): Multiple Choice options\n
		:retrurns (On Submission): '(prompt/prompt(item number))': (False/True)\n 
		:example return {...,...,...,'Multiple Choice0': False,'Multiple Choice1': False,'Multiple Choice3': True}
		"""
		form.append([sg.Text(prompt)])
		for i in range(0,len(options)):
			form.append([sg.Radio(options[i],prompt,key=prompt)])
	@staticmethod
	def select_ata(prompt,options):
		"""
		Adds a Select all that apply option to the form.\n
		:param prompt (str): Question Text\n
		:param options (list) (str): Select all that apply options\n
		:retrurns (On Submission): '(prompt/prompt(item number))': (False/True)\n
		:example return {...,...,...,'Select all apply0': False,'Select all apply1': False,'Select all apply3': True}
		"""
		form.append([sg.Text(prompt)])
		for i in range(0,len(options)):
			form.append([sg.Checkbox(options[i],key=prompt)])
	@staticmethod
	def uploadfile(prompt):
		"""
		:param prompt (str): Text to show\n
		:returns: prompt:'filename'
		"""
		form.append([sg.Text(prompt)])
		form.append([sg.FileBrowse(key=prompt)])
	@staticmethod
	def uploadfile_rt(prompt, ft):
		"""
		Adds a upload Button with restricted files.\n
		:param prompt (str): Text to show\n
		:param ft (list): file types\n
		:returns: prompt:'Filename'
		"""
		form.append([sg.Text(prompt)])
		form.append([sg.FileBrowse(file_types=ft)])
	@staticmethod
	def display():
		"""
		Display the form\n
		:returns: {Form data}
		"""
		form.append([sg.Button("Submit")])
		global formname
		window = sg.Window(formname, form,grab_anywhere=True,resizable=True,enable_close_attempted_event=True,use_default_focus=False)
		while True:
			event ,values = window.read(timeout=500)
			if event == "Submit":
				window.set_cursor('watch')
				window.refresh()
				time.sleep(3)
				window.set_cursor('arrow')
				window.refresh()
				window.close()
				return values
			if event == sg.WINDOW_CLOSE_ATTEMPTED_EVENT:
				ans = sg.popup_yes_no("Are sure you want to close this form, Answers will not be submittted.",title='Close?')
				if ans == "Yes":
					window.close()
					return None

def ver():
	"""
	This function returns the version
	"""
	return [["Version","1.0"],["Name","FormMaker"]]
def brief():
	"""
	Gives a breif
	"""
	return "FormMaker Version 1.0\nNew Features\n- File uploading\n- Short answers\n- Multichoice\n- Select all that apply"
def demo():
	"""
  This function makes a demo window.
  """
	create("FormMaker Demo Form")
	add.shortans("Short answer prompt")
	add.multichoice("Multiple Choice",["So","Many", "Options"])
	add.select_ata("Select all that are correct",['Upload files','Free',"Open Source"])
	add.uploadfile("Upload any file")
	add.uploadfile_rt("Or Upload Specific Files",(("Text Files", "*.txt"),))
	print(add.display())
	sg.Popup("Plus it returns your answers. Look at the console!")
