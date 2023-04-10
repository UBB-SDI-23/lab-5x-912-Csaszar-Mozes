import { Observable, lastValueFrom } from "rxjs";
import { APIService } from "../api/api-service";
import { Company } from "../models/models";

class PageCacheCompany {
    static Empty = new PageCacheCompany([]);
    data: Company[];
    startPageNr: number;
    pageSize: number;
    constructor(data: Company[], startPageNr: number = 0, pageSize: number = 15) {
        this.data = data;
        this.startPageNr = startPageNr;
        this.pageSize = pageSize;
    }
    getPage(pageNr: number): Company[] {
        let internalPageNr: number = pageNr - this.startPageNr;
        return this.data.slice(internalPageNr * this.pageSize, (internalPageNr + 1) * this.pageSize);
    }
    hasPage(pageNr: number): boolean {
        return (pageNr - this.startPageNr < 0) || this.data.length < (pageNr - this.startPageNr) * this.pageSize;
    }
    isEmpty(): boolean {
        return this.data.length == 0;
    }
}

export class PageingCompany {
    pageSize: number;
    currPage: number = 0;
    nrCachedPages: number;
    data: PageCacheCompany[] = [];
    lastPromise?: Promise<void>;
    promisePage?: number;
    finishedSetUp: boolean = false;
    constructor(private apiServ: APIService, pageSize:number = 15, nrCachedPages: number = 20) {
        this.pageSize = pageSize;
        this.nrCachedPages = nrCachedPages;
        this.setUp();
        
    }
    async setUp() {
        await lastValueFrom(
            this.apiServ.getCompanies(0, this.pageSize * this.nrCachedPages * 2)
        ).then(
        result => {
            console.log("FINISED", result)
            this.data.push(PageCacheCompany.Empty);
            let resComp = result as Company[];
            this.data.push(new PageCacheCompany(resComp.slice(0, this.pageSize * this.nrCachedPages), 0, this.pageSize));
            this.data.push(new PageCacheCompany(resComp.slice(this.pageSize * this.nrCachedPages, this.pageSize * this.nrCachedPages * 2), this.nrCachedPages, this.pageSize));
        });
        this.finishedSetUp = true;
    }
    awaitLast() {
        if(this.lastPromise != undefined) {
            this.lastPromise.then();
        }
    }
    async fetchPageIntoPos(pos: number): Promise<void> {
        this.apiServ.getCompanies(Math.floor(this.promisePage! / this.nrCachedPages), this.pageSize * this.nrCachedPages).subscribe((result) => {
            this.data[pos] = new PageCacheCompany(result as Company[], this.promisePage, this.pageSize);
        });
    }
    nextPage(): void {
        this.currPage ++;
        //if it doesn't have enough data
        if(!this.data[1].hasPage(this.currPage)) {
            this.awaitLast();
            this.promisePage = this.currPage;
            this.data[0] = this.data[1];
            this.data[1] = this.data[2];
            this.lastPromise = this.fetchPageIntoPos(2);            
        }
    }
    prevPage(): void {
        this.currPage--;
        if(this.currPage != 0) {
            if(this.currPage < 0) {
                this.awaitLast();
                this.promisePage = this.currPage;
                //move data over
                this.data[2] = this.data[1];
                this.data[1] = this.data[0];
                this.lastPromise = this.fetchPageIntoPos(0);
            }
        }
        
    }
    getPage(): Company[] {
        if(this.finishedSetUp) {
            return this.data[1].getPage(this.currPage);
        }
        else {
            return [];
        }
    }
    getPageNr(): number {
        return this.currPage;
    }
}