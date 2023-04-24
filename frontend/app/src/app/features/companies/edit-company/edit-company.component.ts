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
  baseUrl: string = 'companies';
  company?: CompanyDetail = new CompanyDetail();

  peopleWorkingHere: PC[] = [];
  locations: Location[] = [];
  nameFormControl: FormControl = new FormControl('', [Validators.required]);
  descriptionFormControl: FormControl = new FormControl('', [Validators.required]);
  netWorthFormControl: FormControl = new FormControl('', [Validators.required, Validators.pattern('^([0-9])*$')]);
  reputationFormControl: FormControl = new FormControl('', [Validators.required, Validators.pattern('^[0-9]?[0-9]$|^100$')]);
  startYearFormControl: FormControl = new FormControl('', [Validators.required, Validators.pattern('^([0-9])*$')]);

  baseUrlPeople: string = 'people';
  baseUrlLocations: string = 'locations';

  peopleColumns: string[] = ["role", "salary", "person.first_name", "person.last_name", "person.age", "person.email", "person.worker_id"];
  locationsColumns: string[] = ["country", "city", "street", "number", "apartment", "description"];

  constructor(protected apiServ: APIService, private actRoute: ActivatedRoute, protected router: Router) { }

  cancel() {
    this.router.navigateByUrl(this.baseUrl);
  }

  isInputDataValid(): boolean {
    return this.nameFormControl.valid && this.descriptionFormControl.valid && this.netWorthFormControl.valid && this.reputationFormControl.valid && this.startYearFormControl.valid;
  }

  edit() {
    let data = new Company();
    data["id"] = this.company?.id;
    data["name"] = this.nameFormControl.value;
    data["description"] = this.descriptionFormControl.value;
    data["net_value"] = this.netWorthFormControl.value;
    data["reputation"] = this.reputationFormControl.value;
    if (this.isInputDataValid()) {
      this.apiServ.putEntity(this.baseUrl, this.company!.id!, data).subscribe(result => {
        alert("Updated successfully!");
      });
    }
    else {
      alert("Error with input data; please change data and try again!");
    }
  }

  delete(event: MouseEvent) {
    event.stopPropagation();
    DeleteConfirmationComponent.setUpConfirmDelete(this.baseUrl, this.baseUrl, Number(this.company!.id!));
    this.router.navigateByUrl('delete-confirmation');
  }

  ngOnInit(): void {
    this.actRoute.params.subscribe(
      params => {
        this.apiServ.getEntity(this.baseUrl, params['id']).subscribe(
          result => {
            let c_result = result as CompanyDetail;
            c_result.people_working_here == undefined ? c_result.people_working_here = [] : "";
            c_result.locations == undefined ? c_result.locations = [] : "";
            this.company = c_result;
            this.nameFormControl.setValue(this.company.name);
            this.descriptionFormControl.setValue(this.company.description);
            this.netWorthFormControl.setValue(this.company.net_value);
            this.reputationFormControl.setValue(this.company.reputation);
            this.startYearFormControl.setValue(this.company.start_year);

            this.locations = c_result.locations as Location[];
            this.peopleWorkingHere = c_result.people_working_here as PC[];
          }
        )
      }
    )
  }
}