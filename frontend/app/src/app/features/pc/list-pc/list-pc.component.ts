import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { ManageAccountService } from 'src/app/api/manage-account-service';
import { ListAllPageComponent } from 'src/app/common/list-all-page/list-all-page.component';
import { PC, UserRoles } from 'src/app/models/models';

@Component({
  selector: 'app-list-pc',
  templateUrl: 'list-pc.component.html',
  styleUrls: ['list-pc.component.css']
})
export class ListPcComponent {
  dynamicColumns = ['role', 'salary', 'persons_name', 'persons_email', 'company_name'];
  displayedColumns = ['position', 'role', 'salary', 'persons_name', 'persons_email', 'company_name', 'username', 'delete'];
  baseUrl = 'pc';
  listPageComp?: HTMLElement;
  constructor(protected apiServ: APIService, private manageAccountServ: ManageAccountService, protected router: Router) { }

  ngOnInit() {
    //Remove delete button if there is no log in or the user is only a normal one
    if (this.manageAccountServ.isLoggedOut() || this.manageAccountServ.getRole() == UserRoles.NORMAL) {
      this.displayedColumns.pop();
    }
  }
}
