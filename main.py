from pyscript import document, display

def getting_info(e):
    # Putting multiple document.getElementById to make the outputs work really well.
    document.getElementById('output_name').innerHTML = " "
    document.getElementById('output_grades').innerHTML = " "
    document.getElementById('output_GWA').innerHTML = " "

    name = document.getElementById('input_fullname').value #String

    eng = int(document.getElementById('input_Eng').value) #Integer
    fil = int(document.getElementById('input_Fil').value) #Integer
    math = int(document.getElementById('input_Math').value) #Integer
    sci = int(document.getElementById('input_Sci').value) #Integer
    ss = int(document.getElementById('input_SS').value) #Integer
    ve = int(document.getElementById('input_VE').value) #Integer

    sub = ['English', 'Filipino', 'Math', 'Science', 'Social Studies', 'Values Education'] #List
    units = (5, 3, 5, 5, 3, 1) #Tuples

    #Formula and solution for GWA.
    sub1 = eng * 5
    sub2 = fil * 3
    sub3 = math * 5
    sub4 = sci * 5
    sub5 = ss * 3
    sub6 = ve * 1

    add_sub = sub1 + sub2 + sub3 + sub4 + sub5 + sub6
    add_units = sum(units)

    gwa = round(add_sub / add_units, 2)
    

    display(f'Name: {name}', target='output_name')
    display(f'{sub[0]} = {eng}', target='output_grades')
    display(f'{sub[1]} = {fil}', target='output_grades')
    display(f'{sub[2]} = {math}', target='output_grades')
    display(f'{sub[3]} = {sci}', target='output_grades')
    display(f'{sub[4]} = {ss}', target='output_grades')
    display(f'{sub[5]} = {ve}', target='output_grades')
    display(f'Your general weighted average is {gwa}', target='output_GWA')

#References: Codes from w3schools.com
