import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './common/home/home.component';
import { ListCompaniesComponent } from './features/companies/list-companies/list-companies.component';
import { EditCompanyComponent } from './features/companies/edit-company/edit-company.component';
import { DeleteConfirmationComponent } from './common/delete-confirmation/delete-confirmation.component';
import { AddCompanyComponent } from './features/companies/add-company/add-company.component';
import { ByAvgSalaryComponent } from './features/companies/by-avg-salary/by-avg-salary.component';

const routes: Routes = [
  {
    path: "",
    component: HomeComponent
  },
  {
    path: "companies/add",
    component: AddCompanyComponent
  },
  {
    path: "companies/by-avg-salary",
    component: ByAvgSalaryComponent
  },
  {
    path: "companies/:id",
    component: EditCompanyComponent
  },
  {
    path: "companies",
    component: ListCompaniesComponent
  },
  {
    path: "delete-confirmation",
    component: DeleteConfirmationComponent
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
