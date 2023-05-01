ALTER TABLE a1_api_company DISABLE TRIGGER ALL;
UPDATE a1_api_company
SET user_id=(SELECT floor(random() * 10000) + 1);
ALTER TABLE a1_api_company ENABLE TRIGGER ALL;
ALTER TABLE a1_api_person DISABLE TRIGGER ALL;
UPDATE a1_api_person
SET user_id=(SELECT floor(random() * 10000) + 1);
ALTER TABLE a1_api_person ENABLE TRIGGER ALL;

ALTER TABLE a1_api_personworkingatcompany DISABLE TRIGGER ALL;
UPDATE a1_api_personworkingatcompany
SET user_id=(SELECT floor(random() * 10000) + 1);
ALTER TABLE a1_api_personworkingatcompany ENABLE TRIGGER ALL;
