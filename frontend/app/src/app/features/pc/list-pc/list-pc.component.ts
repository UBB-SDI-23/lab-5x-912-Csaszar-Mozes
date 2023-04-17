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
  dynamicColumns = ['role', 'salary', 'person', 'company'];
  displayedColumns = ['role', 'salary', 'person', 'company'];
  baseUrl = 'pc';
  listPageComp?: HTMLElement;
  constructor(protected apiServ: APIService, protected router: Router) {
    this.listPageComp = document.querySelector('app-list-all-page') as HTMLElement;
    console.log(this.listPageComp);
  }
}
