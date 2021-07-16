import requests

def API_call(api):
    a = requests.get(api)
    a1 = a.text
    return a1
def json_file_creation(a1):
    import json
    with open("courses.json","w") as f:
        python_dict=json.loads(a1)
        json.dump(python_dict,f,indent=4)
    with open("courses.json","r") as f:
        data = json.load(f)
    return data
def course_list():
    api = "http://saral.navgurukul.org/api/courses"
    k=API_call(api)
    data = json_file_creation(k)
    id_of_courses = [] 
    i = 0
    while i < len(data['availableCourses']):
        print(i,".",data['availableCourses'][i]['name'])
        id_of_courses.append(data['availableCourses'][i]['id'])
        i+=1 
    return id_of_courses
    
def excercise_list(id_of_courses,select_course):
    api = "http://saral.navgurukul.org/api/courses/" + id_of_courses[select_course] + "/exercises"
    k = API_call(api)
    exercise_info = json_file_creation(k)

    i = 0
    list_of_slug = []
    while i < len(exercise_info['data']):
        print(i,".",exercise_info['data'][i]['name'])
        list_of_slug.append(exercise_info['data'][i]['slug'])
        j = 0 
        while j < len(exercise_info['data'][i]['childExercises']):
            print("     ",j,".",exercise_info['data'][i]['childExercises'][j]['name'])
            list_of_slug.append(exercise_info['data'][i]['childExercises'][j]['slug'])
            j+=1   
        i+=1
    return list_of_slug
    
def slug_list(id_of_courses,list_of_slug,select_course,slug_slect):
    api = "http://saral.navgurukul.org/api/courses/"+id_of_courses[select_course] +"/exercise/getBySlug?slug="+list_of_slug[slug_slect]
    k = API_call(api)
    slug_info = json_file_creation(k)
    print(slug_info['content'])
        

# main function:-   
def cource():
    id_of_courses = course_list()
    select_course = int(input("select the course u want by selecting cooresponding number:"))
    list_of_slug = excercise_list(id_of_courses,select_course)
    print("these are the list of slugs:")
    n = 0
    while n < len(list_of_slug):
        print(n,".",list_of_slug[n])
        n+=1
    slug_slect = int(input("select the slug by choosing corresponding number"))
    slug_list(id_of_courses,list_of_slug,select_course,slug_slect)
    while True:
        next_step = input("coose your next step:")
        if next_step == "next":
            slugs = requests.get("http://saral.navgurukul.org/api/courses/"+id_of_courses[select_course] +"/exercise/getBySlug?slug="+list_of_slug[slug_slect+1])
            s1 = slugs.text
            slug_info = json_file_creation(s1)
            print(slug_info['content'])
        elif next_step == "prev":
            slugs = requests.get("http://saral.navgurukul.org/api/courses/"+id_of_courses[select_course] +"/exercise/getBySlug?slug="+list_of_slug[slug_slect-1])
            s1 = slugs.text
            slug_info = json_file_creation(s1)
            print(slug_info['content'])
        elif next_step == "up":
            id_of_courses = course_list()
            select_course = int(input("select the course u want by selecting cooresponding number:"))
            list_of_slug = excercise_list(id_of_courses,select_course)
            print("these are the list of slugs:")
            n = 0
            while n < len(list_of_slug):
                print(n,".",list_of_slug[n])
                n+=1
            slug_slect = int(input("select the slug by choosing corresponding number"))
            slug_list(id_of_courses,list_of_slug,select_course,slug_slect)
        elif next_step == "exit":
            break
cource()        