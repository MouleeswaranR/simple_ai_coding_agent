from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def main():
    working_dir= "calculator"

    #get_files_info tests

    # root_contents=get_files_info(working_dir)
    # print(root_contents)
    # pkg_contents=get_files_info(working_dir,"pkg")
    # print(pkg_contents)
    # non_contents=get_files_info(working_dir,"/bin")
    # print(non_contents)

    #get_file_content test

    # print(get_file_content(working_dir,"lorem.txt"))
    # print(get_file_content(working_dir,"main.py"))
    # print(get_file_content(working_dir,"pkg/calculator.py"))


    #write_file tests

    # print(write_file(working_dir,"lorem.txt","wait, this isn't lorem ipsum"))
    # print(write_file(working_dir,"pkg/morelorem.txt","wait, this isn't lorem ipsum"))

    print(run_python_file(working_dir,"main.py",["3 + 5"]))


main()