import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';

@Component({
    selector: 'app-delete-confirmation',
    templateUrl: './delete-confirmation.component.html',
    styleUrls: ['./delete-confirmation.component.css']
})
export class DeleteConfirmationComponent {
    static takeBackUrl: string = '';
    static deleteID?: number;
    static baseUrl: string = '';
    constructor(private router: Router, private apiServ: APIService) { }
    static setUpConfirmDelete(takeBackUrl: string, baseUrl: string, deleteID: number) {
        this.takeBackUrl = takeBackUrl;
        this.deleteID = deleteID;
        this.baseUrl = baseUrl;
    }
    goBack() {
        this.router.navigateByUrl(DeleteConfirmationComponent.takeBackUrl);
    }
    delete() {
        this.apiServ.deleteEntity(DeleteConfirmationComponent.baseUrl, DeleteConfirmationComponent.deleteID!).subscribe(
            () => {
                this.goBack();
            }
        );
    }
}
