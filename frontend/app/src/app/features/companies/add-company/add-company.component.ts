import { Component } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { Company } from 'src/app/models/models';

@Component({
  selector: 'app-add-company',
  templateUrl: './add-company.component.html',
  styleUrls: ['./add-company.component.css']
})
export class AddCompanyComponent {
  nameFormControl: FormControl = new FormControl('', [Validators.required]);
  descriptionFormControl: FormControl = new FormControl('', [Validators.required]);
  netWorthFormControl: FormControl = new FormControl('', [Validators.required, Validators.pattern('^([0-9])*$')]);
  reputationFormControl: FormControl = new FormControl('', [Validators.required, Validators.pattern('^[0-9]?[0-9]$|^100$')]);
  startYearFormControl: FormControl = new FormControl('', [Validators.required, Validators.pattern('^([0-9])*$')]); 
  
  constructor(private apiServ: APIService, private router: Router) {}
  
  cancel() {
    this.router.navigateByUrl('companies');
  }
  add() {
    let data = new Company();
    data["name"] = this.nameFormControl.value;
    data["description"] = this.descriptionFormControl.value;
    data["net_value"] = this.netWorthFormControl.value;
    data["reputation"] = this.reputationFormControl.value;
    if(this.nameFormControl.valid && this.descriptionFormControl.valid && this.netWorthFormControl.valid && this.reputationFormControl.valid && this.startYearFormControl.valid) {
      this.apiServ.addCompany(data).subscribe(result => {
        alert("Updated successfully!");
      });
      
    }
    else {
      alert("Error with input data; please change data and try again!");
    }
  }
}
