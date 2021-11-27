import adsk.core, adsk.fusion, adsk.cam, traceback, os
ui_ = None
def run(context):
	global ui_
	try:
		app:adsk.core.Application = adsk.core.Application.get()
		ui_= ui  = app.userInterface
		useFileDialog = True
		dialogResult = ui.messageBox('Yes = Create a full report (list and control details)\nNo = minimal report (control list only)?', 'UI Report Type', adsk.core.MessageBoxButtonTypes.YesNoCancelButtonType, adsk.core.MessageBoxIconTypes.QuestionIconType) 
		if dialogResult == adsk.core.DialogResults.DialogYes: fullReport = True
		elif dialogResult == adsk.core.DialogResults.DialogNo: fullReport = False
		else: return

		if useFileDialog:
			fileDialog : adsk.core.FileDialog = ui.createFileDialog()
			fileDialog.isMultiSelectEnabled = False
			fileDialog.title = "Specify result filename"
			fileDialog.filter = 'Python files (*.py)'
			fileDialog.filterIndex = 0
			dialogResult = fileDialog.showSave()
			if dialogResult == adsk.core.DialogResults.DialogOK: filename = fileDialog.filename
			else: return
		else:  
			filename = GetPath(os.path.dirname(os.path.realpath(__file__)), "UiObjects.py")

		result = createDefFile(fullReport)
		with open(filename, 'w', encoding='utf-8') as f: f.write(result)
		ui.messageBox('File sucsessfuly written to local directory: \n"' + filename + '"')
	except:
		if ui: ui.messageBox('Failed:\n{}'.format(traceback.format_exc()))
			


def Indent(level, additional = 0, indentChar = '\t'):return ((level+additional)*indentChar)

def stringifyName(name:str):
	if len(name) == 36 and len(name.split('-')) == 5: return 'uuid_' + name.replace('-', '_')
	name = name.replace(" ", "").replace("::", "").replace(".", "_").replace("-", "")
	if name[:2] == '3D': name = name[2:]
	return name

def varString(indent, varName, varVal, strinifyValue = True):
	name = stringifyName(varName)
	varVal = '"'+varVal+'"' if strinifyValue and isinstance(varVal, (str, bytearray)) else str(varVal)
	varVal = r"{}".format(varVal)
	return Indent(indent) + name + ' = ' + varVal + '\n'

def classString(indent, name, cleanName = True, **kwargs):
	className = Indent(indent) + 'class ' + (name if not cleanName else stringifyName(name)) + ':\n'
	vars = ''.join(varString(indent+1, k, v) for k,v in kwargs.items())
	return className + vars

def CheckProduct(obj):
	try: 
		prodType = obj.productType
		obj.toolbarPanels
	except: return False
	return (prodType != '')


def GetPath(fileDir, fileName):
	if not os.path.exists(fileDir): os.makedirs(fileDir)
	return os.path.join(fileDir, fileName)
def DumpData(data, fileDir, fileName='data.py'): 
		if not os.path.exists(fileDir): os.makedirs(fileDir)
		filePath = os.path.join(fileDir, fileName)
		with open(filePath, 'w', encoding='utf-8') as f: f.write(data)






def getCommandDef(commandDef : adsk.core.CommandDefinition, indent):
	if commandDef:      
		returnResult = classString(indent,commandDef.id,ID = commandDef.id, isNative = commandDef.isNative)
		try:
			controlDef = commandDef.controlDefinition
			if controlDef.objectType == adsk.core.ButtonControlDefinition.classType():
				controlType = 'ButtonControlDefinition'
			elif controlDef.objectType == adsk.core.CheckBoxControlDefinition.classType():
				controlType = 'CheckBoxControlDefinition'
			elif controlDef.objectType == adsk.core.ListControlDefinition.classType():
				if controlDef.listControlDisplayType == adsk.core.ListControlDisplayTypes.CheckBoxListType:
					controlType = 'CheckBoxListControlDefinition'
				elif controlDef.listControlDisplayType == adsk.core.ListControlDisplayTypes.RadioButtonlistType:
					controlType = 'RadioButtonListControlDefinition'
				elif controlDef.listControlDisplayType == adsk.core.ListControlDisplayTypes.StandardListType:
					controlType = 'StandardListControlDefinition'
			else: controlType = '___Unexpected_Control_Type'
			returnResult += classString(indent+1,str(commandDef.id) + '_control', isVisible = controlDef.isVisible, isEnabled = controlDef.isEnabled, DefinitionType = controlType)
		except: pass
		return returnResult

def createDefControls(controls, indent, result = '', fullReport=False):
	for control in controls:
		if control.objectType == adsk.core.SeparatorControl.classType():
			result += classString(indent,control.id,ID = control.id, Index = control.index)
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		elif control.objectType == adsk.core.CommandControl.classType():
			result += classString(indent,control.id,ID = control.id, Index = control.index)
			try:
				result += varString(indent+1, 'isPromoted', control.isPromoted)
				result += varString(indent+1, 'isPromotedByDefault', control.isPromotedByDefault)
			except: pass # Failed to get isPromoted so do nothing.
			if fullReport:
				try: commandDef : adsk.core.CommandDefinition = control.commandDefinition        
				except: commandDef = False
				if commandDef != False: result += varString(indent+1, 'commandDefinition', 'AllControls.' + stringifyName(commandDef.id), False)
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		elif control.objectType == adsk.core.DropDownControl.classType():
			result += classString((indent),control.id,ID = control.id, Index = control.index)
			result += createDefControls(control.controls, indent+1, '', fullReport)
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		elif control.objectType == adsk.core.SplitButtonControl.classType():
			try:defaultCommand = control.defaultCommandDefinition.id
			except: defaultCommand = 'Unknown'
			result += classString((indent),control.id,ID = control.id, Index = control.index, 
				isLastUsedShown = control.isLastUsedShown, defaultCommand = defaultCommand)
			try:
				classString(indent+1,'AdditionalControls')
				for cmdDef in control.additionalDefinitions: result += varString( indent+2,'ID', cmdDef.id)
			except:	pass
	return result



def createDefFile(fullReport):
	app : adsk.core.Application = adsk.core.Application.get()
	ui  = app.userInterface
	# Collect workspace information.
	result = 'import adsk.core, adsk.fusion, adsk.cam\n'
	result += "__all__ = ['Toolbars', 'WorkSpaces', 'AllPanels', 'AllTabs']\n\n"
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# Collect All Control information.
	if fullReport:
		result += 'class AllControls:\n'
		for definition in ui.commandDefinitions:
			result += getCommandDef(definition, 1)
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# Collect All panel information.
	result += 'class AllPanels:\n'
	for panel in ui.allToolbarPanels: 
		result += classString(1, panel.id, ID = panel.id)
		result += createDefControls(panel.controls, 2, '',fullReport)
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# Collect All tab information.
	result += 'class AllTabs:\n'
	for tab in ui.allToolbarTabs: 
		if not CheckProduct(tab): continue
		result += classString((1), tab.id, ID = tab.id)
		for panelI in range(len(tab.toolbarPanels)):
			try:
				panel = tab.toolbarPanels.item(panelI)
				result += classString((2), stringifyName(panel.id) + '(AllPanels.' + stringifyName(panel.id) + ')',False, Index = panel.index)
			except:pass
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# Collect All toolbar information.
	result += 'class Toolbars:\n'
	for toolbar in ui.toolbars: result += classString((1), toolbar.id, ID = toolbar.id)
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# Collect All Workspace information.
	result += 'class WorkSpaces:\n'
	for workspace in ui.workspaces:
		if not CheckProduct(workspace) or not workspace.isNative: continue
		result += classString((1), workspace.id, ID = workspace.id)
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		result += Indent(2) + 'class Tabs:\n'
		if len(workspace.toolbarTabs) > 0 :
			for tab in workspace.toolbarTabs: result += classString(3, stringifyName(tab.id) + '(AllTabs.' + stringifyName(tab.id) + ')',False, Index = tab.index)
		else: result += Indent(3) + 'pass\n'
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		panelsResult = Indent(2) + 'class Panels:\n'
		panelsResult += ''.join([varString(3, stringifyName(panel.id), 'AllPanels.' + stringifyName(panel.id), False) for panel in workspace.toolbarPanels])
		result += panelsResult
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	return result









