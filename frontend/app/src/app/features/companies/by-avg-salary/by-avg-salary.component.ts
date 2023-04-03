import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { Company } from 'src/app/models/models';

@Component({
  selector: 'app-by-avg-salary',
  templateUrl: './by-avg-salary.component.html',
  styleUrls: ['./by-avg-salary.component.css']
})
export class ByAvgSalaryComponent {
  companies: Company[] =[];
  displayedColumns: string[] = ['position','name', 'description', 'net-worth', 'reputation', 'avg-salary'];
  constructor(private apiServ: APIService, private router: Router) {}
  goToDetails(id: string) {
    this.router.navigateByUrl(`companies/${id}`);
  }
  ngOnInit(): void {
    this.apiServ.getCompaniesByAvgSalary().subscribe((result) => {
      this.companies = result as Company[];
    })
  }
}
