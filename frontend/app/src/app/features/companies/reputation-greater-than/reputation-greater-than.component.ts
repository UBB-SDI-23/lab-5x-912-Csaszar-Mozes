import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';

@Component({
  selector: 'app-reputation-greater-than',
  templateUrl: './reputation-greater-than.component.html',
  styleUrls: ['./reputation-greater-than.component.css']
})
export class ReputationGreaterThanComponent {
  dynamicColumns = ['name', 'description', 'net_value', 'reputation', 'nr_workers', 'nr_locations'];
  displayedColumns = ['position', 'name', 'description', 'net_value', 'reputation', 'nr_workers', 'nr_locations'];
  baseUrl = 'companies/by-nr-locations';
  constructor(protected apiServ: APIService, protected router: Router) {
  }
}
