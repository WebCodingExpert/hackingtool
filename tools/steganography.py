Skip to content
Search or jump to…
Pull requests
Issues
Marketplace
Explore
 
@SamirJanaOfficial 
SamirJanaOfficial
/
hackingtool
Public
Code
Issues
Pull requests
Actions
Projects
Wiki
Security
Insights
Settings
hackingtool
/
tools
/
steganography.py
in
main
 

Spaces

4

No wrap
1
# coding=utf-8
2
import subprocess
3
​
4
from core import HackingTool
5
from core import HackingToolsCollection
6
from core import validate_input
7
​
8
​
9
class SteganoHide(HackingTool):
10
    TITLE = "SteganoHide"
11
    INSTALL_COMMANDS = ["sudo apt-get install steghide -y"]
12
​
13
    def run(self):
14
        choice_run = input(
15
            "[1] Hide\n"
16
            "[2] Extract\n"
17
            "[99]Cancel\n"
18
            ">> ")
19
        choice_run = validate_input(choice_run, [1, 2, 99])
20
        if choice_run is None:
21
            print("Please choose a valid input")
22
            return self.run()
23
​
24
        if choice_run == 99:
25
            return
26
​
27
        if choice_run == 1:
28
            file_hide = input("Enter Filename you want to Embed (1.txt) >> ")
29
            file_to_be_hide = input("Enter Cover Filename(test.jpeg) >> ")
30
            subprocess.run(
31
                ["steghide", "embed", "-cf", file_to_be_hide, "-ef", file_hide])
32
​
33
        elif choice_run == "2":
34
            from_file = input("Enter Filename From Extract Data >> ")
35
            subprocess.run(["steghide", "extract", "-sf", from_file])
36
​
37
​
38
class StegnoCracker(HackingTool):
39
    TITLE = "StegnoCracker"
40
    DESCRIPTION = "SteganoCracker is a tool that uncover hidden data inside " \
41
                  "files\n using brute-force utility"
42
    INSTALL_COMMANDS = [
43
        "pip3 install stegcracker && pip3 install stegcracker -U --force-reinstall"]
44
​
45
    def run(self):
@SamirJanaOfficial
Commit changes
Commit summary
Create steganography.py
Optional extended description
Add an optional extended description…
 Commit directly to the main branch.
 Create a new branch for this commit and start a pull request. Learn more about pull requests.
 
Footer
© 2022 GitHub, Inc.
Footer navigation
Terms
Privacy
Security
Status
Docs
Contact GitHub
Pricing
API
Training
Blog
About
