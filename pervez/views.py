from django.shortcuts import render, redirect
from .models import *


                                                            #HOME PAGE, CLASSES 
def home(request):
    notes = Notes.objects.all()
    classes = Cls.objects.all()
    recommendations = Recommendations.objects.all()
    blogs = Blogs.objects.all()

    context = {
        'notes':notes,
        'classes':classes,
        'recommendations':recommendations,
        'blogs':blogs,

    }
    return render(request, 'pervez/home.html', context)

                                                                    #NOTES 
def Notess(request, cls):
    cl = Cls.objects.get(clss=cls)
    subjects = Subject.objects.all()
    notes = cl.notes_set.all()

    context = {
        'notes':notes,
        'subjects':subjects,

    }
    return render(request, 'pervez/notes.html', context)


                                                                # NOTES PAGE

def notes_page(request):
    classes = Cls.objects.all()
    context = {
        'classes':classes,
    }
    return render(request, 'pervez/notes_page.html', context)

                                                                # PAPER PAGE

def paper_page(request):
    classes = Cls.objects.all()
    context = {
        'classes':classes,
    }
    return render(request, 'pervez/paper_page.html', context)

                                                                #LECTURES PAGE 

def lecture_page(request):
    classes = Cls.objects.all()
    context = {
        'classes':classes,
    }
    return render(request, 'pervez/lectures_page.html', context)


                                                            #QUESTION AND ANSWERS
def question_answers(request, cls):
    cl = Cls.objects.get(clss=cls)
    subjects = Subject.objects.all()
    # questionsanswers = QuestionAnswer.objects.filter(clss=cl)
    
    questionsanswers = QuestionAnswer.objects.all()
    context = {
        'questionsanswers':questionsanswers,
        'subjects':subjects,
        'cl':cl
    }

    return render(request, 'pervez/question&answers.html', context)


                                                            #LECTURES SUBJECTS 
def lectures_subjects(request, cls):
    subjects = Subject.objects.all()
    # subjects = ['Physics', 'Chemistry', 'Biology', 'Maths']
    # lectures = Lectures.objects.filter(clss=cls)
    bio = Subject.objects.get(sub_type__contains="Biology")
    lectures = Lecture_chapter.objects.filter(clss__clss = cls)
    context = {
        'lectures':lectures,
        'subjects':subjects,
        'bio':bio,
    }
    return render(request, 'pervez/lectures_subject.html', context)


                                                                # INDIVIDUAL CHAPTERS 

def per_video(request, pk, chap_name):
    subtop = SubTopic.objects.filter(chapter__sub__id=pk).filter(chapter__chapter__contains=chap_name)
    url_first = str(subtop[0].vedio)+"?wmode=opaque"
    url_first = url_first[0:23] +"/embed/" + url_first[32:]
    print(url_first)
    chap_name = chap_name
    lengths = len(subtop)
    print(lengths)
    context = {
        'subtop':subtop,
        'lengths':lengths,
        'chap_name':chap_name,
        'url':url_first,
    }

    return render(request, 'pervez/indi_chap.html', context)


def subtopics(request, pk, chap_name):
    subtop = SubTopic.objects.filter(chapter__sub__id=pk).filter(chapter__chapter__contains=chap_name)
    
    url_first = str(subtop[0].vedio)+"?wmode=opaque"
    url_first = url_first[0:23] +"/embed/" + url_first[32:]
    print(url_first)
    chap_name = chap_name
    lengths = len(subtop)
    print(lengths)
    context = {
        'subtop':subtop,
        'lengths':lengths,
        'chap_name':chap_name,
        'url':url_first,
    }
    return render(request, 'pervez/subtopic.html', context)




# # lec = Lectures.objects.filter(clss__exact=7)
# lectures = Lectures.objects.filter(clss=7)
# for lecture in lectures:
#     if lecture.sub == 'Physics':
#         print(lecture.chapter)
#     if lecture.sub == 'Chemistry':
#         print(lecture.sub)



# subtop = SubTopic.objects.filter(chapter__sub__contains='Physics').filter(chapter__chapter__contains='forces')

# for subs in subtop:
#     print(subs)
# # if lec.sub == 'Physics':
#     print("hello world")
# if lec.sub == 'Chemistry':
#     print('hello universe')
# print(lectures)



# subtop = SubTopic.objects.filter(sub_topic='velocity')

# print(subtop)