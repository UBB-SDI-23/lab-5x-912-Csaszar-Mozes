import { Component } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { Company, Location as MLocation } from '../../../models/models';
import { MatAutocompleteSelectedEvent } from '@angular/material/autocomplete';

@Component({
    selector: 'app-add-location',
    templateUrl: './add-location.component.html',
    styleUrls: ['./add-location.component.css']
})
export class AddLocationComponent {
    countryFormControl: FormControl = new FormControl('', [Validators.required]);
    cityFormControl: FormControl = new FormControl('', [Validators.required]);
    streetFormControl: FormControl = new FormControl('', [Validators.required]);
    numberFormControl: FormControl = new FormControl('', [Validators.required, Validators.pattern('^[0-9]{1,4}$|^10000$')]);
    apartmentFormControl: FormControl = new FormControl('', [Validators.pattern('^[0-9]{1,4}$|^10000$')]);
    descriptionFormControl: FormControl = new FormControl('');
    companyFormControl: FormControl = new FormControl('', [Validators.required]);
    suggestions: string[] = [];
    companies: Company[] = [];
    autocompleteSize: number = 15;
    companyID: number = -1;

    constructor(private apiServ: APIService, private router: Router) { }

    cancel() {
        this.router.navigateByUrl('locations');
    }
    isInputDataValid(): boolean {
        return this.countryFormControl.valid && this.cityFormControl.valid && this.streetFormControl.valid && this.numberFormControl.valid && this.companyFormControl.valid && this.companyID > 0;
    }
    updateAutocomplete(): void {
        this.apiServ.getAutocompleteEntity('companies', this.companyFormControl.value, this.autocompleteSize).subscribe(
            result => {
                this.companies = result as Company[];
                this.suggestions = this.companies.map(e => e.name!);
            }
        )
    }
    selectCompany(event: MatAutocompleteSelectedEvent) {
        let selected = event.option;
        let ind = event.source.options.reduce((pVal, cVal, ind) => cVal.id == selected.id ? ind : pVal, 0);
        this.companyID = this.companies[ind].id!;
    }
    add() {
        let data = new MLocation();
        data["country"] = this.countryFormControl.value;
        data["city"] = this.cityFormControl.value;
        data["street"] = this.streetFormControl.value;
        data["number"] = this.numberFormControl.value;
        data["apartment"] = this.apartmentFormControl.value;
        data["company"] = this.companyID;
        if (this.isInputDataValid()) {
            this.apiServ.addEntity('locations', data).subscribe(result => {
                alert("Added successfully!");
            });

        }
        else {
            alert("Error with input data; please change data and try again!");
        }
    }
}
