import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { Company, CompanyDetail, RegisterUser } from "../models/models";
import { ActivatedRoute } from "@angular/router";
import { APIService } from "./api-service";

@Injectable({
  providedIn: 'root'
})
export class ManageAccountService {

  constructor(private http: HttpClient) { }

  registerUser(user: RegisterUser): Observable<Object> {
    return this.http.post(APIService.url + 'register/', user);
  }

  confirmRegistration(token: string): Observable<Object> {
    console.log(token);
    return this.http.post(APIService.url + `register/confirm/${token}`, {});
  }
}