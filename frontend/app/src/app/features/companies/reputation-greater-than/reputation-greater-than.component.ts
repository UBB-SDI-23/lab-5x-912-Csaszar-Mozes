import { Component } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { Params, Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';

@Component({
  selector: 'app-reputation-greater-than',
  templateUrl: './reputation-greater-than.component.html',
  styleUrls: ['./reputation-greater-than.component.css']
})
export class ReputationGreaterThanComponent {
  dynamicColumns = ['name', 'description', 'net_value', 'reputation', 'nr_workers', 'nr_locations'];
  displayedColumns = ['position', 'name', 'description', 'net_value', 'reputation', 'nr_workers', 'nr_locations'];
  baseUrl = 'companies/reputation-greater-than';
  redirectUrl = 'companies';
  reputationFormControl: FormControl = new FormControl(80, [Validators.required, Validators.pattern('^[0-9]?[0-9]$|^100$')]);
  constructor(protected apiServ: APIService, protected router: Router) {
  }
  changeReputation() {
    if (this.reputationFormControl.valid) {
      let queryParams: Params = { reputation: this.reputationFormControl.value };
      this.router!.navigate(
        [],
        {
          queryParams: queryParams,
          queryParamsHandling: 'merge',
        });
    }
  }
}
