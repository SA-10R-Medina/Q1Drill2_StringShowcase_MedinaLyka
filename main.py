from pyscript import when, display, document

@when("click", "#submit-btn")
def show_message(event):
    name = document.querySelector("#name").value
    age = document.querySelector("#age").value
    school = document.querySelector("#school").value

    message = (
        "STUDENT PROFILE\n"
        "Name   : " + name + "\n"
        "Age    : " + age + "\n"
        "School : " + school + "\n\n"
        + name + " is " + age + " years old and studies at " + school + "."
    )

    display(message, target="output")
