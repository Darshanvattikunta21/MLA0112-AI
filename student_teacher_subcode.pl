% Program 28: Student-Teacher-Subject Code database.
% Sample queries:
% ?- teacher_of(alice, Teacher).
% ?- students_under_teacher(dr_smith, Students).
% ?- subject_code(Subject, cs102).

student(alice).
student(bob).
student(charlie).
student(diana).

teacher(dr_smith).
teacher(prof_jones).
teacher(ms_clark).

subject(programming, cs101).
subject(database_systems, cs102).
subject(ai, cs103).

studies(alice, cs101).
studies(alice, cs102).
studies(bob, cs102).
studies(charlie, cs103).
studies(diana, cs101).

teaches(dr_smith, cs101).
teaches(prof_jones, cs102).
teaches(ms_clark, cs103).

subject_code(Subject, Code) :-
    subject(Subject, Code).

teacher_of(Student, Teacher) :-
    studies(Student, Code),
    teaches(Teacher, Code).

student_subject(Student, Subject) :-
    studies(Student, Code),
    subject(Subject, Code).

students_under_teacher(Teacher, Students) :-
    setof(Student, Code^(teaches(Teacher, Code), studies(Student, Code)), Students).
