import { Component } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { ActivatedRoute, Route, Router } from '@angular/router';
import { ManageAccountService } from 'src/app/api/manage-account-service';
import { LoginResponse, Message } from 'src/app/models/models';

@Component({
  selector: 'app-log-in',
  templateUrl: './log-in.component.html',
  styleUrls: ['./log-in.component.css']
})
export class LogInComponent {
  usernameFormControl: FormControl = new FormControl('', [Validators.required]);
  passwordFormControl: FormControl = new FormControl('', [Validators.required, Validators.min(8), Validators.pattern(/(?=.*\d.*\d.*)(?=.*[A-Z]).*/)]);

  constructor(private manageAccountServ: ManageAccountService, private router: Router) { }

  isInputDataValid(): boolean {
    return this.usernameFormControl.valid && this.passwordFormControl.valid;
  }
  logIn() {
    if (this.isInputDataValid()) {
      const username = this.usernameFormControl.value;
      this.manageAccountServ.logIn(username, this.passwordFormControl.value).subscribe(
        (resp) => {
          let res = resp as LoginResponse;
          this.manageAccountServ.saveToken(res.access!);
          this.manageAccountServ.saveRole(res.role!);
          this.manageAccountServ.saveUser(username);
          alert('Login successful!');
          this.router.navigateByUrl('users/profile');
        }, (resp) => {
          if (resp.error.detail.startsWith('Account is not active')) {
            if (confirm('Account is inactive. Activate it now?')) {
              this.manageAccountServ.confirmRegistration(resp.error.detail.split(';')[1]).subscribe(
                (resp) => {
                  let res = resp as Message;
                  alert(res.message!);
                }
              )
            }
            else {
              alert("Account cannot be used for accessing restricted content until activated.")
            }
          }
        }
      )
    }
    else {
      alert("Incorrect username/password combination.");
    }
  }
}
