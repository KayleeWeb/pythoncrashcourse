# go through todo's 

# txt exists
# read from todo.txt as list

# for loop through list 
    # print the todo
    # ask user if they completed this
        # remove
    # else
        # keep

# while loop
    # ask for another todo
    # if they input "q" 
        #quit out with "break"
    # else
        # add to todo list 

# write new todo fil

try:
    with open("todos.txt", "r") as f:
        content = f.read()
        todo_list = content.split("\n")
except FileNotFoundError:
    with open("todos.txt", "w") as f:
        f.write("")

remaining_todo_list = []

for todo in todo_list:
    print(todo)
    user_input = input("Completed? (y/n)")
    if user_input != "y":
        remaining_todo_list.append(todo)

while True:
    new_todo = input("add todo (q to quit): ")
    if new_todo == "q":
            break
    else:
         remaining_todo_list.append(new_todo)

with open("todos.txt","w") as f:
     output = "\n".join(remaining_todo_list)
     f.write(output)

