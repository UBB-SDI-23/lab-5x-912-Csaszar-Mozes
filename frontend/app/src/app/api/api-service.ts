import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Observable } from "rxjs";
import { Company, CompanyDetail, DataGeneration, IntegerSetting } from "../models/models";
import { ActivatedRoute } from "@angular/router";
import { ManageAccountService } from "./manage-account-service";
import { SetPageSizeComponent } from "../features/admin/set-page-size/set-page-size.component";

@Injectable({
    providedIn: 'root'
})
export class APIService {
    static url: string = 'https://mozes-csaszar-sdi-922.strangled.net/api/';
    //static url: string = 'http://127.0.0.1:8000/api/';

    static webSocketUrl(): string {
        return (this.url.includes('127.0.0.1') ? 'ws://' : "wss://") + this.url.split('/')[2];
    }


    private addSearcParamsToUrl(url: string, exclude: string[] = ['pageSize', 'pageNr']): string {
        url += '/?';
        this.route.queryParams.subscribe(
            (res) => {
                for (let key in res) {
                    if (!exclude.includes(key)) {
                        url += key + "=" + res[key] + "&";
                    }
                }
            }
        );
        return url;
    }

    constructor(private http: HttpClient, private route: ActivatedRoute, private manageAccountServ: ManageAccountService) { }
    getSuggestion(data: string) {
        return this.http.post(APIService.url + "predict-next-word/", { "data": data })
    }
    generateData(data: DataGeneration) {
        return this.http.post(APIService.url + "admin/generate-data/", data);
    }
    changeUserRole(user_id: number, role: number) {
        let data = { user_id: user_id, role: role };
        return this.http.put(APIService.url + 'users/edit-role/', data);
    }
    getEntities(page_nr: number, page_size: number, base_url: string) {
        if (page_nr >= 0 && page_size >= 1) {
            let comp_url = APIService.url + base_url;
            comp_url = this.addSearcParamsToUrl(comp_url);
            comp_url += 'page=' + page_nr + "&" + 'size=' + page_size;
            return this.http.get(comp_url);
        }
        else {
            throw "Page number and Page size should be positive integers!";
        }
    }
    getMessages(page_size: number) {
        return this.http.get(APIService.url + 'messages/?size=' + page_size);
    }
    addMessage(data: any) {
        return this.http.post(APIService.url + 'messages/', data);
    }
    setSetting(data: IntegerSetting) {
        return this.http.post(APIService.url + "admin/set-setting/", data);
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
    getNrTotalPages(url: string, page_size: number) {
        let comp_url = APIService.url + 'nr-total-pages';
        comp_url = this.addSearcParamsToUrl(comp_url);
        comp_url += 'url=' + url + "&size=" + page_size;
        return this.http.get(comp_url);
    }
    getPageSize() {
        return this.http.get(APIService.url + 'page-size');
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