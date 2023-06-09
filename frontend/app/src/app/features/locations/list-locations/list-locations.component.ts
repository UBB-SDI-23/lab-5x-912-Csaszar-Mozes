import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { ListAllPageComponent } from 'src/app/common/list-all-page/list-all-page.component';

@Component({
  selector: 'app-list-locations',
  templateUrl: 'list-locations.component.html',
  styleUrls: ['list-locations.component.css']
})
export class ListLocationsComponent {
  dynamicColumns = ['country', 'city', 'street', 'number', 'apartment', 'description'];
  displayedColumns = ['position', 'country', 'city', 'street', 'number', 'apartment', 'description', 'delete'];
  baseUrl = 'locations';
  constructor(protected apiServ: APIService, protected router: Router) { }
}
