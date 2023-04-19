import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { MatAutocompleteSelectedEvent } from '@angular/material/autocomplete';
import { ActivatedRoute, Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { DeleteConfirmationComponent } from 'src/app/common/delete-confirmation/delete-confirmation.component';
import { Company, Person, PC, LocationDetail, PCDetail } from 'src/app/models/models';

@Component({
  selector: 'app-edit-pc',
  templateUrl: './edit-pc.component.html',
  styleUrls: ['./edit-pc.component.css']
})
export class EditPcComponent implements OnInit {
  baseUrl: string = 'pc';
  pc?: PCDetail;

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

  constructor(protected apiServ: APIService, private actRoute: ActivatedRoute, protected router: Router) { }

  cancel() {
    this.router.navigateByUrl(this.baseUrl);
  }
  isInputDataValid(): boolean {
    return this.roleFormControl.valid && this.salaryFormControl.valid && this.personFormControl.valid && this.companyFormControl.valid;
  }
  edit() {
    let data = new PC();
    data["role"] = this.roleFormControl.value;
    data["salary"] = this.salaryFormControl.value;
    data["company"] = this.companyID;
    data["person"] = this.personID;

    if (this.isInputDataValid()) {
      this.apiServ.putEntity(this.baseUrl, this.pc!.id!, data).subscribe(result => {
        alert("Updated successfully!");
      });
    }
    else {
      alert("Error with input data; please change data and try again!");
    }
  }

  delete(event: MouseEvent) {
    event.stopPropagation();
    DeleteConfirmationComponent.setUpConfirmDelete(this.baseUrl, this.baseUrl, Number(this.pc!.id!));
    this.router.navigateByUrl('delete-confirmation');
  }

  ngOnInit(): void {
    this.actRoute.params.subscribe(
      params => {
        this.apiServ.getEntity(this.baseUrl, params['id']).subscribe(
          result => {
            this.pc = result as PCDetail;
            this.roleFormControl.setValue(this.pc.role);
            this.salaryFormControl.setValue(this.pc.salary);
            this.personFormControl.setValue(this.pc.person!.first_name + " " + this.pc.person!.last_name);
            this.companyFormControl.setValue(this.pc.company!.name);
            this.companyID = this.pc.company!.id!;
            this.personID = this.pc.person!.id!;
          }
        )
      }
    );
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
