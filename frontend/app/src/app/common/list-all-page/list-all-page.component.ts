import { Component, Inject, Input } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { DeleteConfirmationComponent } from '../delete-confirmation/delete-confirmation.component';

@Component({
  selector: 'app-list-all-page',
  templateUrl: './list-all-page.component.html',
  styleUrls: ['./list-all-page.component.css']
})
export class ListAllPageComponent {
  dataSource: MatTableDataSource<any> = new MatTableDataSource<any>();
  @Input() baseUrl: string = '';
  @Input() apiServ?: APIService;
  @Input() router?: Router;
  @Input() displayedColumns: string[] = [];
  @Input() dynamicColumns: string[] = [];
  @Input() compareFn?: (a: any, b: any) => number;
  @Input() doSort: boolean = false;
  constructor() {
  }
  formatColumn(name: string): string {
    return name.split('_').map((value) => value[0].toUpperCase() + value.slice(1)).join(' ');
  }
  addEntity() {
    this.router!.navigateByUrl(`${this.baseUrl}/add`);
  }
  setCompareFn(fn: (a: any, b: any) => number) {
    this.compareFn = fn;
  }
}
