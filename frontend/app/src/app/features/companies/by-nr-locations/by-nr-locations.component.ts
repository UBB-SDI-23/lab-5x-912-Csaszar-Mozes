import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';

@Component({
  selector: 'app-by-nr-locations',
  templateUrl: './by-nr-locations.component.html',
  styleUrls: ['./by-nr-locations.component.css']
})
export class ByNrLocationsComponent {
  dynamicColumns = ['name', 'description', 'net_value', 'reputation', 'nr_locations'];
  displayedColumns = ['position', 'name', 'description', 'net_value', 'reputation', 'nr_locations', 'username'];
  baseUrl = 'companies/by-nr-locations';
  redirectUrl = 'companies';
  constructor(protected apiServ: APIService, protected router: Router) {
  }
}
