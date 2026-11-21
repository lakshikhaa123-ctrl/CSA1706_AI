
% Student-Teacher-Subject Database

student(101, arun).
student(102, priya).
student(103, ravi).

teacher(t1, kumar).
teacher(t2, priya_teacher).

subject(s1, mathematics).
subject(s2, computer_science).

teaches(t1, s1).
teaches(t2, s2).

enrolled(101, s1).
enrolled(102, s2).
enrolled(103, s1).

% Find student, teacher and subject

details(Student, Teacher, Subject) :-
    student(ID, Student),
    enrolled(ID, SubCode),
    teaches(TeacherID, SubCode),
    teacher(TeacherID, Teacher),
    subject(SubCode, Subject).
