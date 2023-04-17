import { Component } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { PC } from 'src/app/models/models';

@Component({
    selector: 'app-add-pc',
    templateUrl: './add-pc.component.html',
    styleUrls: ['./add-pc.component.css']
})
export class AddPcComponent {
    roleFormControl: FormControl = new FormControl('', [Validators.required]);
    salaryFormControl: FormControl = new FormControl('', [Validators.required, Validators.pattern('^[0-9]{1,8}$')]);
    personFormControl: FormControl = new FormControl('', [Validators.required]);
    companyFormControl: FormControl = new FormControl('', [Validators.required]);

    constructor(private apiServ: APIService, private router: Router) { }

    cancel() {
        this.router.navigateByUrl('pc');
    }
    isInputDataValid(): boolean {
        return this.roleFormControl.valid && this.salaryFormControl.valid && this.personFormControl.valid && this.companyFormControl.valid;
    }
    add() {
        let data = new PC();
        data["role"] = this.roleFormControl.value;
        data["salary"] = this.salaryFormControl.value;
        data["company"] = this.personFormControl.value;
        data["person"] = this.companyFormControl.value;

        if (this.isInputDataValid()) {
            this.apiServ.addEntity('pc', data).subscribe(result => {
                alert("Updated successfully!");
            });

        }
        else {
            alert("Error with input data; please change data and try again!");
        }
    }
}
