from scraper import start_script
from json_retriever import retriever


target = input("Choose your target: ")
while target == "":
    print("Please put a name!\n")
    target = input("Choose your target: ")

posts_limit = "100" # posts scan limit
start_script(target,posts_limit)

retriever(target)

# https://community.esri.com/thread/231888-calling-a-python-script-from-another-python-script
# https://stackoverflow.com/questions/48395685/launch-a-python-script-from-another-script-with-parameters-in-subprocess-argume
# https://stackoverflow.com/questions/31483655/how-to-select-specific-json-element-in-python
# https://stackoverflow.com/questions/8114355/loop-until-a-specific-user-input
