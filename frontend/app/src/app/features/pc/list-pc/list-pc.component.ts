import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { ListAllPageComponent } from 'src/app/common/list-all-page/list-all-page.component';
import { PC } from 'src/app/models/models';

@Component({
  selector: 'app-list-pc',
  templateUrl: 'list-pc.component.html',
  styleUrls: ['list-pc.component.css']
})
export class ListPcComponent {
  dynamicColumns = ['role', 'salary', 'persons_name', 'persons_email', 'company_name'];
  displayedColumns = ['position', 'role', 'salary', 'persons_name', 'persons_email', 'company_name', 'delete'];
  baseUrl = 'pc';
  listPageComp?: HTMLElement;
  constructor(protected apiServ: APIService, protected router: Router) {
  }
}
