import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { MatTableDataSource } from '@angular/material/table';
import { ActivatedRoute, Route, Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { DeleteConfirmationComponent } from 'src/app/common/delete-confirmation/delete-confirmation.component';
import { Company, CompanyDetail, Person, PC } from 'src/app/models/models';

@Component({
  selector: 'app-edit-company',
  templateUrl: './edit-company.component.html',
  styleUrls: ['./edit-company.component.css']
})
export class EditCompanyComponent implements OnInit {

  company?: CompanyDetail = new CompanyDetail();
  peopleWorkingHere: PC[] = [];
  locations: Location[] = [];
  nameFormControl: FormControl = new FormControl('', [Validators.required]);
  descriptionFormControl: FormControl = new FormControl('', [Validators.required]);
  netWorthFormControl: FormControl = new FormControl('', [Validators.required, Validators.pattern('^([0-9])*$')]);
  reputationFormControl: FormControl = new FormControl('', [Validators.required, Validators.pattern('^[0-9]?[0-9]$|^100$')]);
  startYearFormControl: FormControl = new FormControl('', [Validators.required, Validators.pattern('^([0-9])*$')]);

  //Paging for auxiliary tables
  pageSize: number = 10;
  peoplePageNr: number = 0;
  locationsPageNr: number = 0;

  baseUrlPeople: string = 'people';
  baseUrlLocations: string = 'locations';

  peopleColumns: string[] = ["role", "salary", "person.name", "person.age", "person.email", "person.worker_id"];
  locationsColumns: string[] = ["country", "county", "city", "street", "number", "apartment", "description"];

  constructor(protected apiServ: APIService, private actRoute: ActivatedRoute, protected router: Router) { }



  edit() {
    let data = new Company();
    data["id"] = this.company?.id;
    data["name"] = this.nameFormControl.value;
    data["description"] = this.descriptionFormControl.value;
    data["net_value"] = this.netWorthFormControl.value;
    data["reputation"] = this.reputationFormControl.value;
    if (this.nameFormControl.valid && this.descriptionFormControl.valid && this.netWorthFormControl.valid && this.reputationFormControl.valid && this.startYearFormControl.valid) {
      this.apiServ.putCompany(this.company!.id!, data).subscribe(result => {
        alert("Updated successfully!");
      });

    }
    else {
      alert("Error with input data; please change data and try again!");
    }

  }

  delete(event: MouseEvent) {
    event.stopPropagation();
    DeleteConfirmationComponent.setUpConfirmDelete('companies', 'companies', Number(this.company!.id!));
    this.router.navigateByUrl('delete-confirmation');
  }

  ngOnInit(): void {
    this.actRoute.params.subscribe(
      params => {
        this.apiServ.getCompany(params['id']).subscribe(
          result => {
            result.people_working_here == undefined ? result.people_working_here = [] : "";
            result.locations == undefined ? result.locations = [] : "";
            this.company = result as CompanyDetail;
            this.nameFormControl.setValue(this.company.name);
            this.descriptionFormControl.setValue(this.company.description);
            this.netWorthFormControl.setValue(this.company.net_value);
            this.reputationFormControl.setValue(this.company.reputation);
            this.startYearFormControl.setValue(this.company.start_year);

            this.locations = result.locations as Location[];
            this.peopleWorkingHere = result.people_working_here as PC[];

          }
        )
      }
    )

  }
}

/*
refreshLocations() {
    this.dataSourceLocations.data = this.locations!.slice(this.locationsPageNr * this.pageSize, this.locationsPageNr * this.pageSize + this.pageSize);
  }
  incLocationsPageNr() {
    if ((this.locationsPageNr + 1) * this.pageSize < this.locations.length) {
      this.locationsPageNr += 1;
      this.refreshLocations();
    }

  }
  decLocationsPageNr() {
    if (this.locationsPageNr > 0) {
      this.locationsPageNr -= 1;
      this.refreshLocations();
    }
  }
  refreshPeople() {
    this.dataSourcePeople.data = this.peopleWorkingHere!.slice(this.peoplePageNr * this.pageSize, this.peoplePageNr * this.pageSize + this.pageSize);
  }
  incPeoplePageNr() {
    if ((this.peoplePageNr + 1) * this.pageSize < this.peopleWorkingHere.length) {
      this.peoplePageNr += 1;
      this.refreshPeople();
    }

  }
  decPeoplePageNr() {
    if (this.peoplePageNr > 0) {
      this.peoplePageNr -= 1;
      this.refreshPeople();
    }
  }
*/