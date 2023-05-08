import { Component } from '@angular/core';
import { ManageAccountService } from './api/manage-account-service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';
  static errors: Object = {};

  constructor(public manageAccountServ: ManageAccountService, private router: Router) { }

  logOut() {
    if (confirm("Are you sure you want to log out?")) {
      this.manageAccountServ.logOut();
      this.router.navigateByUrl('login');
    }
  }

  hasErrors() {
    return Object.keys(AppComponent.errors).length != 0;
  }
}
