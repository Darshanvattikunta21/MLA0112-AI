% Program 33: Dieting suggestion system based on disease.
% Sample queries:
% ?- diet_for(diabetes, Diet).
% ?- suggest_diet(hypertension).

disease(diabetes).
disease(hypertension).
disease(obesity).
disease(anemia).
disease(heart_disease).

avoid(diabetes, sugar).
avoid(diabetes, sweet_drinks).
avoid(hypertension, excess_salt).
avoid(hypertension, fried_food).
avoid(obesity, junk_food).
avoid(obesity, sugary_food).
avoid(anemia, tea_after_meals).
avoid(heart_disease, trans_fat).
avoid(heart_disease, oily_food).

recommend(diabetes, whole_grains).
recommend(diabetes, green_vegetables).
recommend(hypertension, fruits).
recommend(hypertension, low_sodium_food).
recommend(obesity, salads).
recommend(obesity, high_fiber_food).
recommend(anemia, iron_rich_food).
recommend(anemia, leafy_vegetables).
recommend(heart_disease, oats).
recommend(heart_disease, nuts).

diet_for(Disease, Diet) :-
    disease(Disease),
    setof(Food, recommend(Disease, Food), Diet).

foods_to_avoid(Disease, Foods) :-
    disease(Disease),
    setof(Food, avoid(Disease, Food), Foods).

suggest_diet(Disease) :-
    diet_for(Disease, Diet),
    foods_to_avoid(Disease, Avoid),
    write('Recommended foods: '),
    write(Diet),
    nl,
    write('Avoid: '),
    write(Avoid),
    nl.
