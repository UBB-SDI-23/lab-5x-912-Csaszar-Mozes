import { Component } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { Company } from 'src/app/models/models';

@Component({
  selector: 'app-by-avg-salary',
  templateUrl: './by-avg-salary.component.html',
  styleUrls: ['./by-avg-salary.component.css']
})
export class ByAvgSalaryComponent {
  pageSize: number = 15;
  pageNr: number = 0;
  companies: Company[] =[];
  dataSource: MatTableDataSource<Company> = new MatTableDataSource<Company>();
  displayedColumns: string[] = ['position','name', 'description', 'net-worth', 'reputation', 'avg-salary'];
  pageNrComponent?: HTMLElement;
  buttonLeft?: HTMLElement;
  buttonRight?: HTMLElement;
  constructor(private apiServ: APIService, private router: Router) {}
  goToDetails(id: string) {
    this.router.navigateByUrl(`companies/${id}`);
  }
  refresh() {
    this.apiServ.getCompaniesByAvgSalary(this.pageNr, this.pageSize).subscribe((result) => {
      this.companies = result as Company[];
      this.dataSource.data = this.companies;
      this.pageNrComponent!.innerHTML = this.pageNr + '';
    })
  }
  incPageNr() {
    this.pageNr += 1;
    this.refresh();
  }
  decPageNr() {
    if(this.pageNr > 0) {
      this.pageNr -= 1;
      this.refresh();
    }
  }
  ngOnInit(): void {
    this.refresh();
    this.buttonLeft = document.getElementById("ButtonLeft") as HTMLElement;
    this.buttonRight = document.getElementById("ButtonRight") as HTMLElement;
    this.pageNrComponent = document.getElementById("PageNr") as HTMLElement;
  }
}
