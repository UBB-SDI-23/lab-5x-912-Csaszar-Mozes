import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';
import { MatInputModule } from '@angular/material/input';
import { MatTableModule } from '@angular/material/table';
import { MatFormFieldModule } from '@angular/material/form-field';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { MatButtonModule } from '@angular/material/button';
import { MatIconModule } from '@angular/material/icon';
import { MatOptionModule } from '@angular/material/core';
import { MatAutocompleteModule } from '@angular/material/autocomplete';
import { MatMenuModule } from '@angular/material/menu';
import { MatRadioModule } from '@angular/material/radio';
import { MatCheckboxModule } from '@angular/material/checkbox';
import { SocketIoModule } from 'ngx-socket-io';


import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HomeComponent } from './common/home/home.component';
import { ListCompaniesComponent } from './features/companies/list-companies/list-companies.component';
import { EditCompanyComponent } from './features/companies/edit-company/edit-company.component';
import { DeleteConfirmationComponent } from './common/delete-confirmation/delete-confirmation.component';
import { AddCompanyComponent } from './features/companies/add-company/add-company.component';
import { ByAvgSalaryComponent } from './features/companies/by-avg-salary/by-avg-salary.component';
import { ListAllPageComponent } from './common/list-all-page/list-all-page.component';
import { ListLocationsComponent } from './features/locations/list-locations/list-locations.component';
import { ListPcComponent } from './features/pc/list-pc/list-pc.component';
import { ListPeopleComponent } from './features/people/list-people/list-people.component';
import { AddLocationComponent } from './features/locations/add-location/add-location.component';
import { AddPersonComponent } from './features/people/add-person/add-person.component';
import { AddPcComponent } from './features/pc/add-pc/add-pc.component';
import { EditPcComponent } from './features/pc/edit-pc/edit-pc.component';
import { EditPersonComponent } from './features/people/edit-person/edit-person.component';
import { EditLocationComponent } from './features/locations/edit-location/edit-location.component';
import { DynamicTableComponent } from './common/dynamic-table/dynamic-table.component';
import { StaticTableComponent } from './common/static-table/static-table.component';
import { ByNrLocationsComponent } from './features/companies/by-nr-locations/by-nr-locations.component';
import { ReputationGreaterThanComponent } from './features/companies/reputation-greater-than/reputation-greater-than.component';
import { ViewUserPageComponent } from './features/users/view-user-page/view-user-page.component';
import { RegisterComponent } from './common/account/register/register.component';
import { LogInComponent } from './common/account/log-in/log-in.component';
import { AuthGuard } from '_helpers/auth.guard';
import { AuthInterceptor } from '_helpers/auth.interceptor';
import { ProfileComponent } from './common/account/profile/profile.component';
import { ErrorInterceptor } from '_helpers/error.interceptor';
import { ErrorMessagesComponent } from './common/error-messages/error-messages.component';
import { ListUsersComponent } from './features/users/list-users/list-users.component';
import { GenerateDataComponent } from './features/admin/generate-data/generate-data.component';
import { SetPageSizeComponent } from './features/admin/set-page-size/set-page-size.component';
import { ChatComponent } from './common/chat/chat.component';


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    ListCompaniesComponent,
    EditCompanyComponent,
    DeleteConfirmationComponent,
    AddCompanyComponent,
    ByAvgSalaryComponent,
    ListAllPageComponent,
    ListLocationsComponent,
    ListPcComponent,
    ListPeopleComponent,
    AddLocationComponent,
    AddPersonComponent,
    AddPcComponent,
    EditPcComponent,
    EditPersonComponent,
    EditLocationComponent,
    DynamicTableComponent,
    StaticTableComponent,
    ByNrLocationsComponent,
    ReputationGreaterThanComponent,
    ViewUserPageComponent,
    RegisterComponent,
    LogInComponent,
    ProfileComponent,
    ErrorMessagesComponent,
    ListUsersComponent,
    GenerateDataComponent,
    SetPageSizeComponent,
    ChatComponent
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
    MatIconModule,
    MatOptionModule,
    MatAutocompleteModule,
    MatMenuModule,
    MatRadioModule,
    MatCheckboxModule,
    //SocketIoModule.forRoot({ url: 'http://localhost:8000/api/', options: {} }),
  ],
  providers: [
    AuthGuard,
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true
    },
    {
      provide: HTTP_INTERCEPTORS,
      useClass: ErrorInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
