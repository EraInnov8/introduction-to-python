# Common operations - 'w', 'a', 'r'

# with open('./welcome.txt', 'a') as f:
#     message='This is an appended message.'
#     f.write(message)
#     f.close()


with open('./5_file_handling/lorem_ipsum.txt', 'r') as file:
    content = file.read()
    print(content)
    file.close()


# import os
# print(os.getcwd())
# os.mkdir('temp')


# Play with it - https://www.digitalocean.com/community/tutorials/python-os-module

# with keyword - the with statement replaces a try-catch block with a concise shorthand
# Know more about with keyword - https://stackoverflow.com/questions/3012488/what-is-the-python-with-statement-designed-for

# In depth Read write in python - https://www.youtube.com/watch?v=eCvT4zreu4g
