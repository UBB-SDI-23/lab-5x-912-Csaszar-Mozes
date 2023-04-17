import { Component } from '@angular/core';
import { Company } from '../../../models/models';
import { APIService } from 'src/app/api/api-service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-list-companies',
  templateUrl: 'list-companies.component.html',
  styleUrls: ['list-companies.component.css']
})
export class ListCompaniesComponent {
  dynamicColumns = ['name', 'description', 'net-worth', 'reputation', 'nr-workers', 'nr-locations'];
  displayedColumns = ['name', 'description', 'net-worth', 'reputation', 'nr-workers', 'nr-locations'];
  baseUrl = 'companies';
  listPageComp?: HTMLElement;
  doSort: boolean = false;
  compareFn?: (a: never, b: never) => number;
  constructor(protected apiServ: APIService, protected router: Router) {
    this.listPageComp = document.querySelector('app-list-all-page') as HTMLElement;
    console.log(this.listPageComp);
  }
  sortCompaniesByReputation() {
    //Change comparte function to be appropriate
    this.compareFn = (a, b) => {
      let dc_a = a as Company; let dc_b = b as Company;
      return dc_a.reputation == dc_b.reputation ? 0 : (dc_a.reputation! < dc_b.reputation! ? 1 : -1);
    };
    //Start sort by changing this value
    this.doSort = true;
    //Reset value for next sort
    setTimeout(
      () => { this.doSort = false; }, 100
    );
  }
}

