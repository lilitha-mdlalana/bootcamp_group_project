#6982507979@bootcamp.wethinkcode.co.za

import os
'''
    This is the team allocator project solution example project
'''


def student_list():
    return ['zakithikhDBN2022 - 4 April - Johannesburg Physical - seat 3', 'ddhaalJHB2022 - 2 May - Cape Town Virtual',
            'thandohDBN2022 - 4 April - Phokeng Physical - seat 3', 'zaneleJHB2022 - 2 May - Durban Virtual',
            'ntobekoDBN2022 - 4 April - Phokeng Physical - seat 2', 'BusiJHB2022 - 2 May - Durban Virtual',
            'zinhlehDBN2022 - 4 April - Phokeng Physical - seat 1', 'CebiJHB2022 - 2 May - Durban Virtual',
            'lukhona - 4 April - Phokeng Virtual', 'ddhaalJHB2022 - 2 May - Durban Physical - seat 4',
            'gabiDBN2022 - 4 April - Phokeng Virtual', 'ngakithilJHB2022 - 2 May - Durban Physical - seat 5',
            'zimthembilehDBN2022 - 4 April - Phokeng Virtual', 'ngakuyelJHB2022 - 2 May - Durban Physical - seat 2',
            'zimlindilehDBN2022 - 4 April - Phokeng Virtual', 'yenzileJHB2022 - 2 May - Durban Physical - seat 3',
            'zimthandilehDBN2022 - 4 April - Johannesburg Virtual', 'kuhlengaweDBN2022 - 4 April - Durban Physical - seat 1',
            'zimkhonzileDBN2022 - 4 April - Johannesburg Virtual', 'hlelokuhlehDBN2022 - 4 April - Durban Physical - seat 3',
            'zizonkehDBN2022 - 4 April - Johannesburg Virtual', 'sibusisohDBN2022 - 4 April - Durban Physical - seat 2',
            'kholekileDBN2022 - 4 April - Johannesburg Virtual', 'vusiDBN2022 - 4 April - Durban Physical - seat 9',
            'kholelwahDBN2022 - 4 April - Johannesburg Virtual', 'zuzumuzihDBN2022 - 4 April - Durban Physical - seat 10',
            'thembelahDBN2022 - 4 April - Johannesburg Virtual', 'babazileDBN2022 - 4 April - Durban Physical - seat 11',
            'thembisileDBN2022 - 4 April - Johannesburg Virtual', 'owenkosiDBN2022 - 4 April - Durban Physical - seat 8',
            'thembisiweDBN2022 - 4 April - Johannesburg Physical - seat 5', 'nobuhleJHB2022 - 2 May - Cape Town Physical',
            'thenjisiweDBN2022 - 4 April - Johannesburg Physical - seat 6', 'nonkonzoJHB2022 - 2 May - Cape Town Physical',
            'thethelelileDBN2022 - 4 April - Johannesburg Physical - seat 7', 'nombusoJHB2022 - 2 May - Cape Town Virtual',
            'thembiDBN2022 - 4 April - Johannesburg Physical - seat 4', 'nozizweJHB2022 - 2 May - Cape Town Virtual']

#Custom functions
def getStudentsByLocation(student_list,location):
    students = []
    for student in student_list:
        if location in student:
            students.append(student)
    return students

def getPhysicalTeams(physical_students):
    student_teams = []
    temp_teams = []
    index = 0
    for student in physical_students:
        index += 1;
        temp_teams.append(student)
        if index == 4:
            student_teams.append(list(temp_teams))
            temp_teams.clear()
            index = 0
    return student_teams        


def dbn_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Durban campus only.
    '''
    dbn_campus_students = getStudentsByLocation(student_list,'Durban')
    return dbn_campus_students
print(dbn_campus_students(student_list()))

def cpt_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Cape Town campus only.
    '''
    cpt_students = getStudentsByLocation(student_list,'Cape Town')
    return cpt_students

def jhb_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the Johannesburg campus only.
    '''
    jhb_students = getStudentsByLocation(student_list,'Johannesburg')
    return jhb_students

def nw_campus_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students in the North West campus only.
    '''
    nw_students = getStudentsByLocation(student_list,'Phokeng')
    return nw_students

def dbn_physical_students(dbn_students):
    '''
    from the list of dbn_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    dbn_physical_students = getStudentsByLocation(dbn_students,'Durban Physical')
    return dbn_physical_students

def dbn_physical_teams(dbn_physical_students):
    '''
    from the list of dbn_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    dbn_physical_teams = getPhysicalTeams(dbn_physical_students)
    return dbn_physical_teams

def dbn_teams_file(durban_physical_teams):
    '''
    write and save the information in the dbn_physical_teams into a textfile
    '''
    if not os.path.exists('team_allocator_teams/'):
        os.mkdir('team_allocator_teams')
    fpath = open('team_allocator_teams/dbn_teams_file.txt','w+')
    for team in durban_physical_teams:
        # fpath.writelines(team)  
        # fpath.write('\n')
         fpath.write(' '.join(map(str,team)) + '\n')
    fpath.close()   
     

def cpt_physical_students(cpt_physical_students):
    '''
    from the list of cpt_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    cpt_campus_physical_students = getStudentsByLocation(cpt_physical_students,'Cape Town Physical')
    return cpt_campus_physical_students


def cpt_physical_teams(cpt_physical_students):
    '''
    from the list of cpt_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    cpt_physical_teams = []
    team = [] 
    index = 0
    for student in cpt_physical_students:
        index += 1
        team.append(student)
        if(index == 4):
            dbn_physical_teams.append(list(team))
            team.clear()
            index = 0
    return cpt_physical_teams

def cpt_teams_file(capetown_final_teams):
    '''
    write and save the information in the cpt_physical_teams into a textfile
    '''
    if not os.path.exists('team_allocator_teams/'):
        os.mkdir('team_allocator_teams')
    fpath = open('team_allocator_teams/cpt_final_teams_file.txt','w+')
    for team in capetown_final_teams:
         fpath.write(' '.join(map(str,team)) + '\n')
    fpath.close() 


def jhb_physical_students(jhb_physical_students):
    '''
    from the list of jhb_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    johannesburg_physical_students = []
    for student in jhb_physical_students:
        if 'Johannesburg Physical' in student:
            johannesburg_physical_students.append(student)
    return johannesburg_physical_students

def jhb_physical_teams(jhb_physical_students):
    '''
    from the list of jhb_physical_students create list of 4 students per team, and add them to 
    one big list
    '''
    johannesburg_physical_teams = []
    team = []
    index = 0
    for student in jhb_physical_students:
        index += 1
        team.append(student)
        if(index == 4):
            johannesburg_physical_teams.append(list(team))
            team.clear()
            index = 0

    return johannesburg_physical_teams


def jhb_teams_file(jhb_final_teams):
    '''
    write and save the information in the jhb_physical_teams into a textfile
    '''
    if not os.path.exists('team_allocator_teams/'):
        os.mkdir('team_allocator_teams')
    fpath = open('team_allocator_teams/jhb_final_teams.txt','w+')
    for team in jhb_final_teams:
        # fpath.writelines(team)
        # fpath.write('\n')
        fpath.write(' '.join(map(str,team)) + '\n')
    fpath.close() 

def nw_physical_students(nw_physical_students):
    '''
    from the list of nw_campus_students, fill in this function to return a list of all
    students who will be attending physically on campus
    '''
    phokeng_physical_students = []
    for student in nw_physical_students:
        if 'Phokeng Physical' in student:
            phokeng_physical_students.append(student)
    return nw_physical_students

def nw_physical_teams(nw_physical_students):
    '''
    from the list of nw_physical_students, create list of 4 students per team, and add them to 
    one big list
    '''
    phokeng_physical_teams = []
    team = []
    index = 0
    for student in nw_physical_students:
        index += 1
        team.append(student)
        if index == 4:
            phokeng_physical_teams.append(list(team))
            team.clear()
            index = 0
    return phokeng_physical_teams

def nw_teams_file(nw_final_teams):
    '''
    write and save the information in the nw_physical_teams into a textfile
    '''
    if not os.path.exists('team_allocator_teams/'):
            os.mkdir('team_allocator_teams')
    fpath = open('team_allocator_teams/nw_final_teams.txt','w+')
    for team in nw_final_teams:
        fpath.writelines(team)
        fpath.write('\n')
    fpath.close() 


def get_virtual_students(student_list):
    '''
    from the list of students above, fill in this function to return a list of all
    students attending virtually.
    '''
    virtual_students = []
    for student in student_list:
        if 'Virtual' in student:
            virtual_students.append(student)
    return virtual_students


def virtual_teams(virtual_students_list):
    '''
    from the list of virtual_students above,  create list of 4 students per team, and add them to 
        one big list
    '''
    virtual_teams = []
    team = []
    index = 0
    for student in virtual_students_list:
        index += 1
        team.append(student)
        if index == 4:
            virtual_teams.append(list(team))
            team.clear()
            index = 0
    return virtual_teams

def virtual_teams_file(virtual_teams):
    '''
    write and save the information in the virtual_teams into a textfile
    '''
    fpath = open('team_allocator_teams/virtual_teams.txt','w+')
    for team in virtual_teams:
        fpath.writelines(team)
        fpath.write("\n")
    fpath.close()

if __name__ == '__main__':
    '''
    call all your functions below to make your program execute    
    '''
    dbn_campus_students(student_list())
    cpt_campus_students(student_list())
    jhb_campus_students(student_list())
    nw_campus_students(student_list())
    dbn_physical_students(dbn_campus_students(student_list()))
    dbn_physical_teams(dbn_physical_students(dbn_campus_students(student_list())))
    dbn_teams_file(dbn_physical_teams(dbn_physical_students(dbn_campus_students(student_list()))))
    cpt_physical_students(cpt_campus_students(student_list()))
    cpt_physical_teams(cpt_physical_students(cpt_campus_students(student_list())))
    cpt_teams_file(cpt_physical_teams(cpt_physical_students(cpt_campus_students(student_list()))))
    jhb_physical_students(jhb_campus_students(student_list()))
    jhb_physical_teams(jhb_physical_students(jhb_campus_students(student_list())))
    jhb_teams_file(jhb_physical_teams(jhb_physical_students(student_list())))
    nw_physical_students(nw_campus_students(student_list()))
    nw_physical_teams(nw_physical_students(nw_campus_students(student_list())))
    nw_teams_file(nw_physical_teams(nw_physical_students(student_list())))
    get_virtual_students(student_list())
    virtual_teams(get_virtual_students(student_list()))
    virtual_teams_file(virtual_teams(get_virtual_students(student_list())))
