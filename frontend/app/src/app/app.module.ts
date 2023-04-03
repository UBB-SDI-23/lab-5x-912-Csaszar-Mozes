import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import {MatInputModule} from '@angular/material/input';
import { MatTableModule } from '@angular/material/table';
import {MatFormFieldModule} from '@angular/material/form-field';
import {ReactiveFormsModule, FormsModule} from '@angular/forms';
import {MatButtonModule} from '@angular/material/button'
import {MatIconModule} from '@angular/material/icon'



import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HomeComponent } from './common/home/home.component';
import { ListCompaniesComponent } from './features/companies/list-companies/list-companies.component';
import { EditCompanyComponent } from './features/companies/edit-company/edit-company.component';
import { DeleteConfirmationComponent } from './common/delete-confirmation/delete-confirmation.component';
import { AddCompanyComponent } from './features/companies/add-company/add-company.component';
import { ByAvgSalaryComponent } from './features/companies/by-avg-salary/by-avg-salary.component';

@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    ListCompaniesComponent,
    EditCompanyComponent,
    DeleteConfirmationComponent,
    AddCompanyComponent,
    ByAvgSalaryComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    HttpClientModule,
    MatTableModule,
    FormsModule,
    ReactiveFormsModule,
    MatFormFieldModule,
    MatInputModule,
    MatButtonModule,
    MatIconModule
    

  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
