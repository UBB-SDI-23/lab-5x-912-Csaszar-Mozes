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
    this.saveUser(user.username!);
    return this.http.post(APIService.url + 'register/', user);
  }

  confirmRegistration(token: string): Observable<Object> {
    return this.http.post(APIService.url + `register/confirm/${token}` + '?username=' + this.getUser(), {});
  }

  logIn(username: string, password: string) {
    this.saveUser(username);
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
    this.removeToken();
    this.removeUser();
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

  removeToken() {
    window.localStorage.removeItem(TOKEN_KEY);
  }

  getToken() {
    return window.localStorage.getItem(TOKEN_KEY);
  }

  saveUser(username: string) {
    window.localStorage.removeItem(USER_KEY);
    window.localStorage.setItem(USER_KEY, username);
  }

  removeUser() {
    window.localStorage.removeItem(USER_KEY);
  }

  getUser(): string {
    const username = window.localStorage.getItem(USER_KEY);
    if (username) {
      return username;
    }
    return '';
  }
}