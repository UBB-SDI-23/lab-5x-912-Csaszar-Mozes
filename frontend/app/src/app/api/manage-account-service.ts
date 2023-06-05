import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { Company, CompanyDetail, RegisterUser, UserProfile, UserRoles } from "../models/models";
import { ActivatedRoute } from "@angular/router";
import { APIService } from "./api-service";

const TOKEN_KEY = 'auth_token';
const USER_KEY = 'auth_user';
const ROLE_KEY = 'auth_role';
const NICKNAME_KEY = 'nickname';

@Injectable({
  providedIn: 'root'
})
export class ManageAccountService {

  constructor(private http: HttpClient) { }

  registerUser(user: RegisterUser): Observable<Object> {
    return this.http.post(APIService.url + 'register/', user);
  }

  confirmRegistration(token: string): Observable<Object> {
    return this.http.post(APIService.url + `register/confirm/${token}` + '?username=' + this.getUser(), {});
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
    this.removeToken();
    this.removeUser();
  }

  isLoggedIn() {
    return window.localStorage.getItem(TOKEN_KEY) != undefined;
  }

  isLoggedOut() {
    return window.localStorage.getItem(TOKEN_KEY) == undefined;
  }

  isLoggedInAsModerator() {
    return this.isLoggedIn() && this.getRole() == UserRoles.MODERATOR;
  }

  isLoggedInAsAdmin() {
    return this.isLoggedIn() && this.getRole() == UserRoles.ADMIN;
  }

  isLoggedInAndOwnsObject(obj_user_username: string) {
    return this.isLoggedIn() && this.getUser() == obj_user_username;
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
    return username == undefined ? '' : username;
  }

  saveRole(role: string) {
    window.localStorage.removeItem(ROLE_KEY);
    window.localStorage.setItem(ROLE_KEY, role);
  }

  removeRole() {
    window.localStorage.removeItem(ROLE_KEY);
  }

  getRole(): string {
    const role = window.localStorage.getItem(ROLE_KEY)
    return role == undefined ? '' : role;
  }

  saveNickname(nickname: string) {
    window.localStorage.removeItem(NICKNAME_KEY);
    window.localStorage.setItem(NICKNAME_KEY, nickname);
  }

  removeNickname() {
    window.localStorage.removeItem(NICKNAME_KEY);
  }

  getNickname(): string {
    const nickname = window.localStorage.getItem(NICKNAME_KEY);
    return nickname == undefined ? (this.isLoggedIn() ? this.getUser() : 'Guest') : nickname;
  }
}