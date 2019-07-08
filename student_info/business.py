from .models import StudentInfo

from django.http import HttpResponse

def datastore(request):
    print("Data stored")
    first_name = request.POST["first_name"]
    last_name = request.POST["last_name"]
    contact = request.POST["contact"]
    email = request.POST["mail"]
    password = request.POST["password"]
    re_password = request.POST["re_password"]

    student_input = StudentInfo(username = email, First_Name = first_name, Last_Name = last_name,
                          Contact = contact,  password = password,
                          Re_Password = re_password)
    student_input.save()
    return()

