
from __future__ import annotations
import adsk.core, adsk.fusion, adsk.cam, traceback, os, getpass

app : adsk.core.Application = adsk.core.Application.get()
ui  = app.userInterface
def run(context):
	try:
		useFileDialog = True
		dialogResult = ui.messageBox('Yes = Create a full report (list and control details)\nNo = minimal report (control list only)?', 'UI Report Type', adsk.core.MessageBoxButtonTypes.YesNoCancelButtonType, adsk.core.MessageBoxIconTypes.QuestionIconType) 
		if dialogResult == adsk.core.DialogResults.DialogYes: fullReport = True
		elif dialogResult == adsk.core.DialogResults.DialogNo: fullReport = False
		else: return

		if useFileDialog:
			fileDialog : adsk.core.FileDialog = ui.createFileDialog()
			fileDialog.isMultiSelectEnabled = False
			fileDialog.initialDirectory = os.path.dirname(os.path.realpath(__file__))
			fileDialog.initialFilename = "UiObjects.py"
			fileDialog.title = "Specify result filename"
			fileDialog.filter = 'Python files (*.py)'
			fileDialog.filterIndex = 0

			dialogResult = fileDialog.showSave()
			if dialogResult != adsk.core.DialogResults.DialogOK: return
			filename = fileDialog.filename
		else: filename = GetPath(os.path.dirname(os.path.realpath(__file__)), "UiObjects.py")

		with open(filename, 'w', encoding='utf-8') as f: f.write(createDefFile(fullReport))
		ui.messageBox(f'File sucsessfuly written to local directory: \n"{filename}"')
	except: ui.messageBox(f'Failed:\n{traceback.format_exc()}')
			


def Indent(level, additional = 0, indentChar = '\t'):return (indentChar*(level+additional))

class Ignore:
	def __enter__(self):return self
	def __exit__(self,ExType,ExVal,ExTrace): return True


def stringifyName(name:str):
	if len(name) == 36 and len(name.split('-')) == 5: return 'uuid_' + name.replace('-', '_')
	return name.replace(" ", "").replace("::", "").replace("-", "").replace(".", "_").replace("3D", "")

def varString(indent, varName, varVal, strinifyValue = True):
	varVal = f'"{varVal}"' if strinifyValue and isinstance(varVal, (str, bytearray)) else str(varVal)
	return f'{Indent(indent)}{stringifyName(varName)} = {r"{}".format(varVal)}\n'

def classString(indent, name, cleanName = True, **kwargs):
	className = f'{Indent(indent)}class {(name if not cleanName else stringifyName(name))}:\n'
	vars = ''.join(varString(indent+1, k, v) for k,v in kwargs.items())
	return className + vars


def GetPath(fileDir, fileName):
	if not os.path.exists(fileDir): os.makedirs(fileDir)
	return os.path.join(fileDir, fileName)

def GetResource(cmdDef:adsk.core.CommandDefinition):
	try: return cmdDef.resourceFolder.replace(getpass.getuser(), '<user>')
	except: return 'No Icon Provided'


def ClassRefString(parentClassName:str,subclassId:str, isClass=False):
	refString = f'{parentClassName}.{stringifyName(subclassId)}'
	if isClass: refString = f'{stringifyName(subclassId)} ({refString})'
	return refString

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

ListControlMap = {	adsk.core.ListControlDisplayTypes.CheckBoxListType:'CheckBoxListControlDefinition',
				adsk.core.ListControlDisplayTypes.RadioButtonlistType:'RadioButtonListControlDefinition',
				adsk.core.ListControlDisplayTypes.StandardListType: 'StandardListControlDefinition'}
DefinitionMap = {adsk.core.ButtonControlDefinition.classType():'ButtonControlDefinition',
				adsk.core.CheckBoxControlDefinition.classType():'CheckBoxControlDefinition'}

def getCommandDef(commandDef : adsk.core.CommandDefinition, indent):
	if not commandDef: return ''
	returnResult = classString(indent,commandDef.id,ID = commandDef.id, isNative = commandDef.isNative, icon = GetResource(commandDef))
	with Ignore():
		controlDef = commandDef.controlDefinition
		if isinstance(controlDef, adsk.core.ListControlDefinition):
			controlType = ListControlMap.get(controlDef.listControlDisplayType, 'NoneListControl')
		else: controlType = DefinitionMap.get(controlDef.classType(), 'Unexpected_Control_Type')
		returnResult += classString(indent+1, f'{commandDef.id}_control', isVisible = controlDef.isVisible, 
									isEnabled = controlDef.isEnabled, DefinitionType = controlType)
	return returnResult

def createDefControls(controls:'list[adsk.core.ToolbarControl]', indent, result = '', fullReport=False):
	for control in controls:
		if isinstance(control, adsk.core.SeparatorControl):
			result += classString(indent,control.id, ID = control.id, Index = control.index)
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		elif isinstance(control, adsk.core.DropDownControl):
			result += classString((indent),control.id,ID = control.id, Index = control.index)
			result += createDefControls(control.controls, indent+1, '', fullReport)
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		elif isinstance(control, adsk.core.SplitButtonControl):
			try:defaultCommand = control.defaultCommandDefinition.id
			except: defaultCommand = 'Unknown'
			result += classString((indent),control.id,ID = control.id, Index = control.index, 
								isLastUsedShown = control.isLastUsedShown, defaultCommand = defaultCommand)
			with Ignore():
				if fullReport and len(control.additionalDefinitions) > 0:
					result += classString(indent+1,'AdditionalControls')
					additionalCtrls = TryGet(control.additionalDefinitions)
					TempResult = [varString(indent+2, stringifyName(cmdDef.id), ClassRefString('AllPanels', cmdDef.id), False) for cmdDef in additionalCtrls]
					if len(TempResult) == 0 : result += f'{Indent(indent+2)}pass\n'
					else: result += ''.join(TempResult)
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		elif isinstance(control, adsk.core.CommandControl):
			result += classString(indent,control.id, ID = control.id, Index = control.index)
			with Ignore():
				result += varString(indent+1, 'isPromoted', control.isPromoted)
				result += varString(indent+1, 'isPromotedByDefault', control.isPromotedByDefault)
			if fullReport:
				with Ignore(): result += varString(indent+1, 'commandDefinition', ClassRefString('AllControls', control.commandDefinition.id), False)
	return result


def CheckProduct(obj:adsk.core.Workspace):
	try: return obj.toolbarPanels and (obj.productType != '')
	except: return False #Tying to get its panels can throw an error


def TryGet(collection):
	for I in range(len(collection)):
		try: 
			colItem = collection.item(I)
			if not isinstance(colItem, (adsk.core.Workspace,adsk.core.ToolbarTab)) or CheckProduct(colItem):
				yield colItem
		except:pass


def createDefFile(fullReport):
	# Collect ui information.

	uiToolbars = list(TryGet(ui.toolbars))
	uiWorkspaces = list(TryGet(ui.workspaces))
	uiTabs = list(TryGet(ui.allToolbarTabs))
	uiPanels = list(TryGet(ui.allToolbarPanels))
	commandDefs = list(TryGet(ui.commandDefinitions))
		
	if fullReport:
		def checkAppend(setList:list,iterable:list): setList.extend([item for item in iterable if item not in setList])

		for workspace in uiWorkspaces:
			workspaceTabs,workspacePanels = TryGet(workspace.toolbarTabs),TryGet(workspace.toolbarPanels)
			checkAppend(uiTabs,workspaceTabs);checkAppend(uiPanels,workspacePanels)
			for tab in workspaceTabs:
				tabPanels = TryGet(tab.toolbarPanels)
				checkAppend(uiPanels,tabPanels)
				for panel in tabPanels:
					panelControls = [control.commandDefinition for control in TryGet(panel.controls) if isinstance(control,adsk.core.CommandControl)]
					checkAppend(commandDefs,panelControls)
		
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	result='\n'.join((
	"import adsk.core, adsk.fusion, adsk.cam",
	"__all__ = ['Toolbars', 'WorkSpaces', 'AllPanels', 'AllTabs']",
	"",""))

	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# Collect All Control information.
	if fullReport:
		result += classString(0, 'AllControls')
		for definition in commandDefs: result += getCommandDef(definition, 1)

	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# Collect All panel information.
	result += classString(0, 'AllPanels')
	for panel in uiPanels: 
		result += classString(1, panel.id, ID = panel.id)
		result += createDefControls(panel.controls, 2, '',fullReport)
	
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# Collect All tab information.
	result += classString(0, 'AllTabs')
	for tab in uiTabs: 
		result += classString((1), tab.id, ID = tab.id)
		for panel in TryGet(tab.toolbarPanels):
			result += classString((2), ClassRefString("AllPanels", panel.id, True), False, Index = panel.index)	
	
	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# Collect All toolbar information.
	if fullReport:
		result += classString(0, 'Toolbars')
		for toolbar in uiToolbars: 
			result += classString(1, toolbar.id, ID = toolbar.id)
			result += createDefControls(toolbar.controls, 2, '',fullReport)

	#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	# Collect All Workspace information.
	result += classString(0, 'WorkSpaces')
	for workspace in uiWorkspaces:
		result += classString(1, workspace.id, ID = workspace.id)
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		result += classString(2, 'Tabs')
		if len(workspace.toolbarTabs) > 0 :
			for tab in TryGet(workspace.toolbarTabs):  result += classString(3, ClassRefString("AllTabs", tab.id, True),False, Index = tab.index)
		else: result += f'{Indent(3)}pass\n'
		#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		result += classString(2, 'Panels')
		for panel in TryGet(workspace.toolbarPanels): result += varString(3, stringifyName(panel.id), ClassRefString('AllPanels', panel.id), False)
	return result
