import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { ManageAccountService } from 'src/app/api/manage-account-service';

@Component({
  selector: 'app-list-users',
  templateUrl: './list-users.component.html',
  styleUrls: ['./list-users.component.css']
})
export class ListUsersComponent {
  dynamicColumns = ['first_name', 'last_name', 'user.email', 'user.username'];
  displayedColumns = ['first_name', 'last_name', 'user.email', 'user.username', 'edit_role'];
  baseUrl = 'users';
  constructor(protected apiServ: APIService, private manageAccountServ: ManageAccountService, protected router: Router) { }
}
