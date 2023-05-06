import { Component, Input } from '@angular/core';
import { NavigationEnd, Router } from '@angular/router';
import { AppComponent } from 'src/app/app.component';

@Component({
  selector: 'app-error-messages',
  templateUrl: './error-messages.component.html',
  styleUrls: ['./error-messages.component.css']
})
export class ErrorMessagesComponent {
  static errors: Object = {};
  static timeout?: number = undefined;

  constructor(private router: Router) { }

  getValues(value: Function) {
    return value as unknown as Array<string>;
  }

  hasErrors() {
    return Object.keys(ErrorMessagesComponent.errors).length > 0;
  }

  getErrors(): Object {
    return ErrorMessagesComponent.errors;
  }

  static setError(error: Object) {
    this.clearError();
    this.errors = error;
    //this.timeout = window.setTimeout(() => ErrorMessagesComponent.clearError(), 30000);
  }

  static clearError() {
    if (this.timeout != undefined) {
      clearTimeout(this.timeout);
    }
    this.timeout = undefined;
    this.errors = {};
  }

  ngOnInit() {
    this.router.events.subscribe(event => {
      if (event instanceof NavigationEnd) {
        ErrorMessagesComponent.clearError();
      }
    })
  }
}
