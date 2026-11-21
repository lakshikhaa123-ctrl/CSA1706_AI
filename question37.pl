
% Patient symptoms
symptom(fever).
symptom(cough).
symptom(headache).

% Diagnosis rules
disease(flu) :-
    symptom(fever),
    symptom(cough),
    symptom(headache).

disease(cold) :-
    symptom(cough),
    symptom(sneezing).

disease(malaria) :-
    symptom(fever),
    symptom(headache),
    symptom(chills).
