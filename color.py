from colorama import init, Fore, Style
init()

def yellow(text):
	return Fore.YELLOW + text + Style.RESET_ALL

def green(text):
	return Fore.GREEN + text + Style.RESET_ALL

def red(text):
	return Fore.RED + text + Style.RESET_ALL
