import { Component } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { ManageAccountService } from 'src/app/api/manage-account-service';
import { DeleteConfirmationComponent } from 'src/app/common/delete-confirmation/delete-confirmation.component';
import { PC, PCDetail, Person, PersonDetail } from 'src/app/models/models';

@Component({
  selector: 'app-edit-person',
  templateUrl: './edit-person.component.html',
  styleUrls: ['./edit-person.component.css']
})
export class EditPersonComponent {
  baseUrl: string = "people";
  person?: PersonDetail;

  firstNameFormControl: FormControl = new FormControl('', [Validators.required, Validators.maxLength(50)]);
  lastNameFormControl: FormControl = new FormControl('', [Validators.required, Validators.maxLength(50)]);
  emailFormControl: FormControl = new FormControl('', [Validators.required, Validators.email, Validators.maxLength(75)]);
  ageFormControl: FormControl = new FormControl('', [Validators.required, Validators.pattern('^[012]?[0-9]{1,2}$')]);
  workerIDFormControl: FormControl = new FormControl('', [Validators.required, Validators.pattern('^[0-9]{1,10}$')]);

  redirectEntityPropertyCompanies: string = 'company.id';
  companyColumns: string[] = ['role', 'salary', 'company.name', 'company.description', 'company.net_value', 'company.reputation'];
  baseUrlCompany: string = "companies";

  workingAtCompanies: PCDetail[] = [];

  canEdit: boolean = false;

  constructor(protected apiServ: APIService, private manageAccountServ: ManageAccountService, private actRoute: ActivatedRoute, protected router: Router) { }

  cancel() {
    this.router.navigateByUrl('people');
  }
  isInputDataValid(): boolean {
    return this.firstNameFormControl.valid && this.lastNameFormControl.valid && this.emailFormControl.valid && this.ageFormControl.valid && this.workerIDFormControl.valid;
  }
  edit() {
    let data = new Person();
    data["first_name"] = this.firstNameFormControl.value;
    data["last_name"] = this.lastNameFormControl.value;
    data["email"] = this.emailFormControl.value;
    data["age"] = this.ageFormControl.value;
    data["worker_id"] = this.workerIDFormControl.value;

    if (this.isInputDataValid()) {
      this.apiServ.putEntity(this.baseUrl, this.person!.id!, data).subscribe(result => {
        alert("Updated successfully!");
      });

    }
    else {
      alert("Error with input data; please change data and try again!");
    }
  }
  delete(event: MouseEvent) {
    event.stopPropagation();
    DeleteConfirmationComponent.setUpConfirmDelete(this.baseUrl, this.baseUrl, Number(this.person!.id!));
    this.router.navigateByUrl('delete-confirmation');
  }

  ngOnInit(): void {
    this.actRoute.params.subscribe(
      params => {
        this.apiServ.getEntity(this.baseUrl, params['id']).subscribe(
          result => {
            this.person = result as PersonDetail;
            this.firstNameFormControl.setValue(this.person.first_name);
            this.lastNameFormControl.setValue(this.person.last_name);
            this.emailFormControl.setValue(this.person.email);
            this.ageFormControl.setValue(this.person.age);
            this.workerIDFormControl.setValue(this.person.worker_id);

            this.workingAtCompanies = this.person!.working_at_companies as PCDetail[];

            this.canEdit = this.manageAccountServ.isLoggedInAsModerator() || this.manageAccountServ.isLoggedInAsAdmin() ||
              this.manageAccountServ.isLoggedInAndOwnsObject(this.person.user?.username!);
          }
        )
      }
    );
  }
}
