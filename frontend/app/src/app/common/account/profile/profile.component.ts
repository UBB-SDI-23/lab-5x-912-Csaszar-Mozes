import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { ManageAccountService } from 'src/app/api/manage-account-service';
import { UserProfile } from 'src/app/models/models';

@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  user?: UserProfile;

  baseUrl: string = 'users';

  firstNameFormControl: FormControl = new FormControl('', [Validators.maxLength(70), Validators.pattern(/^(?!.*[#$%^&*!]).*$/)]);
  lastNameFormControl: FormControl = new FormControl('', [Validators.maxLength(70), Validators.pattern(/^(?!.*[#$%^&*!]).*$/)]);
  bioFormControl: FormControl = new FormControl('', [Validators.maxLength(1000)]);
  universityFormControl: FormControl = new FormControl('', [Validators.maxLength(200), Validators.pattern(/^(?!.*[#$%^&*!]).*$/)]);
  highSchoolFormControl: FormControl = new FormControl('', [Validators.maxLength(200), Validators.pattern(/^(?!.*[#$%^&*!]).*$/)]);
  usernameFormControl: FormControl = new FormControl('');
  emailFormControl: FormControl = new FormControl('');

  constructor(protected manageAccountServ: ManageAccountService, private actRoute: ActivatedRoute, protected router: Router) { }

  isInputDataValid(): boolean {
    return this.firstNameFormControl.valid && this.lastNameFormControl.valid && this.bioFormControl.valid && this.universityFormControl.valid && this.highSchoolFormControl.valid;
  }
  edit() {
    let data = new UserProfile();
    data["first_name"] = this.firstNameFormControl.value;
    data["last_name"] = this.lastNameFormControl.value;
    data["bio"] = this.bioFormControl.value;
    data["university"] = this.universityFormControl.value;
    data["high_school"] = this.highSchoolFormControl.value;

    if (this.isInputDataValid()) {
      this.manageAccountServ.updateProfile(data).subscribe(result => {
        alert("Updated successfully!");
      });
    }
    else {
      alert("Error with input data; please change data and try again!");
    }
  }
  reset() {
    if (confirm("Are you sure you want to reset your profile?")) {
      this.manageAccountServ.resetProfile().subscribe(() => {
        UserProfile.reset(this.user!);
        this.loadDataIntoInputs();
      });
    }
  }

  loadDataIntoInputs() {
    this.firstNameFormControl.setValue(this.user?.first_name!);
    this.lastNameFormControl.setValue(this.user?.last_name!);
    this.universityFormControl.setValue(this.user?.university!);
    this.highSchoolFormControl.setValue(this.user?.high_school!);
    this.bioFormControl.setValue(this.user?.bio!);
    this.usernameFormControl.setValue(this.user?.user?.username!);
    this.emailFormControl.setValue(this.user?.user?.email!);
  }

  ngOnInit(): void {
    this.manageAccountServ.getProfile().subscribe(
      result => {
        this.user = result as UserProfile;
        console.log(this.user);
        this.emailFormControl.disable();
        this.usernameFormControl.disable();
        this.loadDataIntoInputs();
      }
    )
  }
}
