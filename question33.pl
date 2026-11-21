
% Dieting System Based on Disease

disease(diabetes).
disease(blood_pressure).
disease(obesity).

diet(diabetes, low_sugar_food).
diet(blood_pressure, low_salt_food).
diet(obesity, low_fat_food).

% Diet Recommendation Rule

recommend(Disease, Food) :-
    disease(Disease),
    diet(Disease, Food),
    write('Recommended diet: '),
    write(Food).
