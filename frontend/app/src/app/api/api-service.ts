import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { Company, CompanyDetail } from "../models/models";

@Injectable({
    providedIn: 'root'
})
export class APIService {
    //static url: string = 'http://ec2-13-49-134-0.eu-north-1.compute.amazonaws.com/api/';
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
    getAutocompleteCompany(name: string, size: number) {
        if (size >= 1) {
            return this.http.get(APIService.url + `companies/name-autocomplete/?name=${name}&size=${size}`);
        }
        else {
            throw "Page size should be a positive integer!";
        }
    }
    getCompany(id: number): Observable<CompanyDetail> {
        return this.http.get(APIService.url + 'companies/' + id + '/') as Observable<CompanyDetail>;
    }
    putCompany(id: number, data: Company) {
        return this.http.put(APIService.url + 'companies/' + id + '/', data);
    }
    deleteEntity(base_url: string, id: number) {
        return this.http.delete(APIService.url + base_url + '/' + id + '/');
    }
    addEntity(base_url: string, data: any) {
        return this.http.post(APIService.url + base_url + "/", data);
    }
}