import { Component, Inject, Input, OnChanges, SimpleChanges } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { DeleteConfirmationComponent } from '../delete-confirmation/delete-confirmation.component';


@Component({
  selector: 'app-dynamic-table',
  templateUrl: './dynamic-table.component.html',
  styleUrls: ['./dynamic-table.component.css']
})
export class DynamicTableComponent implements OnChanges {
  pageSize: number = 15;
  pageNr: number = 0;
  entities: [] = [];
  pageNrComponent?: HTMLElement;
  buttonLeft?: HTMLElement;
  buttonRight?: HTMLElement;
  dataSource: MatTableDataSource<any> = new MatTableDataSource<any>();
  @Input() baseUrl: string = '';
  @Input() apiServ?: APIService;
  @Input() router?: Router;
  @Input() displayedColumns: string[] = [];
  @Input() dynamicColumns: string[] = [];
  @Input() compareFn?: (a: never, b: never) => number;
  @Input() doSort: boolean = false;
  constructor() {
    this.displayedColumns.unshift('position');
    this.displayedColumns.push('delete');
  }
  formatColumn(name: string): string {
    return name.split('_').map((value) => value[0].toUpperCase() + value.slice(1)).join(' ');
  }
  goToDetails(id: string) {
    this.router!.navigateByUrl(`${this.baseUrl}/${id}`);
  }
  delete(event: MouseEvent, id: string) {
    event.stopPropagation();
    DeleteConfirmationComponent.setUpConfirmDelete(this.baseUrl, this.baseUrl, Number(id));
    this.router!.navigateByUrl('delete-confirmation');
  }
  refresh() {
    this.apiServ!.getEntities(this.pageNr, this.pageSize, this.baseUrl).subscribe((result) => {
      this.entities = result as [];
      this.dataSource.data = this.entities;
    })
  }
  sortByFunction() {
    if (this.compareFn != undefined) {
      this.entities.sort(this.compareFn);
    }
    else {
      this.entities.sort();
    }
    this.dataSource.data = this.entities;
  }
  ngOnChanges(changes: SimpleChanges) {
    // changes.prop contains the old and the new value...
    if (changes["doSort"]?.currentValue) {
      this.sortByFunction()
    }
  }
  incPageNr() {
    this.pageNr += 1;
    this.refresh();
  }
  decPageNr() {
    if (this.pageNr > 0) {
      this.pageNr -= 1;
      this.refresh();
    }
  }
  ngOnInit(): void {
    this.refresh();
  }
}
