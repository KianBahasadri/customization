import os
php_extensions = [
    '.php', '.php2', '.php3', '.php4', '.php5', '.php6', '.php7', '.phps', '.phps',
    '.pht', '.phtm', '.phtml', '.pgif', '.shtml', '.htaccess', '.phar', '.inc', '.hphp',
    '.ctp', '.module'
]

filename = input("What is the original filename called?\n")
for extension in php_extensions:
    new_name = filename.split(".")[0] + extension
    os.system(f"cp {filename} {new_name}")
