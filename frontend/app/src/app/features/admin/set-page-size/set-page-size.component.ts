import { Component } from '@angular/core';
import { FormControl, Validators } from '@angular/forms';
import { APIService } from 'src/app/api/api-service';
import { ManageAccountService } from 'src/app/api/manage-account-service';
import { IntegerSetting } from 'src/app/models/models';

@Component({
  selector: 'app-set-page-size',
  templateUrl: './set-page-size.component.html',
  styleUrls: ['./set-page-size.component.css']
})
export class SetPageSizeComponent {
  pageSizeFormControl: FormControl = new FormControl(15, [Validators.required, Validators.min(15), Validators.max(200)]);

  constructor(protected manageAccountServ: ManageAccountService, protected apiServ: APIService) { }


  isInputDataValid(): boolean {
    return this.pageSizeFormControl.valid;
  }

  edit() {
    let data = new IntegerSetting();
    data["value"] = Number(this.pageSizeFormControl.value);
    data["name"] = 'page_size';
    data["user_role"] = Number(this.manageAccountServ.getRole());
    if (this.isInputDataValid()) {
      this.apiServ.setSetting(data).subscribe(result => {
        alert("Setting updated successfully!");
      });
    }
    else {
      alert("Error with input data; please change data and try again!");
    }
  }

}
