% Program 37: Medical diagnosis.
% Sample queries:
% ?- diagnose([fever, cough, sore_throat], Disease).
% ?- advice(flu, Advice).

symptom(cold, sneezing).
symptom(cold, runny_nose).
symptom(cold, sore_throat).

symptom(flu, fever).
symptom(flu, cough).
symptom(flu, body_pain).
symptom(flu, headache).

symptom(malaria, fever).
symptom(malaria, chills).
symptom(malaria, sweating).

symptom(typhoid, fever).
symptom(typhoid, stomach_pain).
symptom(typhoid, weakness).

advice(cold, 'Drink warm fluids and take rest.').
advice(flu, 'Take rest and consult a doctor if fever continues.').
advice(malaria, 'Consult a doctor for blood test and treatment.').
advice(typhoid, 'Consult a doctor and drink safe water.').

has_symptom(Disease, Symptom) :-
    symptom(Disease, Symptom).

diagnose(Symptoms, Disease) :-
    symptom(Disease, _),
    forall(member(Symptom, Symptoms), has_symptom(Disease, Symptom)).

diagnosis_with_advice(Symptoms, Disease, Advice) :-
    diagnose(Symptoms, Disease),
    advice(Disease, Advice).
