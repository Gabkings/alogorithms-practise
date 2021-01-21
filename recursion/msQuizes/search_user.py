def search_user(arr, email):
    email = email.split("@")[0]
    new_name = "".join(email)
    if "." in new_name:
        new_name = new_name.split(".")
    
    if "_" in new_name:
        new_name = new_name.split("_")
    fname = new_name[0]
    lname = new_name[1]
    fname = fname.capitalize()
    lname = lname.capitalize()
    fullname = fname +" "+ lname

    for i in range(len(arr)):
        if arr[i] == fullname:
            return arr[i]
    return "Not Found"

arr = ["Gabriel Gitonga", "James Gitau", "Gab Works"]
email = "gab_works@gmail.com"

s = search_user(arr, email)
print(s)
