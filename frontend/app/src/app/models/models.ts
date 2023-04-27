export class NrTotalPages {
    nr_total_pages?: number;
}

class User {
    id?: number;
    username?: string;
    email?: string;
    is_active?: boolean;
}

export class UserProfile {
    id?: number;
    first_name?: string;
    last_name?: string;
    bio?: string;
    high_school?: string;
    university?: string;
    user?: User;
}

export class Company {
    id?: number;
    name?: string;
    start_year?: number;
    description?: string;
    net_value?: number;
    reputation?: number;
    nr_workers?: number;
    nr_locations?: number;
}

export class Location {
    id?: number;
    country?: string;
    city?: string;
    street?: string;
    number?: number;
    apartment?: string;
    description?: string;
    company?: number;

    toString() {
        return this.country + ", " + this.city + ", " + this.street + " " + this.number + (this.apartment != "" ? ", " + this.apartment : "");
    }
}

export class LocationDetail {
    id?: number;
    country?: string;
    city?: string;
    street?: string;
    number?: number;
    apartment?: string;
    description?: string;
    company?: Company;

    toString() {
        return this.country + ", " + this.city + ", " + this.street + " " + this.number + (this.apartment != "" ? ", " + this.apartment : "");
    }
}

export class Person {
    id?: number;
    first_name?: string;
    last_name?: string;
    email?: string;
    age?: number;
    worker_id?: number;
    nr_workplaces?: number;

    toString() {
        return "Name: " + this.first_name + " " + this.last_name + "; E-mail: " + this.email + "; Age: " + this.age + "; Worker id: " + this.worker_id + "; Nr. workplaces: " + this.nr_workplaces;
    }
}

export class PersonDetail {
    id?: number;
    first_name?: string;
    last_name?: string;
    email?: string;
    age?: number;
    worker_id?: number;
    working_at_companies?: Company[];
}

export class PC {
    id?: number;
    role?: string;
    salary?: number;
    person?: number;
    company?: number;
}

export class PCDetail {
    id?: number;
    role?: string;
    salary?: number;
    person?: Person;
    company?: Company;
}

export class PersonCompanyFull {
    id?: number;
    role?: string;
    salary?: number;
    p_id?: number;
    first_name?: string;
    last_name?: string;
    email?: string;
    age?: number;
    worker_id?: number;
    nr_workplaces?: number;
    c_id?: number;
    name?: string;
    start_year?: number;
    description?: string;
    net_value?: number;
    reputation?: number;
    nr_workers?: number;
    nr_locations?: number;


    constructor(person: PC) {
        this.role = person.role;
        this.salary = person.salary;
        this.id = person.id;
    }
}

export class CompanyDetail {
    name?: string;
    id?: number;
    start_year?: number;
    description?: string;
    net_value?: number;
    reputation?: number;
    people_working_here: Person[] = [];
    locations: Location[] = [];
}