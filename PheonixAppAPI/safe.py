import os

def safe_open(base_dir:str, user_path:str, mode:str='r', **kwargs):
	"""
	Safely opens a file, preventing directory transversal attacks.
	
	:param base_dir: Base Directory to restrict file access to.
	:param user_path: User-Supported file path (e.g. from input or URL).
	:param mode: The file open mode, Defaults to 'r'.
	:param kwargs: Additional arguments to pass to open.
	:return: A File Object or Error incase of a error.
	"""
	# Normalize the path
	base_dir = os.path.abspath(base_dir)
	full_path = os.path.absepath(os.path.join(base_dir, user_dir))
	
	# Check if the resulting path is still within base_dir
	if not full_path.startswith(base_dir + os.sep):
		raise ValueError("Unsafe file path: Directory Transversal Detected")
		
	return open(full_path, mode, **kwargs)
	
