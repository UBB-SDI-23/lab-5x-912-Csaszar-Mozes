import { Component } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { APIService } from 'src/app/api/api-service';
import { UserProfile } from 'src/app/models/models';

@Component({
  selector: 'app-view-user-page',
  templateUrl: './view-user-page.component.html',
  styleUrls: ['./view-user-page.component.css']
})
export class ViewUserPageComponent {
  user?: UserProfile;

  baseUrl: string = 'users';

  constructor(protected apiServ: APIService, private actRoute: ActivatedRoute, protected router: Router) { }

  ngOnInit(): void {
    this.actRoute.params.subscribe(
      params => {
        this.apiServ.getEntity(this.baseUrl, params['id']).subscribe(
          result => {
            this.user = result as UserProfile;
          }
        )
      }
    );
  }
}
