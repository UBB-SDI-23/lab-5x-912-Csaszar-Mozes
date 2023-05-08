import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { ManageAccountService } from 'src/app/api/manage-account-service';
import { ListAllPageComponent } from 'src/app/common/list-all-page/list-all-page.component';
import { UserRoles } from 'src/app/models/models';

@Component({
  selector: 'app-list-locations',
  templateUrl: 'list-locations.component.html',
  styleUrls: ['list-locations.component.css']
})
export class ListLocationsComponent {
  dynamicColumns = ['country', 'city', 'street', 'number', 'apartment', 'description'];
  displayedColumns = ['position', 'country', 'city', 'street', 'number', 'apartment', 'description', 'username', 'delete'];
  baseUrl = 'locations';
  constructor(protected apiServ: APIService, private manageAccountServ: ManageAccountService, protected router: Router) { }

  ngOnInit() {
    //Remove delete button if there is no log in or the user is only a normal one
    if (this.manageAccountServ.isLoggedOut() || this.manageAccountServ.getRole() == UserRoles.NORMAL) {
      this.displayedColumns.pop();
    }
  }
}
