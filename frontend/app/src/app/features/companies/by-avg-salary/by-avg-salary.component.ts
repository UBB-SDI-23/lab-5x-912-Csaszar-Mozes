import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';

@Component({
  selector: 'app-by-avg-salary',
  templateUrl: 'by-avg-salary.component.html',
  styleUrls: ['by-avg-salary.component.css']
})
export class ByAvgSalaryComponent {
  dynamicColumns = ['name', 'description', 'net_value', 'reputation', 'people_working_here', 'avg_salary'];
  displayedColumns = ['position', 'name', 'description', 'net_value', 'reputation', 'people_working_here', 'avg_salary'];
  baseUrl = 'companies/by-avg-salary';
  constructor(protected apiServ: APIService, protected router: Router) {
  }
}
