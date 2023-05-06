export class NrTotalPages {
    nr_total_pages?: number;
    nr_results?: number;
}

export class RegistrationMessage {
    activation_token?: string;
}

export class LoginResponse {
    access?: string;
    refresh?: string;
}

export class Message {
    message?: string;
}

class User {
    id?: number;
    username?: string;
    email?: string;
    is_active?: boolean;
}

export class RegisterUser {
    username?: string;
    email?: string;
    password?: string;
    password2?: string;
}

export class UserProfile {
    id?: number;
    first_name?: string;
    last_name?: string;
    bio?: string;
    high_school?: string;
    university?: string;
    user?: User;
    nr_entities_added?: number;

    static reset(user: UserProfile) {
        user.first_name = '';
        user.last_name = '';
        user.bio = '';
        user.high_school = '';
        user.university = '';
    }
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
    user?: User;
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
    user?: User;


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
    user?: User;


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
    user?: User;


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
    user?: User;

}

export class PC {
    id?: number;
    role?: string;
    salary?: number;
    person?: number;
    company?: number;
    user?: User;

}

export class PCDetail {
    id?: number;
    role?: string;
    salary?: number;
    person?: Person;
    company?: Company;
    user?: User;

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
    user?: User;

}



// export class PersonCompanyFull {
//     id?: number;
//     role?: string;
//     salary?: number;
//     p_id?: number;
//     first_name?: string;
//     last_name?: string;
//     email?: string;
//     age?: number;
//     worker_id?: number;
//     nr_workplaces?: number;
//     c_id?: number;
//     name?: string;
//     start_year?: number;
//     description?: string;
//     net_value?: number;
//     reputation?: number;
//     nr_workers?: number;
//     nr_locations?: number;
//     user?: User;



//     constructor(person: PC) {
//         this.role = person.role;
//         this.salary = person.salary;
//         this.id = person.id;
//     }
// }