from __future__ import absolute_import
import platform
if platform.system() == 'Windows':
	from ..libloader import com
	from ..libloader.com import load_com

	def _load_com(*names):
		try:
			return load_com(*names)
		except AttributeError:
			# remove cache
			import os
			import sys
			import shutil
			for module in [m.__name__ for m in sys.modules.values()]:
				if module.startswith("win32com.gen_py."):
					del sys.modules[module]
			shutil.rmtree(os.path.join(os.environ.get('LOCALAPPDATA'), 'Temp', 'gen_py'))
			# try again
			return load_com(*names)
	com.load_com = _load_com

	from . import nvda
	from . import jaws
	from . import sapi5
#	from . import sapi4
	from . import pc_talker
	#import sapi4
	from . import clipboard
	from . import nospeech

from . import auto
