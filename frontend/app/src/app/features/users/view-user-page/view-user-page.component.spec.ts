import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ViewUserPageComponent } from './view-user-page.component';

describe('ViewUserPageComponent', () => {
  let component: ViewUserPageComponent;
  let fixture: ComponentFixture<ViewUserPageComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ViewUserPageComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ViewUserPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
