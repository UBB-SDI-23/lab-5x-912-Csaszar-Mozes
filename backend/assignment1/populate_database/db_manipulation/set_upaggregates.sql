--UPDATE a1_api_company SET avg_salary = (SELECT AVG(PC.salary) FROM a1_api_personworkingatcompany PC WHERE PC.company_id = a1_api_company.id);
--UPDATE a1_api_company SET nr_locations = (SELECT COUNT(*) FROM a1_api_location L WHERE L.company_id = a1_api_company.id);

CREATE OR REPLACE FUNCTION update_company_aggregates() RETURNS trigger AS $$
BEGIN
	IF (TG_OP = 'INSERT') THEN
		UPDATE a1_api_company 
		SET avg_salary = (SELECT AVG(PC.salary) FROM a1_api_personworkingatcompany PC WHERE PC.company_id = a1_api_company.id),
			nr_locations = (SELECT COUNT(*) FROM a1_api_location L WHERE L.company_id = a1_api_company.id)
		WHERE id=NEW.company_id;
	ELSIF (TG_OP = 'DELETE') THEN
		UPDATE a1_api_company 
		SET avg_salary = (SELECT AVG(PC.salary) FROM a1_api_personworkingatcompany PC WHERE PC.company_id = a1_api_company.id),
			nr_locations = (SELECT COUNT(*) FROM a1_api_location L WHERE L.company_id = a1_api_company.id)
		WHERE id=OLD.company_id;
	ELSE
		UPDATE a1_api_company 
		SET avg_salary = (SELECT AVG(PC.salary) FROM a1_api_personworkingatcompany PC WHERE PC.company_id = a1_api_company.id),
			nr_locations = (SELECT COUNT(*) FROM a1_api_location L WHERE L.company_id = a1_api_company.id)
		WHERE id=NEW.company_id OR OLD.company_id;
	END IF;
	RETURN NULL;
    END;
$$ LANGUAGE PLPGSQL;



CREATE OR REPLACE TRIGGER company_aggregates_trigger AFTER DELETE OR INSERT OR UPDATE ON a1_api_personworkingatcompany FOR EACH ROW EXECUTE PROCEDURE update_company_aggregates();
