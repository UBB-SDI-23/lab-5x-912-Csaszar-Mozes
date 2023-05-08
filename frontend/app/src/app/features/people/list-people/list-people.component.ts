import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { ManageAccountService } from 'src/app/api/manage-account-service';
import { UserRoles } from 'src/app/models/models';

@Component({
  selector: 'app-list-people',
  templateUrl: 'list-people.component.html',
  styleUrls: ['list-people.component.css']
})
export class ListPeopleComponent {
  dynamicColumns = ['first_name', 'last_name', 'email', 'age', 'worker_id', 'nr_workplaces'];
  displayedColumns = ['position', 'first_name', 'last_name', 'email', 'age', 'worker_id', 'nr_workplaces', 'username', 'delete'];
  baseUrl = 'people';
  listPageComp?: HTMLElement;
  constructor(protected apiServ: APIService, private manageAccountServ: ManageAccountService, protected router: Router) { }

  ngOnInit() {
    //Remove delete button if there is no log in or the user is only a normal one
    if (this.manageAccountServ.isLoggedOut() || this.manageAccountServ.getRole() == UserRoles.NORMAL) {
      this.displayedColumns.pop();
    }
  }
}
