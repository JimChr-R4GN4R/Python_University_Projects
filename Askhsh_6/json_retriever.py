import json


def retriever(target):
  try:
    json_str = open('{0}/{0}.json'.format(target)).read()
  except FileNotFoundError:
    print("The target has private profile or not found!")
    exit()

  contact = json.loads(json_str)



  commnets_authors_total = []   


  x = 0
  for graph_image in contact['GraphImages']:
    y = 0

    try:

      comment = contact["GraphImages"][x]["comments"]["data"][y]["text"] #Check if post x has comments

      for comments_total in contact["GraphImages"][x]["comments"]["data"]:
        comment = contact["GraphImages"][x]["comments"]["data"][y]["text"]
        comment_author = contact["GraphImages"][x]["comments"]["data"][y]["owner"]["username"]
        #print(comment_author," : ",comment)
        commnets_authors_total.append(comment_author)
        y = y + 1

    except IndexError:

      #print("Not commnet in", x, 'Post')
      pass


    x = x + 1


  b = {}
  for item in commnets_authors_total:
      b[item] = b.get(item, 0) + 1

  sorted_list = sorted(b.items(), key=lambda kv: kv[1])
  sorted_list.reverse()

  try:
    most_comments_author = sorted_list[0]
  except IndexError:
    print("There are no commenters :(")
    exit()

  print("Most Commenter(s) with", most_comments_author[1],"comments: ")
  for i in sorted_list:
    if most_comments_author[1] == i[1]:
      print(i[0])








#########################################
# https://opentechguides.com/how-to/article/python/183/json-read-write.html
# https://stackoverflow.com/questions/31483655/how-to-select-specific-json-element-in-python
# https://stackoverflow.com/questions/8369219/how-to-read-a-text-file-into-a-string-variable-and-strip-newlines
# https://stackoverflow.com/questions/27315472/how-to-count-items-in-json-data
# https://wiki.python.org/moin/ForLoop



# https://stackoverflow.com/questions/2600191/how-can-i-count-the-occurrences-of-a-list-item
# https://www.datasciencelearner.com/how-to-create-a-list-in-python-append/
# https://blog.softhints.com/python-count-items-list/
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
# https://stackoverflow.com/questions/59736308/python-check-json-file-with-variables
# https://stackoverflow.com/questions/59738905/python-count-lists-values-and-put-them-in-ordered-list-without-library
# https://stackoverflow.com/questions/2161752/how-to-count-the-frequency-of-the-elements-in-a-list
# https://www.tutorialspoint.com/python/list_reverse.htm
# https://stackoverflow.com/questions/59742922/python-cd-in-a-folder-without-library?noredirect=1#comment105634285_59742922
# https://stackoverflow.com/questions/19522990/python-catch-exception-and-continue-try-block
# https://stackoverflow.com/questions/59742922/python-cd-in-a-folder-without-library


