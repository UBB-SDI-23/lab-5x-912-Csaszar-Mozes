import { Component } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { APIService } from 'src/app/api/api-service';
import { Company, DataGeneration } from 'src/app/models/models';

@Component({
  selector: 'app-generate-data',
  templateUrl: './generate-data.component.html',
  styleUrls: ['./generate-data.component.css']
})
export class GenerateDataComponent {
  nrPFormControl: FormControl = new FormControl(0, [Validators.required, Validators.min(10), Validators.max(100)]);
  nrCFormControl: FormControl = new FormControl(0, [Validators.required, Validators.min(10), Validators.max(100)]);
  nrPCFormControl: FormControl = new FormControl(0, [Validators.required, Validators.min(0), Validators.max(100)]);
  nrLFormControl: FormControl = new FormControl(0, [Validators.required, Validators.min(0), Validators.max(100)]);
  constructor(protected apiServ: APIService) { }

  isInputDataValid() {
    return this.nrPFormControl.valid && this.nrPCFormControl.valid && this.nrCFormControl.valid && this.nrLFormControl.valid;
  }
  generate() {
    let data = new DataGeneration();
    data["nr_p"] = Number(this.nrPFormControl.value);
    data["nr_c"] = Number(this.nrCFormControl.value);
    data["nr_pc"] = Number(this.nrPCFormControl.value);
    data["nr_l"] = Number(this.nrLFormControl.value);
    if (this.isInputDataValid()) {
      this.apiServ.generateData(data).subscribe(result => {
        alert("Generated successfully!");
      });
    }
    else {
      alert("Error with input data; please change data and try again!");
    }
  }

  changePCNr() {
    if (Number(this.nrPCFormControl.value) > Number(this.nrPFormControl.value) * Number(this.nrCFormControl.value) / 4) {
      this.nrPCFormControl.setErrors({ tooManyPC: true });
    }
  }
}
