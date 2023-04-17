import { Component } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { Company } from 'src/app/models/models';

@Component({
    selector: 'app-edit-location',
    templateUrl: './edit-location.component.html',
    styleUrls: ['./edit-location.component.css']
})
export class EditLocationComponent {
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
}
