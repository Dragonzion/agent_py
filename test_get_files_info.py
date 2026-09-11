from functions.get_files_info import get_files_info

print(
"Result for current directory:" + "\n  " + get_files_info("calculator", ".").replace("\n", "\n  "),
"Result for 'pkg' directory:" +  "\n  " + get_files_info("calculator", "pkg").replace("\n", "\n  "),
"Result for '/bin' directory:" +  "\n  " + get_files_info("calculator", "/bin").replace("\n", "\n  "),
"Result for '../' directory:" +  "\n  " + get_files_info("calculator", "../").replace("\n", "\n  "),
sep="\n"
)
