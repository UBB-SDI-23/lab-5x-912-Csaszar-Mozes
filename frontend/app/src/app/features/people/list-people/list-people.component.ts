import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';

@Component({
  selector: 'app-list-people',
  templateUrl: 'list-people.component.html',
  styleUrls: ['list-people.component.css']
})
export class ListPeopleComponent {
  dynamicColumns = ['first_name', 'last_name', 'email', 'age', 'worker_id', 'nr_workplaces'];
  displayedColumns = ['position', 'first_name', 'last_name', 'email', 'age', 'worker_id', 'nr_workplaces', 'delete'];
  baseUrl = 'people';
  listPageComp?: HTMLElement;
  constructor(protected apiServ: APIService, protected router: Router) { }
}
