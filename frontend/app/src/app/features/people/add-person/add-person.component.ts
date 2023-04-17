import { Component } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { Company, Person } from 'src/app/models/models';

@Component({
    selector: 'app-add-person',
    templateUrl: './add-person.component.html',
    styleUrls: ['./add-person.component.css']
})
export class AddPersonComponent {
    firstNameFormControl: FormControl = new FormControl('', [Validators.required]);
    lastNameFormControl: FormControl = new FormControl('', [Validators.required]);
    emailFormControl: FormControl = new FormControl('', [Validators.required, Validators.email]);
    ageFormControl: FormControl = new FormControl('', [Validators.required, Validators.pattern('^[012]?[0-9]{1,2}$')]);
    workerIDFormControl: FormControl = new FormControl('', [Validators.required, Validators.pattern('^[0-9]{1,10}$')]);

    constructor(private apiServ: APIService, private router: Router) { }

    cancel() {
        this.router.navigateByUrl('people');
    }
    isInputDataValid(): boolean {
        return this.firstNameFormControl.valid && this.lastNameFormControl.valid && this.emailFormControl.valid && this.ageFormControl.valid && this.workerIDFormControl.valid;
    }
    add() {
        let data = new Person();
        data["first_name"] = this.firstNameFormControl.value;
        data["last_name"] = this.lastNameFormControl.value;
        data["email"] = this.emailFormControl.value;
        data["age"] = this.ageFormControl.value;
        data["worker_id"] = this.workerIDFormControl.value;

        if (this.isInputDataValid()) {
            this.apiServ.addEntity('people', data).subscribe(result => {
                alert("Updated successfully!");
            });

        }
        else {
            alert("Error with input data; please change data and try again!");
        }
    }
}
