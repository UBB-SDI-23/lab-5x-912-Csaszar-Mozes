import { Component, OnInit } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { APIService } from 'src/app/api/api-service';
import { ManageAccountService } from 'src/app/api/manage-account-service';
import { Message, RegisterUser, RegistrationMessage } from 'src/app/models/models';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.css']
})
export class RegisterComponent {
  usernameFormControl: FormControl = new FormControl('', [Validators.required]);
  emailFormControl: FormControl = new FormControl('', [Validators.required, Validators.email]);
  passwordFormControl: FormControl = new FormControl('', [Validators.required, Validators.min(8), Validators.pattern(/(?=.*\d.*\d.*)(?=.*[A-Z]).*/)]);
  password2FormControl: FormControl = new FormControl('', [Validators.required]);

  pass1MatchesPass2: boolean = true;
  passwordsShouldMatchError?: HTMLElement;

  constructor(private manageAccountServ: ManageAccountService) { }

  updateMatch() {
    if (this.passwordFormControl.value != this.password2FormControl.value) {
      this.password2FormControl.setErrors({ 'notMatching': true });
    }
    else {
      this.password2FormControl.setErrors(null);
    }
  }
  isInputDataValid(): boolean {
    return this.usernameFormControl.valid && this.emailFormControl.valid && this.passwordFormControl.valid && this.password2FormControl.valid;
  }
  signUp() {
    if (this.isInputDataValid()) {
      let user: RegisterUser = new RegisterUser();
      user.email = this.emailFormControl.value;
      user.username = this.usernameFormControl.value;
      user.password = this.passwordFormControl.value;
      user.password2 = this.password2FormControl.value;
      this.manageAccountServ.registerUser(user).subscribe(
        (resp) => {
          let res = resp as RegistrationMessage;
          console.log(resp, res);
          if (confirm('Activate your account now?')) {
            this.manageAccountServ.confirmRegistration(res.activation_token!).subscribe(
              (resp) => {
                let res = resp as Message;
                alert(res.message!);
              }
            )
          }
          else {
            alert(`Your confirmation token: ${res.activation_token}`);
          }
        }
      )
    }
  }
}
