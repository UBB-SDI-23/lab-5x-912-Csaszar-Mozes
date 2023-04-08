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

    constructor(private http: HttpClient) {}

    getCompanies(page_nr: number, page_size: number) {
        if(page_nr >= 0 && page_size >= 1) {
            return this.http.get(APIService.url + 'companies/page-' + page_nr + ',size-' + page_size);
        }
        else {
            throw "Page number and Page size should be positive integers!";
        }
    }
    getCompaniesByAvgSalary(page_nr: number, page_size: number) {
        if(page_nr >= 0 && page_size >= 1) {
            return this.http.get(APIService.url + 'companies/avg-salary/page-' + page_nr + ',size-' + page_size);
        }
        else {
            throw "Page number and Page size should be positive integers!";
        }
        
    }
    getCompany(id: number): Observable<CompanyDetail> {
        return this.http.get(APIService.url + 'companies/' + id + '/') as Observable<CompanyDetail>;
    }
    putCompany(id: number, data: Company) {
        return this.http.put(APIService.url + 'companies/' + id + '/', data);
    }
    deleteCompany(id: number) {
        return this.http.delete(APIService.url + 'companies/' + id + '/');
    }
    addCompany(data: Company) {
        return this.http.post(APIService.url + 'companies/', data);
    }
}