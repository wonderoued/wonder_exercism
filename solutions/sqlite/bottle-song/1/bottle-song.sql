-- Schema:
-- CREATE TABLE "bottle-song" (
--         start_bottles INTEGER NOT NULL,
--         take_down     INTEGER NOT NULL,
--         result        TEXT
-- );
-- Task: update bottle-song table and set the result based on the
-- start_bottles and take_down.


UPDATE
  "bottle-song"
SET
  result = (
    -- Début du Couplet (N en texte Majuscule)
    CASE start_bottles
      WHEN 10 THEN 'Ten'
      WHEN 9 THEN 'Nine'
      WHEN 8 THEN 'Eight'
      WHEN 7 THEN 'Seven'
      WHEN 6 THEN 'Six'
      WHEN 5 THEN 'Five'
      WHEN 4 THEN 'Four'
      WHEN 3 THEN 'Three'
      WHEN 2 THEN 'Two'
      WHEN 1 THEN 'One'
    END || ' green bottles hanging on the wall,\n' ||
    
    -- Répétition de la première ligne
    CASE start_bottles
      WHEN 10 THEN 'Ten'
      WHEN 9 THEN 'Nine'
      WHEN 8 THEN 'Eight'
      WHEN 7 THEN 'Seven'
      WHEN 6 THEN 'Six'
      WHEN 5 THEN 'Five'
      WHEN 4 THEN 'Four'
      WHEN 3 THEN 'Three'
      WHEN 2 THEN 'Two'
      WHEN 1 THEN 'One'
    END || ' green bottles hanging on the wall,\n' ||
    
    -- Ligne fixe
    'And if one green bottle should accidentally fall,\n' ||
    
    -- Fin du Couplet (N-1 en texte minuscule/spécial, avec correction de l'apostrophe)
    'There''ll be ' ||
    CASE (start_bottles - 1)
      WHEN 9 THEN 'nine'
      WHEN 8 THEN 'eight'
      WHEN 7 THEN 'seven'
      WHEN 6 THEN 'six'
      WHEN 5 THEN 'five'
      WHEN 4 THEN 'four'
      WHEN 3 THEN 'three'
      WHEN 2 THEN 'two'
      WHEN 1 THEN 'one'
      WHEN 0 THEN 'no'
    END || ' green bottles hanging on the wall.'
  );


