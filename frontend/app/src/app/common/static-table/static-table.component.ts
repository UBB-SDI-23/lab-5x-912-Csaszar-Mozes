import { Component, Input, OnChanges, SimpleChanges } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { Router } from '@angular/router';

@Component({
  selector: 'app-static-table',
  templateUrl: './static-table.component.html',
  styleUrls: ['./static-table.component.css']
})
export class StaticTableComponent implements OnChanges {
  @Input() dynamicColumns: string[] = [];
  @Input() displayedColumns: string[] = [];
  @Input() baseUrl = '';
  @Input() router?: Router;
  @Input() entities: any[] = [];
  @Input() pageSize: number = 10;
  @Input() id: number = 0;

  dataSource: MatTableDataSource<any> = new MatTableDataSource();


  pageNr: number = 0;

  constructor() {
    this.displayedColumns.unshift('position');
  }
  ngOnChanges(changes: SimpleChanges) {
    // changes.prop contains the old and the new value...
    if (changes["entities"]?.currentValue) {
      this.refresh();
    }
  }
  refresh() {
    this.dataSource.data = this.entities.slice(this.pageNr * this.pageSize, this.pageNr * this.pageSize + this.pageSize);
  }
  incPageNr() {
    if ((this.pageNr + 1) * this.pageSize < this.entities.length) {
      this.pageNr += 1;
      this.refresh();
    }
  }
  decPageNr() {
    if (this.pageNr > 0) {
      this.pageNr -= 1;
      this.refresh();
    }
  }
  formatColumn(name: string): string {
    return name.split('.')[name.split('.').length - 1]?.split('_').map((value) => value[0].toUpperCase() + value.slice(1)).join(' ');
  }
  goToDetails(id: string) {
    this.router!.navigateByUrl(`${this.baseUrl}/${id}`);
  }
  getColumnValue(base: any, col: string): string {
    for (let c of col.split('.')) {
      base = base[c];
    }
    return base + '';
  }

}
