import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { Company, CompanyDetail } from "../models/models";

@Injectable({
    providedIn: 'root'
})
export class APIService {
    //static url: string = 'https://mozes-csaszar-sdi-922.strangled.net/';
    static url: string = 'http://127.0.0.1:8000/api/';
    //static url: string = '/api/';

    constructor(private http: HttpClient) { }
    getEntities(page_nr: number, page_size: number, base_url: string) {
        if (page_nr >= 0 && page_size >= 1) {
            return this.http.get(APIService.url + base_url + '/?page=' + page_nr + '&size=' + page_size);
        }
        else {
            throw "Page number and Page size should be positive integers!";
        }
    }
    getAutocompleteEntity(base_url: string, name: string, size: number) {
        if (size >= 1) {
            return this.http.get(APIService.url + base_url + `/name-autocomplete/?name=${name}&size=${size}`);
        }
        else {
            throw "Page size should be a positive integer!";
        }
    }
    getEntity(base_url: string, id: number): Observable<Object> {
        return this.http.get(APIService.url + base_url + '/' + id + '/') as Observable<CompanyDetail>;
    }
    putEntity(base_url: string, id: number, data: Object) {
        return this.http.put(APIService.url + base_url + '/' + id + '/', data);
    }
    deleteEntity(base_url: string, id: number) {
        return this.http.delete(APIService.url + base_url + '/' + id + '/');
    }
    addEntity(base_url: string, data: any) {
        return this.http.post(APIService.url + base_url + "/", data);
    }
}