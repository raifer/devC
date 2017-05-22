# coding:utf-8

import re

import sixpad as sp

regex={
	'struct': r'^(enum|struct) [A-z0-9_\-]+[\n ]*(\{|;)',
	'function': r'^(extern )?(struct )?([-A-z0-9_]+[ *]+)([-A-z0-9_]+) *\(([-_*,\sA-z0-9]*)\)\s*(\{|;)'
	}


reg_function = re.compile(regex['function'], re.MULTILINE)


def next_function():
	page = sp.window.curPage
	pre_position  = page.position
	page.curLine += 1
	if page.find(regex['function'], scase=False, regex=True, up=False, stealthty=False):
		page.position = page.selectionStart
		sp.say(page.curLineText, True)
	else :
		page.position = pre_position
		sp.window.messageBeep(0)
# end def


def previous_function():
	page = sp.window.curPage
	pre_position  = page.position
	#page.curLine -= 1
	page.position = page.lineStartOffset(page.curLine)
	if page.find(regex['function'], scase=False, regex=True, up=True, stealthty=False):
		page.position = page.selectionStart
		sp.say(page.curLineText)
	else :
		sp.window.messageBeep(0)
# end def


def select_function():
	page = sp.window.curPage
# On recherche dans tout le document les fonction
# Voir au début du fichier l'objet reg_function qui compile la regex
	result = reg_function.finditer(page.text)
	
	# Si pas de résultat, on beep et on n'affiche rien
	if not result :
		sp.window.messageBeep(0)
		return False
	# end if

	# On créer une liste des fonctions avec deux éléments
	# 0 : Chaine qui contient le nom de la fonction et le type de retour
	# 1 : Position de la fonction dans le texte
	function_list = [["%s, type %s" %(m.group(4), m.group(3)), m.start()] for m in result]
	
	# On affiche la boite de dialogue et on récupère le résultat de l'utilisateur
	choice = box = sp.window.choice("Choisissez une fonction", "Liste des fonctions", [f[0] for f in function_list])
	
	# Si l'utilisateur a quité.
	if choice == -1:
		return False
	# end if
	
	# Si un choix a été fait, on se déplace à la fonction
	page.position = function_list[choice][1]
	
	return True
	
def next_struct():
		page = sp.window.curPage
		pre_position  = page.position
		page.curLine += 1
		if page.find(regex['struct'], scase=False, regex=True, up=False, stealthty=False):
			page.position = page.selectionStart
			sp.say(page.curLineText, True)
		else :
			page.position = pre_position
			sp.window.messageBeep(0)
	# end def
	
	
def previous_struct():
		page = sp.window.curPage
		pre_position  = page.position
		#page.curLine -= 1
		page.position = page.lineStartOffset(page.curLine)
		if page.find(regex['struct'], scase=False, regex=True, up=True, stealthty=False):
			page.position = page.selectionStart
			sp.say(page.curLineText)
		else :
			sp.window.messageBeep(0)
	# end def
	
	