import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { ListAllPageComponent } from 'src/app/common/list-all-page/list-all-page.component';
import { Person } from 'src/app/models/models';

@Component({
  selector: 'app-list-people',
  templateUrl: 'list-people.component.html',
  styleUrls: ['list-people.component.css']
})
export class ListPeopleComponent {
  dynamicColumns = ['first_name', 'last_name', 'email', 'age', 'worker_id'];
  displayedColumns = ['first_name', 'last_name', 'email', 'age', 'worker_id'];
  baseUrl = 'people';
  listPageComp?: HTMLElement;
  constructor(protected apiServ: APIService, protected router: Router) {
    this.listPageComp = document.querySelector('app-list-all-page') as HTMLElement;
    console.log(this.listPageComp);
  }

}
