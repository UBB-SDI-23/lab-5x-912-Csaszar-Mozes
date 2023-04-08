import { Component, OnInit } from '@angular/core';
import {Company} from '../../../models/models';
import { APIService } from 'src/app/api/api-service';
import { Router } from '@angular/router';
import { DeleteConfirmationComponent } from 'src/app/common/delete-confirmation/delete-confirmation.component';
import { MatTableDataSource } from '@angular/material/table';

@Component({
  selector: 'app-list-companies',
  templateUrl: './list-companies.component.html',
  styleUrls: ['./list-companies.component.css']
})
export class ListCompaniesComponent implements OnInit {
  companies: Company[] =[];
  displayedColumns: string[] = ['position','name', 'description', 'net-worth', 'reputation', 'nr-workers', 'nr-locations', 'delete'];
  dataSource: MatTableDataSource<Company> = new MatTableDataSource<Company>();
  constructor(private apiServ: APIService, private router: Router) {}
  goToDetails(id: string) {
    this.router.navigateByUrl(`companies/${id}`);
  }
  addCompany() {
    this.router.navigateByUrl('companies/add');
  }
  delete(event: MouseEvent, id: string) {
    event.stopPropagation();
    DeleteConfirmationComponent.setUpConfirmDelete('companies', Number(id));
    this.router.navigateByUrl('delete-confirmation');
  }
  sortCompaniesByReputation() {
    this.companies.sort((a, b) => {
      if(a.reputation! < b.reputation!) {
        return 1;
      }
      return -1;
    });
    this.dataSource.data = this.companies;
  }
  ngOnInit(): void {
    this.apiServ.getCompanies().subscribe((result) => {
      this.companies = result as Company[];
      this.dataSource.data = this.companies;
    })
  }
}

