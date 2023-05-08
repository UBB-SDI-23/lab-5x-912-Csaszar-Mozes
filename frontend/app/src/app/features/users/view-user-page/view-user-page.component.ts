import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { UserProfile } from 'src/app/models/models';

@Component({
  selector: 'app-view-user-page',
  templateUrl: './view-user-page.component.html',
  styleUrls: ['./view-user-page.component.css']
})
export class ViewUserPageComponent implements OnInit {
  user?: UserProfile;

  baseUrl: string = 'users';
  firstNameFormControl: FormControl = new FormControl('');
  lastNameFormControl: FormControl = new FormControl('');
  bioFormControl: FormControl = new FormControl('');
  universityFormControl: FormControl = new FormControl('');
  highSchoolFormControl: FormControl = new FormControl('');
  usernameFormControl: FormControl = new FormControl('');
  emailFormControl: FormControl = new FormControl('');

  constructor(protected apiServ: APIService, private actRoute: ActivatedRoute, protected router: Router) { }

  ngOnInit(): void {
    this.actRoute.params.subscribe(
      params => {
        this.apiServ.getEntity(this.baseUrl, params['id']).subscribe(
          result => {
            this.user = result as UserProfile;
            this.firstNameFormControl.setValue(this.user.first_name);
            this.lastNameFormControl.setValue(this.user.last_name);
            this.universityFormControl.setValue(this.user.university);
            this.highSchoolFormControl.setValue(this.user.high_school);
            this.bioFormControl.setValue(this.user.bio);
            this.usernameFormControl.setValue(this.user.user?.username);
            this.emailFormControl.setValue(this.user.user?.email);
          }
        )
      }
    );
  }
}
