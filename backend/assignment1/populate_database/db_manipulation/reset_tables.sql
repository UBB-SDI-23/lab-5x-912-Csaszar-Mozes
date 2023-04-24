DELETE FROM a1_api_personworkingatcompany;
DELETE FROM a1_api_location;
DELETE FROM a1_api_company;
DELETE FROM a1_api_person;
DELETE FROM sqlite_sequence WHERE name = 'a1_api_company' OR name = 'a1_api_personworkingatcompany' OR name = 'a1_api_person' OR name = 'a1_api_location';