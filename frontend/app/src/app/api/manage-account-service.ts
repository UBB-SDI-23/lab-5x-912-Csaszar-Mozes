import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { Company, CompanyDetail, RegisterUser, UserProfile } from "../models/models";
import { ActivatedRoute } from "@angular/router";
import { APIService } from "./api-service";

const TOKEN_KEY = 'auth_token';
const USER_KEY = 'auth_user';

@Injectable({
  providedIn: 'root'
})
export class ManageAccountService {

  constructor(private http: HttpClient) { }

  registerUser(user: RegisterUser): Observable<Object> {
    return this.http.post(APIService.url + 'register/', user);
  }

  confirmRegistration(token: string): Observable<Object> {
    return this.http.post(APIService.url + `register/confirm/${token}`, {});
  }

  logIn(username: string, password: string) {
    return this.http.post(APIService.url + 'token/', { username: username, password: password });
  }

  getProfile() {
    return this.http.get(APIService.url + "users/profile/");
  }
  updateProfile(userProfile: UserProfile) {
    return this.http.put(APIService.url + "users/profile/", userProfile);
  }
  resetProfile() {
    return this.http.delete(APIService.url + "users/profile");
  }

  logOut() {
    window.localStorage.removeItem(TOKEN_KEY);
  }

  isLoggedIn() {
    return window.localStorage.getItem(TOKEN_KEY) != undefined;
  }

  isLoggedOut() {
    return window.localStorage.getItem(TOKEN_KEY) == undefined;
  }

  saveToken(token: string) {
    window.localStorage.removeItem(TOKEN_KEY);
    window.localStorage.setItem(TOKEN_KEY, token);
  }

  getToken() {
    return window.localStorage.getItem(TOKEN_KEY);
  }

  saveUser(user: any) {
    window.localStorage.removeItem(USER_KEY);
    window.localStorage.setItem(USER_KEY, JSON.stringify(user));
  }

  getUser(): any {
    const user = window.sessionStorage.getItem(USER_KEY);
    if (user) {
      return JSON.parse(user);
    }
    return {};
  }
}