import { Component } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { MatAutocompleteSelectedEvent } from '@angular/material/autocomplete';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { Company, PC, Person } from 'src/app/models/models';

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

    autocompleteSize: number = 15;
    companiesSuggestions: string[] = [];
    companies: Company[] = [];
    companyID: number = -1;
    peopleSuggestions: string[] = [];
    people: Person[] = [];
    personID: number = -1;

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
        data["company"] = this.companyID;
        data["person"] = this.personID;

        if (this.isInputDataValid()) {
            this.apiServ.addEntity('pc', data).subscribe(result => {
                alert("Updated successfully!");
            });

        }
        else {
            alert("Error with input data; please change data and try again!");
        }
    }
    updateCompaniesAutocomplete(): void {
        this.apiServ.getAutocompleteEntity('companies', this.companyFormControl.value, this.autocompleteSize).subscribe(
            result => {
                this.companies = result as Company[];
                this.companiesSuggestions = this.companies.map(e => e.name!);
            }
        )
    }
    selectCompany(event: MatAutocompleteSelectedEvent) {
        let selected = event.option;
        let ind = event.source.options.reduce((pVal, cVal, ind) => cVal.id == selected.id ? ind : pVal, 0);
        this.companyID = this.companies[ind].id!;
    }
    updatePeopleAutocomplete(): void {
        this.apiServ.getAutocompleteEntity('people', this.personFormControl.value, this.autocompleteSize).subscribe(
            result => {
                this.people = result as Person[];
                this.peopleSuggestions = this.people.map(e => e.first_name! + " " + e.last_name! + ", " + e.email);
            }
        )
    }
    selectPerson(event: MatAutocompleteSelectedEvent) {
        let selected = event.option;
        let ind = event.source.options.reduce((pVal, cVal, ind) => cVal.id == selected.id ? ind : pVal, 0);
        this.personID = this.people[ind].id!;
    }
}
