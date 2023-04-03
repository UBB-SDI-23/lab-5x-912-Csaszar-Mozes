import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { Company, CompanyDetail } from "../models/models";

@Injectable({
    providedIn: 'root'
})
export class APIService {
    static url: string = 'http://ec2-13-49-134-0.eu-north-1.compute.amazonaws.com/';

    constructor(private http: HttpClient) {}

    getCompanies() {
        return this.http.get(APIService.url + 'companies/');
    }
    getCompaniesByAvgSalary() {
        return this.http.get(APIService.url + 'companies/avg-salary/');
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