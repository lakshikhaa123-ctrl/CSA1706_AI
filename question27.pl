
% Database with Name and DOB

person(arun, date(10, 5, 2005)).
person(priya, date(15, 6, 2006)).
person(ravi, date(20, 7, 2005)).

show_dob(Name, DOB) :-
    person(Name, DOB).
