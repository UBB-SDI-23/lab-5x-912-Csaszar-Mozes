import { Component } from '@angular/core';
import { ManageAccountService } from './api/manage-account-service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'app';

  constructor(public manageAccountServ: ManageAccountService) { }

  logOut() {
    if (confirm("Are you sure you want to log out?")) {
      this.manageAccountServ.logOut();
    }
  }
}
