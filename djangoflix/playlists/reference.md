'''python

class CourseGrade():
    student -> FK(student)
    course -> FK(course)


class CourseAttendance():
    student -> FK(student)
    course -> FK(course)
    datetime -> DateTime

class Course():
    student -> M2M()
    # course_obj.coursegrade_set.all()
    # course_obj.courseattendance_set.all()

class Parent():
    name
    # parent_obj.student_set.all()


class Student():
    mother = FK(parent, related_name="mother")
    father = FK(parent, related_name="father")
    # student.course_set.all()
    # student.coursegrade_set.all()
    # student.father
    # student.mother
'''

'''
playlist_a = Playlist.objects.first()
'''
## Add to ManyTomany
'''python
video_a = Video.objects.first()
playlist_a.videos.add(video_a)
'''

## Remove from ManyToMany
'''python
video_a = Video.objects.first()
playlist_a.videos.remove(video_a)
'''

## Set (or reset) ManyToMany
'''python
video_qs = Video.objects.all()
playlist_a.videos.set(video_qs) ## или добавляем список сразу ([video_qs])
'''

##
'''python
playlist_a.videos.clear()
'''

## Queryset from ManyToMany
'''python
playlist_a.videos.all()
'''