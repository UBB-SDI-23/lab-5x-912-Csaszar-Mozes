import { Injectable } from "@angular/core";
import { CanActivate, Router } from "@angular/router";
import { ManageAccountService } from "src/app/api/manage-account-service";

@Injectable()
export class AuthGuard implements CanActivate {

  constructor(private authService: ManageAccountService, private router: Router) { }

  canActivate() {
    if (this.authService.isLoggedIn()) {
      return true;
    } else {
      this.authService.logOut();
      this.router.navigate(['login']);

      return false;
    }
  }
}

interface JWTPayload {
  user_id: number;
  username: string;
  email: string;
  exp: number;
}