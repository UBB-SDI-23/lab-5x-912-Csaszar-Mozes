import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './common/home/home.component';
import { ListCompaniesComponent } from './features/companies/list-companies/list-companies.component';
import { EditCompanyComponent } from './features/companies/edit-company/edit-company.component';
import { DeleteConfirmationComponent } from './common/delete-confirmation/delete-confirmation.component';
import { AddCompanyComponent } from './features/companies/add-company/add-company.component';
import { ByAvgSalaryComponent } from './features/companies/by-avg-salary/by-avg-salary.component';
import { ListLocationsComponent } from './features/locations/list-locations/list-locations.component';
import { ListPcComponent } from './features/pc/list-pc/list-pc.component';
import { ListPeopleComponent } from './features/people/list-people/list-people.component';
import { AddLocationComponent } from './features/locations/add-location/add-location.component';
import { AddPcComponent } from './features/pc/add-pc/add-pc.component';
import { AddPersonComponent } from './features/people/add-person/add-person.component';
import { EditLocationComponent } from './features/locations/edit-location/edit-location.component';
import { EditPcComponent } from './features/pc/edit-pc/edit-pc.component';
import { EditPersonComponent } from './features/people/edit-person/edit-person.component';
import { ByNrLocationsComponent } from './features/companies/by-nr-locations/by-nr-locations.component';
import { ReputationGreaterThanComponent } from './features/companies/reputation-greater-than/reputation-greater-than.component';
import { ViewUserPageComponent } from './features/users/view-user-page/view-user-page.component';
import { RegisterComponent } from './common/account/register/register.component';
import { LogInComponent } from './common/account/log-in/log-in.component';
import { UserProfile } from './models/models';
import { ProfileComponent } from './common/account/profile/profile.component';
import { ListUsersComponent } from './features/users/list-users/list-users.component';
import { GenerateDataComponent } from './features/admin/generate-data/generate-data.component';
import { SetPageSizeComponent } from './features/admin/set-page-size/set-page-size.component';

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
        path: "companies/by-nr-locations",
        component: ByNrLocationsComponent
    },
    {
        path: "companies/reputation-greater-than",
        component: ReputationGreaterThanComponent
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
        path: "locations",
        component: ListLocationsComponent
    },
    {
        path: "locations/add",
        component: AddLocationComponent
    },
    {
        path: "locations/:id",
        component: EditLocationComponent
    },
    {
        path: "pc",
        component: ListPcComponent
    },
    {
        path: "pc/add",
        component: AddPcComponent
    },
    {
        path: "pc/:id",
        component: EditPcComponent
    },
    {
        path: "people",
        component: ListPeopleComponent
    },
    {
        path: "people/add",
        component: AddPersonComponent
    },
    {
        path: "people/:id",
        component: EditPersonComponent
    },
    {
        path: "delete-confirmation",
        component: DeleteConfirmationComponent
    },
    {
        path: "users",
        component: ListUsersComponent
    },
    {
        path: "users/profile",
        component: ProfileComponent
    },
    {
        path: "users/:id",
        component: ViewUserPageComponent
    },
    {
        path: "register",
        component: RegisterComponent
    },
    {
        path: "login",
        component: LogInComponent
    },
    {
        path: "admin/generate-data",
        component: GenerateDataComponent
    },
    {
        path: "admin/set-page-size",
        component: SetPageSizeComponent
    },
];

@NgModule({
    imports: [RouterModule.forRoot(routes)],
    exports: [RouterModule]
})
export class AppRoutingModule { }
