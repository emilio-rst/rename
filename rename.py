#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  rename.py
#  
#  Renombra un archivo conservando la extension utilizando la cadena
#  de texto que se encuentra en el portapapeles
#
#  Copyright 2012 emilio silveira <emilio.rst@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

import os
import sys
import subprocess

class FileRename:
	""" Clase para renombrar archivo """
	
	def __init__(self, filename):
		""" Constructor """
		
		self.filename = filename
	
	def get_clipboard(self):
		""" Obtiene el contenido del portapapeles """
		
		clipboard = subprocess.check_output('xsel', shell = True)
		return clipboard
	
	def rename_from_clipboard(self):
		""" Renombrar archivo desde el nombre indicado en el portapapeles preservando la extensión """
		
		# Se obtiene y se filtra el contenido del portapapeles
		clipboard = self.get_clipboard().replace("/", " ").strip()
		
		if clipboard == "": 
			raise Exception("El portapapeles no posee una cadena de texto valida")
		
		# Genera el nombre de archivo
		new_filename = os.path.join(os.path.dirname(self.filename), clipboard)
		extension = os.path.splitext(self.filename)[1]
		
		if extension != "":
			new_filename += extension
		
		os.rename(self.filename, new_filename)


if __name__ == '__main__':
	FileRename(sys.argv[1]).rename_from_clipboard()

