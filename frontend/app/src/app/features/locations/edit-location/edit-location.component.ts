import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { MatAutocompleteSelectedEvent } from '@angular/material/autocomplete';
import { ActivatedRoute, Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { DeleteConfirmationComponent } from 'src/app/common/delete-confirmation/delete-confirmation.component';
import { Company, CompanyDetail, Location, LocationDetail } from 'src/app/models/models';

@Component({
    selector: 'app-edit-location',
    templateUrl: './edit-location.component.html',
    styleUrls: ['./edit-location.component.css']
})
export class EditLocationComponent implements OnInit {
    baseUrl: string = "locations";
    location?: LocationDetail;

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


    constructor(protected apiServ: APIService, private actRoute: ActivatedRoute, protected router: Router) { }

    cancel() {
        this.router.navigateByUrl(this.baseUrl);
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

    edit() {
        let data = new Location();
        data["id"] = this.location?.id;
        data["country"] = this.countryFormControl.value;
        data["city"] = this.cityFormControl.value;
        data["street"] = this.streetFormControl.value;
        data["number"] = this.numberFormControl.value;
        data["apartment"] = this.apartmentFormControl.value;
        data["company"] = this.companyID;
        if (this.isInputDataValid()) {
            this.apiServ.putEntity(this.baseUrl, this.location!.id!, data).subscribe(result => {
                alert("Updated successfully!");
            });
        }
        else {
            alert("Error with input data; please change data and try again!");
        }
    }

    delete(event: MouseEvent) {
        event.stopPropagation();
        DeleteConfirmationComponent.setUpConfirmDelete(this.baseUrl, this.baseUrl, Number(this.location!.id!));
        this.router.navigateByUrl('delete-confirmation');
    }

    ngOnInit(): void {
        this.actRoute.params.subscribe(
            params => {
                this.apiServ.getEntity(this.baseUrl, params['id']).subscribe(
                    result => {
                        this.location = result as LocationDetail;
                        this.countryFormControl.setValue(this.location.country);
                        this.descriptionFormControl.setValue(this.location.description);
                        this.cityFormControl.setValue(this.location.city);
                        this.streetFormControl.setValue(this.location.street);
                        this.numberFormControl.setValue(this.location.number);
                        this.apartmentFormControl.setValue(this.location.apartment);
                        this.companyFormControl.setValue(this.location.company!.name);
                        this.companyID = this.location.company!.id!;
                    }
                )
            }
        );
    }
}
