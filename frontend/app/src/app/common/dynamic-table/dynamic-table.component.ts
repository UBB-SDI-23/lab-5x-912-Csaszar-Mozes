import { Component, Inject, Input, OnChanges, SimpleChanges } from '@angular/core';
import { MatTableDataSource } from '@angular/material/table';
import { ActivatedRoute, Params, Route, Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { DeleteConfirmationComponent } from '../delete-confirmation/delete-confirmation.component';
import { Message, NrTotalPages } from 'src/app/models/models';
import { ManageAccountService } from 'src/app/api/manage-account-service';

class PaginationButtonNumbersHolder {
  before_the_dots: number[] = [];
  before: number[] = [];
  actual: number = 0;
  after: number[] = [];
  after_the_dots: number[] = [];
  displayBeforeDots: boolean = false;
  displayAfterDots: boolean = false;

  private totalPageNr: number = 0;
  nrResults: number = 0;

  constructor() { }

  setPage(pageNr: number) {
    pageNr++;
    this.before_the_dots = [];
    this.before = [];
    this.after = [];
    this.after_the_dots = [];
    for (let i = 1; i < 6 && i < pageNr; i++) {
      this.before_the_dots.push(i);
    }
    for (let i = pageNr - 1; i > 5 && i > pageNr - 1 - 5; i--) {
      this.before.unshift(i);
    }
    for (let i = pageNr + 1; i < pageNr + 1 + 5 && i < this.totalPageNr - 5; i++) {
      this.after.push(i);
    }
    for (let i = this.totalPageNr; i > this.totalPageNr - 5 && i > pageNr; i--) {
      this.after_the_dots.unshift(i);
    }
    this.actual = pageNr;
    this.displayBeforeDots = this.hasBeforeDots();
    this.displayAfterDots = this.hasAfterDots();
  }

  setTotalPageNr(totalPageNr: number) {
    this.totalPageNr = totalPageNr;
  }
  setNrResults(nrResults: number) {
    this.nrResults = nrResults;
  }

  hasBeforeTheDots(): boolean {
    return this.before_the_dots.length > 0;
  }
  hasBeforeDots(): boolean {
    return this.before.length == 5 && this.before_the_dots[4] + 1 < this.before[0];
  }
  hasBefore(): boolean {
    return this.before.length > 0;
  }
  hasAfter(): boolean {
    return this.after.length > 0;
  }
  hasAfterDots(): boolean {
    return this.after.length == 5 && this.after[4] + 1 < this.after_the_dots[0];
  }
  hasAfterTheDots(): boolean {
    return this.after_the_dots.length > 0;
  }
}

@Component({
  selector: 'app-dynamic-table',
  templateUrl: './dynamic-table.component.html',
  styleUrls: ['./dynamic-table.component.css']
})
export class DynamicTableComponent implements OnChanges {
  pageSize: number = 15;
  pageNr: number = 0;
  entities: any[] = [];
  paginationNrs: PaginationButtonNumbersHolder = new PaginationButtonNumbersHolder();
  dataSource: MatTableDataSource<any> = new MatTableDataSource<any>();
  checkBoxes: boolean[] = [];

  @Input() baseUrl: string = '';
  @Input() redirectUrl: string = '';
  @Input() apiServ?: APIService;
  @Input() router?: Router;
  @Input() displayedColumns: string[] = [];
  @Input() dynamicColumns: string[] = [];
  @Input() compareFn?: (a: any, b: any) => number;
  @Input() doSort: boolean = false;

  constructor(private route: ActivatedRoute, protected manageAccountServ: ManageAccountService) {
    for (let i = 0; i < this.pageSize; i++) {
      this.checkBoxes.push(false);
    }
  }
  formatColumn(name: string): string {
    return name.split('.').pop()!.split('_').map((value) => value[0].toUpperCase() + value.slice(1)).join(' ');
  }
  getColumnValue(base: any, col: string): string {
    for (let c of col.split('.')) {
      base = base[c];
    }
    return base + '';
  }
  goToDetails(id: string) {
    if (this.redirectUrl == '') {
      this.router!.navigateByUrl(`${this.baseUrl}/${id}`);
    }
    else {
      this.router!.navigateByUrl(`${this.redirectUrl}/${id}`);
    }
  }
  delete(event: MouseEvent, id: string) {
    event.stopPropagation();
    DeleteConfirmationComponent.setUpConfirmDelete(this.baseUrl, this.baseUrl, Number(id));
    this.router!.navigateByUrl('delete-confirmation');
  }
  deleteSelected() {
    if (confirm("Are you sure?")) {
      let nr_to_delete = this.nrBoxesChecked();
      let nr_deleted = 0;
      this.checkBoxes.forEach((v, i) => {
        if (v) {
          this.checkBoxes[i] = false;
          this.apiServ?.deleteEntity(this.baseUrl, this.entities[i].id).subscribe(
            (res) => {
              nr_deleted++;
              if (nr_deleted == nr_to_delete) {
                alert("Succesfully deleted all");
                this.refresh();
              }
            }
          );
        }
      });
    }
  }
  flipCheckbox(event: MouseEvent, i: number) {
    event.stopPropagation();
    this.checkBoxes[i] = !this.checkBoxes[i];
  }
  nrBoxesChecked() {
    return this.checkBoxes.reduce((p, c) => p + Number(c), 0);
  }
  refresh() {
    this.apiServ?.getNrTotalPages(this.baseUrl, this.pageSize).subscribe((result) => {
      let res = result as NrTotalPages;
      if (res.nr_total_pages! < this.pageNr) {
        this.pageNr = res.nr_total_pages! - 1;
      }
      this.paginationNrs.setTotalPageNr(res.nr_total_pages!);
      this.paginationNrs.setNrResults(res.nr_results!);
      this.paginationNrs.setPage(this.pageNr);

      let queryParams: Params = { pageNr: this.pageNr, pageSize: this.pageSize };
      this.router!.navigate(
        [],
        {
          queryParams: queryParams,
          queryParamsHandling: 'merge',
        });
      this.apiServ!.getEntities(this.pageNr, this.pageSize, this.baseUrl).subscribe((result) => {
        this.entities = result as Array<any>;
        this.dataSource.data = this.entities;
        console.log(this.entities);
      });
    });

  }
  isRoleChecked(i: number, nr: number) {
    return this.entities[i].role == nr;
  }
  changeRoleTo(event: MouseEvent, i: number, role: number) {
    event.stopPropagation();
    //if the user doesn't select current role
    if (!this.isRoleChecked(i, role)) {
      if (confirm("Are you sure?")) {
        this.apiServ!.changeUserRole(this.entities[i].user.id, role).subscribe(
          (result) => {
            let res = result as Message;
            alert(res.message);
            this.entities[i].role = role;
          }
        );
      }
    }
  }
  isSameUserAsLoggedIn(i: number) {
    return this.manageAccountServ.getUser() == this.entities[i].user.username
  }
  goToUser(userNr: number) {
    this.router!.navigateByUrl('users/' + userNr);
  }
  goToPage(pageNr: number) {
    //unshift page numbers
    pageNr--;
    this.pageNr = pageNr;
    this.refresh();
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
  ngOnInit(): void {
    this.route.queryParams.subscribe((params) => {
      this.pageNr = params["pageNr"] == undefined ? 0 : Number(params["pageNr"]);
      this.pageSize = params["pageSize"] == undefined ? 15 : Number(params["pageSize"]);

      this.refresh();
    });

  }
}
