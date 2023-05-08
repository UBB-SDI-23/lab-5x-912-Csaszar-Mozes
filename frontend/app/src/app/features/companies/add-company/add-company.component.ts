import { Component } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { ManageAccountService } from 'src/app/api/manage-account-service';
import { Company } from 'src/app/models/models';


@Component({
    selector: 'app-add-company',
    templateUrl: './add-company.component.html',
    styleUrls: ['./add-company.component.css']
})
export class AddCompanyComponent {
    nameFormControl: FormControl = new FormControl('', [Validators.required]);
    descriptionFormControl: FormControl = new FormControl('', [Validators.required]);
    netWorthFormControl: FormControl = new FormControl('', [Validators.required, Validators.pattern('^([0-9])*$')]);
    //, Validators.pattern('^[0-9]?[0-9]$|^100$')
    reputationFormControl: FormControl = new FormControl('', [Validators.required]);
    startYearFormControl: FormControl = new FormControl('', [Validators.required, Validators.pattern('^([0-9])*$')]);

    constructor(private apiServ: APIService, private manageAccountServ: ManageAccountService, private router: Router) { }

    cancel() {
        this.router.navigateByUrl('companies');
    }
    isInputDataValid(): boolean {
        return this.nameFormControl.valid && this.descriptionFormControl.valid && this.netWorthFormControl.valid && this.reputationFormControl.valid && this.startYearFormControl.valid;
    }
    add() {
        let data = new Company();
        data["name"] = this.nameFormControl.value;
        data["description"] = this.descriptionFormControl.value;
        data["net_value"] = this.netWorthFormControl.value;
        data["reputation"] = this.reputationFormControl.value;
        data["start_year"] = this.startYearFormControl.value;
        if (this.isInputDataValid()) {
            this.apiServ.addEntity('companies', data).subscribe(result => {
                alert("Updated successfully!");
            });

        }
        else {
            alert("Error with input data; please change data and try again!");
        }
    }
}
