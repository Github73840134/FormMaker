import PySimpleGUI as sg
from PIL import Image
from html.parser import HTMLParser
import urllib.request
import urllib.parse
import requests
import json
import time
import re
global formname
formname = ''
form = []
cmds = []
attri = []
tags = []
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
	def image(prompt,filename):
		"""
		:param prompt (str): Text to show above the image\n
		:param filename (str): Filename\n
		Supported types:\n
		- .png\n
		- .jpg\n
		"""
		form.append([sg.Text(prompt)])
		form.append([sg.Image(filename)])
	@staticmethod
	def dropdown(prompt,options):
		"""
		:param prompt (str): Text to show above the dropdown
		:param options (str): options
		"""
		form.append([sg.Text(prompt)])
		form.append([sg.Combo(options)])
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
			event ,values = window.read(timeout=0)
			if event == "Submit":
				window.set_cursor('watch')
				window.refresh()
				time.sleep(3)
				window.set_cursor('arrow')
				window.refresh()
				window.close()
				print(values)
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
	return [["Version","1.1"],["Name","FormMaker"]]
def brief():
	"""
	Gives a breif
	"""
	return "FormMaker Version 1.1\nNew Features\n- Network Forms\n"
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
class MyHTMLParser(HTMLParser):
	def handle_starttag(self, tag, attrs):
		tags.append(tag)
		for attr in attrs:
			tags.append('')
			cmds.append(attr)
	def handle_endtag(self, tag):
		tags.append('/'+tag)
	def handle_data(self, data):
		attri.append(data)
class networkform:
	@staticmethod
	def create_fromurl(url):
		'''
		Creates a form from a url via HTML\n
		param:url (str) can be https:// or http://\n
		useable elements: file,input,checkbox\n
		'''
		try:
			page = urllib.request.urlopen(url)
		except:
			return "Request Failed"
		data = page.read()
		parser = MyHTMLParser()
		parser.feed(data.decode('utf-8'))
		print(tags,cmds,attri)
		for i in range(0,len(tags)):
			if tags[i] == 'form':
				print("Form Started")
				for i in range(0,len(cmds)):
					print(cmds[i][1])
					if cmds[i] == ('type','file'):
						add.uploadfile(attri[i])
					if cmds[i][1] == ('type','input'):
						add.short_ans(attri[i])
					if cmds[i][1] == ('type','checkbox'):
						form.append([sg.Checkbox(attri[i],key=attri[i])])
		add.display()
	@staticmethod
	def fill_fromurl(url):
		'''
		Allows you to make and fill a from with a url\n
		Make sure url supports HEAD and POST methods\n
		param:url\n 
		useable elements: file and normal input\n
		header must be named file or File to use file object\n
		'''
		try:
			d = str(requests.head(url).headers)
		except:
			return "Request Failed"
		d = d.strip('{')
		d = d.strip('}')
		d = d.split(',')
		d = d[5+1:len(d)-2]
		for i in range(0,len(d)):
			d[i] = d[i][1 : : ]
			d[i] = d[i].split(':')
		for i in range(0,len(d)):
			d[i][0] = d[i][0].strip("'")
		for i in range(0,len(d)):
			d[i][1] = d[i][1].strip("'")
		for i in range(0,len(d)):
			d[i][1] = d[i][1].strip(" ")
		r = []
		for i in range(0,len(d)):
			if "File" in d[i][0]:
				add.uploadfile(d[i][0].lower())
				r.append(d[i][0].lower())
			else:
				add.shortans(d[i][0].lower())
				r.append('')
		res = add.display()
		for i in range(0,len(res)):
			print(json.loads(str(res).replace("'",'"')))
			if r[i] == 'file':
				file = open(res[r[i]],'rb')
				res[r[i]] = file.read()
				file.close()
		try:
			requests.post(url, data=res)
			return "Sent"
		except:
			return "Sending Falied"